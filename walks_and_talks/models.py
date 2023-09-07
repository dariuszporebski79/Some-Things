from django.db import models


class
class DemocracyPositiveOpinions(models.Model):
    opinion = models.TextField(unique=True)
    comment = models.TextField()


class DemocracyNegativeOpinions(models.Model):
    opinion = models.TextField(unique=True)
    comment = models.TextField()


class ElectoralCommittee(models.Model):
    committee_name = models.CharField(max_length=255, unique=True)
    is_coalition = models.BooleanField()


class Constituencies(models.Model):
    number = models.SmallIntegerField(unique=True)
    seat_of_commission = models.CharField(max_length=50)
    description = models.TextField()
    number_of_mandates = models.SmallIntegerField()
    number_of_voters = models.IntegerField()

# class Room(models.Model):
#     room_name = models.CharField(max_length=255, unique=True)
#     room_capacity = models.SmallIntegerField()
#     projector_availability = models.BooleanField()
#
#
# class RoomReservation(models.Model):
#     room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
#     date_of_reservation = models.DateField()
#     comment = models.TextField(default="No comment")
