from django.db import models


class AllocatingMandatesMethods(models.Model):
    name = models.CharField(max_length=255, unique=True)
    short_information = models.TextField()
    link_more_information = models.TextField(null=True)

    def __str__(self):
        return self.name


class People(models.Model):
    name_and_surname = models.CharField(max_length=255)
    years_of_life = models.CharField(max_length=50)
    short_information = models.TextField()
    more_information = models.TextField()
    link_photo = models.TextField(null=True)
    link_biography = models.TextField(null=True)
    allocating_mandates_method = models.ForeignKey(AllocatingMandatesMethods,
                                                   on_delete=models.SET_NULL, null=True)


class DemocracyPositiveOpinions(models.Model):
    opinion = models.TextField(unique=True)
    comment = models.TextField()
    author = models.ForeignKey(People, on_delete=models.CASCADE)


class DemocracyNegativeOpinions(models.Model):
    opinion = models.TextField(unique=True)
    comment = models.TextField()
    author = models.ForeignKey(People, on_delete=models.CASCADE)


class ElectoralCommittee(models.Model):
    committee_name = models.CharField(max_length=255, unique=True)
    is_coalition = models.BooleanField()


class Constituencies(models.Model):
    number = models.SmallIntegerField(unique=True)
    seat_of_commission = models.CharField(max_length=50)
    description = models.TextField()
    number_of_mandates = models.SmallIntegerField()
    number_of_voters = models.IntegerField()

    def __str__(self):
        return self.seat_of_commission


class AllocatingMethodsAdvantages(models.Model):
    advantage = models.TextField()
    methods = models.ManyToManyField(AllocatingMandatesMethods)


class AllocatingMethodsDisadvantages(models.Model):
    disadvantage = models.TextField()
    methods = models.ManyToManyField(AllocatingMandatesMethods)
