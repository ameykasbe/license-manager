from django.db import models

class Software(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return str(self.name)

class Recipient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)

class License(models.Model):
    INDIVIDUAL = "indiv"
    GROUP = "grp"
    LICENSE_TYPE_CHOICES =  ((INDIVIDUAL, "Individual"), (GROUP, "Group"))

    software = models.ForeignKey(Software, on_delete=models.RESTRICT)
    type = models.CharField(max_length=50, choices=LICENSE_TYPE_CHOICES, default=INDIVIDUAL)
    start_date = models.DateField()
    expiration_date = models.DateField()
    recipients = models.ManyToManyField(Recipient)
    max_users = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.software.name + ": " + dict(self.LICENSE_TYPE_CHOICES).get(self.type)
