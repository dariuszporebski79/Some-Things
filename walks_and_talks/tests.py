from django.test import TestCase
import pytest
from walks_and_talks.models import (ElectoralCommittee, AllocatingMethodsAdvantages,
                                    AllocatingMethodsDisadvantages)


# testowane główne funkcjonalności aplikacji:
# A. Dodawanie komitetu wyborczego, edycja jego danych i usuwanie go
# B. przypisywanie poparcia w procentach komitetowi wyborczemu, w celu
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
# ad A
# test 1
@pytest.mark.django_db
def test_add_electoral_committee(add_electoral_committee):
    assert len(ElectoralCommittee.objects.all()) == 1
    assert (ElectoralCommittee.objects.get(committee_name='We Are The Best')
            == add_electoral_committee)


# test 2
@pytest.mark.django_db
def test_edit_electoral_committee(edit_electoral_committee):
    assert len(ElectoralCommittee.objects.all()) == 1
    assert (ElectoralCommittee.objects.get(committee_name='We Will Win')
            == edit_electoral_committee)


# test 3
@pytest.mark.django_db
def test_delete_electoral_committee(delete_electoral_committee):
    assert len(ElectoralCommittee.objects.filter(committee_name='We Are The Best')) == 0


# ad B
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


# ad C
# test 1
@pytest.mark.django_db
def test_allocating_methods_advantages_model(method_advantage):
    assert len(AllocatingMethodsAdvantages.objects.all()) == 1
    assert (AllocatingMethodsAdvantages.objects.get(advantage='It is ok')
            == method_advantage)


# test 2
@pytest.mark.django_db
def test_allocating_methods_disadvantages_model(method_disadvantage):
    assert len(AllocatingMethodsDisadvantages.objects.all()) == 1
    assert (AllocatingMethodsDisadvantages.objects.get(disadvantage='It is bad')
            == method_disadvantage)


# test 3

# TESTY WIDOKI
# ad D
# test 1, test 2 - widok przetestowany w części B

# ad E
# test 1 - zobacz A, test 1 - test_add_electoral_committee
# test 2
@pytest.mark.django_db
def test_add_electoral_committee_view(client):
    response = client.get('/society/addcommittee/')
    assert response.status_code == 200


# ad F
# test 1 - zobacz A, test 2 - test_edit_electoral_committee
# test 2

# ad G
# test 1 - zobacz A, test 3 - test_delete_electoral_committee
# test 2

# ad H
# test 1 - zobacz C, test 1 - test_allocating_methods_advantages_model
# test 2 - zobacz C, test 2 - test_allocating_methods_disadvantages_model
# dodatkowy test:
@pytest.mark.django_db
def test_methods_advantages_and_disadvantages_view(client):
    response = client.get('/society/aboutmethods/')
    assert response.status_code == 200

# materiały:
# def test_details(client):
#     response = client.get('sith/list/')  # Pobieramy stronę metodą GET.
#     assert response.status_code == 200  # Czy odpowiedź HTTP to 200 OK.
#     # Czy widok zwrócił w kontekście DOKŁADNIE 2 Sithów?
#     assert len(response.context['sith']) == 2
# @pytest.mark.django_db
# def test_client_list_products(client, add_product):
#     response = client.get("/")
#     assert response.status_code == 200
#     assert add_product in response.context.get('products')
# Zadanie 3
# @pytest.mark.django_db
# def test_client_add_product():
#     client = Client()
#     new_product = {
#         "name": "Krzesło",
#         "description": "wygodne",
#         "price": 850,
#     }
#     response = client.post("/product/add/", new_product)
#     assert response.status_code == 302
#     assert Product.objects.filter(name=new_product["name"]).exists()
# Zadanie 4
# @pytest.mark.django_db
# def test_list_products(add_some_products):
#     client = Client()
#     response = client.get("/")
#     assert response.status_code == 200
#     for i in range(3):
#         assert add_some_products[i] == response.context.get('products')[i]
