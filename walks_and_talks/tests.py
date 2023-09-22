from django.test import TestCase
import pytest
from walks_and_talks.models import ElectoralCommittee


# wymogi:
# 3 testy do głównych funkcjonalności
# 2 testy do widoku

# testowane główne funkcjonalności:
# A. Dodawanie komitetu wyborczego, edycja jego danych i usuwanie go
# B. Przypisywanie poparcia w procentach komitetowi wyborczemu, w celu
# uzyskania informacji, czy komitet zdobył jakieś mandaty w wyborach
# do polskiego Sejmu, a jeśli tak, to ile mandatów zdobył
# C. dodawanie przez zalogowanego użytkownika plusów albo minusów
# metody D'Hondta i wyświetlanie ich na stronie internetowej

# testowane widoki:
# D. DHondtMethodView
# E. AddElectoralCommitteeView
# F. EditElectoralCommitteeView
# G. DeleteElectoralCommitteeView
# H. MethodsAdvantagesAndDisadvantagesView

# TESTY - FUNKCJONALNOŚCI
# ad A Dodawanie komitetu wyborczego, edycja jego danych i usuwanie go
# test 1
@pytest.mark.django_db
def test_add_electoral_committee_view_1(client):
    response = client.get('/society/addcommittee/')
    assert response.status_code == 200


# test 2
@pytest.mark.django_db
def test_add_electoral_committee_view_2(client):
    committee_name = '3 x ok'
    is_coalition = 'Yes'  # użytkownik podał w formularzu prawidłowe dane
    # nazwa komitetu się nie powtarza - przekierowanie na /society/dHondt/
    response = client.post('/society/addcommittee/', {'committee_name': committee_name,
                                                      'is_coalition': is_coalition})
    assert response.status_code == 302


# test 3
@pytest.mark.django_db
def test_add_electoral_committee_view_3(client, add_electoral_committee):
    committee_name = 'We Are The Best'
    is_coalition = "Yes"  # użytkownik podał w formularzu wymagane dane
    # ale nazwa komitetu się nie powtarza
    response = client.post('/society/addcommittee/', {'committee_name': committee_name,
                                                      'is_coalition': is_coalition})
    assert response.status_code == 200


# ad B Przypisywanie poparcia w procentach komitetowi wyborczemu...
# test 1
@pytest.mark.django_db
def test_dHondt_method_view(client, dHondt_electoral_committees, method):
    response = client.get('/society/dHondt/', {'electoral_committees': dHondt_electoral_committees,
                                               'method': method})
    assert response.status_code == 200
    assert len(response.context['ctx'][0]) == 2


# test 2, 3...
@pytest.mark.parametrize("support_1, support_2, result_1, result_2", (
    (33, 17, 152, 78),
    (15.5, 35.75, 71, 164),
    (3, 44, 'Brak mandatów. Komitet nie przekroczył progu 5%', 202),
    (42.5, 6, 196, 'Brak mandatów. Komitet nie przekroczył progu 8%')
))
@pytest.mark.django_db
def test_dHondt_method_view_calculations(support_1, support_2, result_1, result_2,
                                         client, dHondt_electoral_committees, method):
    support = [support_1, support_2]
    response = client.post('/society/dHondt/', {'electoral_committees': dHondt_electoral_committees,
                                                'method': method, 'support': support})
    assert response.status_code == 200
    assert response.context['ctx'][5][0][2] == result_1
    assert response.context['ctx'][5][1][2] == result_2


# ad C dodawanie przez zalogowanego użytkownika plusów albo minusów metody D'Hondta...
# test 1
@pytest.mark.django_db
def test_methods_advantages_and_disadvantages_view_1(client):
    response = client.get('/society/aboutmethods/')  # klient niezalogowany,
    # przekierowanie do widoku logowania
    assert response.status_code == 302


# test 2
@pytest.mark.django_db
def test_methods_advantages_and_disadvantages_view_2(client, user, method):
    client.login(username='nohtyp', password='nohtyp777')
    feature_of_method = 'It is ok'
    advantage_or_disadvantage = 'advantage'
    methods = ['dHondt']  # użytkownik zalogowany, przekazane wszystkie potrzebne dane
    # przekierowanie na /society/dHondt
    response = client.post('/society/aboutmethods/', {'feature_of_method': feature_of_method,
                                                      'advantage_or_disadvantage':
                                                          advantage_or_disadvantage,
                                                      'methods': methods})
    assert response.status_code == 302


# test 3
@pytest.mark.django_db
def test_methods_advantages_and_disadvantages_view_3(client, user):
    client.login(username='nohtyp', password='nohtyp777')
    feature_of_method = 'It is ok'
    advantage_or_disadvantage = 'advantage'  # użytkownik zalogowany, ale nie podał
    # wszystkich potrzebnych danych - wraca do formularza
    response = client.post('/society/aboutmethods/', {'feature_of_method': feature_of_method,
                                                      'advantage_or_disadvantage':
                                                          advantage_or_disadvantage})
    assert response.status_code == 200

# TESTY WIDOKI
# ad D DHondtMethodView
# test 1, test 2 - widok przetestowany w części B

# ad E AddElectoralCommitteeView
# test 1, test 2 - widok przetestowany w części A


# ad F EditElectoralCommitteeView
# test 1
@pytest.mark.django_db
def test_edit_electoral_committee_view_1(client, add_electoral_committee):
    committee_id = add_electoral_committee.id
    response = client.get(f'/society/editcommittee/{committee_id}/')
    assert response.status_code == 200


# test 2
@pytest.mark.django_db
def test_edit_electoral_committee_view_2(client, add_electoral_committee):
    committee_id = add_electoral_committee.id
    committee_name = '3 x ok'   # nazwy nie ma w bazie danych
    response = client.post(f'/society/editcommittee/{committee_id}/',
                           {'committee_name': committee_name})
    assert response.status_code == 302
    assert ElectoralCommittee.objects.get(id=committee_id).committee_name == committee_name


# ad G DeleteElectoralCommitteeView
# test 1
@pytest.mark.django_db
def test_delete_electoral_committee_view_1(client, add_electoral_committee):
    committee_id = add_electoral_committee.id
    response = client.get(f'/society/deletecommittee/{committee_id}/')
    assert response.status_code == 302


# test 2
@pytest.mark.django_db
def test_delete_electoral_committee_view_2(client, add_electoral_committee):
    committee_id = add_electoral_committee.id
    client.get(f'/society/deletecommittee/{committee_id}/')
    assert not ElectoralCommittee.objects.filter(id=committee_id)


# ad H MethodsAdvantagesAndDisadvantagesView
# test 1, test 2 - widok przetestowany w częci C
