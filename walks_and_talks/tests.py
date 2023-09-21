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
# test 2
# test 3

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
# test 1
# test 2

# ad E
# test 1 - zobacz A, test 1 - test_add_electoral_committee
# test 2

# ad F
# test 1 - zobacz A, test 2 - test_edit_electoral_committee
# test 2

# ad G
# test 1 - zobacz A, test 3 - test_delete_electoral_committee
# test 2

# ad H
# test 1 - zobacz C, test 1 - test_allocating_methods_advantages_model
# test 2 - zobacz C, test 2 - test_allocating_methods_disadvantages_model
