from django.db import models

# Create your models here.
class Superhero(models.Model):

    name = models.CharField(max_length=200)

    POWER_OPTIONS = (
        ("strength", "Super Strength"),
        ("speed", "Super Speed"),
        ("flying", "Flying"),
        ("telepathy", "Telepathy"),
        ("invisibility", "Invisibility"),
        ("healing", "Healing"),
        ("technology", "Advanced Technology"),
        ("magic", "Magic"),
        ("time_travel", "Time Travel"),
        ("energy", "Energy Manipulation"),
        ("other", "Other"),
    )

    power = models.CharField(
        max_length=200,
        choices=POWER_OPTIONS,
        default="other"
    )

    city = models.CharField(max_length=200)

    age = models.PositiveIntegerField()

    TEAM_OPTIONS = (
        ("avengers", "Avengers"),
        ("justice_league", "Justice League"),
        ("xmen", "X-Men"),
        ("guardians", "Guardians"),
        ("fantastic_four", "Fantastic Four"),
        ("other", "Other"),
    )

    team = models.CharField(
        max_length=200,
        choices=TEAM_OPTIONS,
        default="other"
    )

    real_name = models.CharField(max_length=200)

    # String representation of object
    def __str__(self):
        return self.name