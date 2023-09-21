import pytest
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
    electoral_committee.committee_name = "We Will Win"
    electoral_committee.save()
    return electoral_committee


@pytest.fixture
def delete_electoral_committee():
    electoral_committee = ElectoralCommittee.objects.create(committee_name='We Are The Best',
                                                            is_coalition=False)
    electoral_committee.delete()
    return ':-)'


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
