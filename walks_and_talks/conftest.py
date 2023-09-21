import pytest
from django.test import Client
from walks_and_talks.models import (ElectoralCommittee, AllocatingMethodsAdvantages,
                                    AllocatingMethodsDisadvantages, AllocatingMandatesMethods)


@pytest.fixture
def add_electoral_committee():
    electoral_committee = ElectoralCommittee.objects.create(committee_name="We Are The Best",
                                                            is_coalition=False)
    return electoral_committee


@pytest.fixture
def edit_electoral_committee():
    electoral_committee = ElectoralCommittee.objects.create(committee_name='We Are The Best',
                                                            is_coalition=False)
    electoral_committee.committee_name = 'We Will Win'
    electoral_committee.save()
    return electoral_committee


@pytest.fixture
def delete_electoral_committee():
    electoral_committee = ElectoralCommittee.objects.create(committee_name='We Are The Best',
                                                            is_coalition=False)
    electoral_committee.delete()
    return ':-)'


@pytest.fixture
def method():
    method = AllocatingMandatesMethods.objects.create(name="metoda d'Hondta",
                                                      short_information="metoda d'Hondta")
    return method


@pytest.fixture
def dHondt_electoral_committees():
    electoral_committee_1 = ElectoralCommittee.objects.create(committee_name="We Are The Best",
                                                            is_coalition=False)
    electoral_committee_2 = ElectoralCommittee.objects.create(committee_name="We Will Win",
                                                            is_coalition=True)
    electoral_committees = ElectoralCommittee.objects.all()
    return electoral_committees


@pytest.fixture
def method_advantage():
    method_1 = AllocatingMandatesMethods.objects.create(name='funny method',
                                                        short_information='funny method is not sad')
    method_2 = AllocatingMandatesMethods.objects.create(name='sad method',
                                                        short_information='sad method is not funny')
    advantage = AllocatingMethodsAdvantages.objects.create(advantage='It is ok')
    advantage.methods.set([method_1, method_2])
    return advantage


# test 2
@pytest.fixture
def method_disadvantage():
    method_1 = AllocatingMandatesMethods.objects.create(name='funny method',
                                                        short_information='funny method is not sad')
    method_2 = AllocatingMandatesMethods.objects.create(name='sad method',
                                                        short_information='sad method is not funny')
    disadvantage = AllocatingMethodsDisadvantages.objects.create(disadvantage='It is bad')
    disadvantage.methods.set([method_1, method_2])
    return disadvantage


@pytest.fixture
def client():
    client = Client()
    return client


# materiały:
# Zadanie 4 fixtura
# @pytest.fixture
# def add_some_products():
#     products = [
#         Product.objects.create(
#             name=f"Produkt_{i}",
#             description=f"Opis produktu {i}",
#             price=150 + (i * 100)
#         ) for i in range(3)
#     ]
#     return products
