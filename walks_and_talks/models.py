from django.db import models


class AllocatingMandatesMethods(models.Model):
    """The class represents methods of allocating of mandates in proportional elections.
    It includes name, short information about a method and optional link to more information."""
    name = models.CharField(max_length=255, unique=True)
    short_information = models.TextField()
    link_more_information = models.TextField(null=True)

    def __str__(self):
        return self.name


class People(models.Model):
    """The model represents famous people, authors of books and articles etc. It is for use
    in different views. The model has fields for name and surname, years of life, short information
    about a person, more information about a person, photo link, biography link and a foreign key
    to the AllocatingMandatesMethods model"""
    name_and_surname = models.CharField(max_length=255)
    years_of_life = models.CharField(max_length=50)
    short_information = models.TextField()
    more_information = models.TextField()
    link_photo = models.TextField(null=True)
    link_biography = models.TextField(null=True)
    allocating_mandates_method = models.ForeignKey(AllocatingMandatesMethods,
                                                   on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name_and_surname


class DemocracyPositiveOpinions(models.Model):
    """The model holds positive opinions on democracy with fields for opinion, comment and the author"""
    opinion = models.TextField(unique=True)
    comment = models.TextField()
    author = models.ForeignKey(People, on_delete=models.CASCADE)


class DemocracyNegativeOpinions(models.Model):
    """The model holds negative opinions on democracy with fields for opinion, comment and the author"""
    opinion = models.TextField(unique=True)
    comment = models.TextField()
    author = models.ForeignKey(People, on_delete=models.CASCADE)


class ElectoralCommittee(models.Model):
    """The class represents electoral committees. It includes a committee name
    and a boolean field indicating whether it's a coalition"""
    committee_name = models.CharField(max_length=255, unique=True)
    is_coalition = models.BooleanField()


class Constituencies(models.Model):
    """The class represents electoral constituencies. It includes number of constituency,
    seat of commission, description of constituency, number of mandates in constituency
    and number of voters in it"""
    number = models.SmallIntegerField(unique=True)
    seat_of_commission = models.CharField(max_length=50)
    description = models.TextField()
    number_of_mandates = models.SmallIntegerField()
    number_of_voters = models.IntegerField()

    def __str__(self):
        return self.seat_of_commission


class AllocatingMethodsAdvantages(models.Model):
    """The model lists advantages of allocating methods and has two fields: advantage and
    a many-to-many relationship with the AllocatingMandatesMethods model"""
    advantage = models.TextField()
    methods = models.ManyToManyField(AllocatingMandatesMethods)


class AllocatingMethodsDisadvantages(models.Model):
    """The model lists disadvantages of allocating methods and has two fields: disadvantage and
    a many-to-many relationship with the AllocatingMandatesMethods model"""
    disadvantage = models.TextField()
    methods = models.ManyToManyField(AllocatingMandatesMethods)
