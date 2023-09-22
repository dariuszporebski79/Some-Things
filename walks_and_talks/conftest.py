import pytest
from django.test import Client
from django.contrib.auth.models import User
from walks_and_talks.models import (ElectoralCommittee, AllocatingMandatesMethods)


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def add_electoral_committee():
    electoral_committee = ElectoralCommittee.objects.create(committee_name='We Are The Best',
                                                            is_coalition=False)
    return electoral_committee


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
def user():
    user = User.objects.create_superuser('nohtyp', 'nohtyp@nohtyp.com', 'nohtyp777')
    return user
