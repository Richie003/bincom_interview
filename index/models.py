from email.policy import default
from django.db import models

# Create your models here.
class AgentName(models.Model):
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255, null=False)
    email = models.CharField(default="", max_length=255, null=False)
    phone = models.CharField(max_length=13, null=False)
    pollingunit_uniqueid = models.UUIDField()

    def __str__(self):
        return str(self.firstname)

class Announced_lga_results(models.Model):
    lga_name = models.CharField(default="", max_length=50, null=False)
    party_abbreviation = models.CharField(default="", max_length=4, null=False)
    party_score = models.IntegerField(null=False)
    entered_by_user = models.CharField(default="", max_length=50, null=False)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(default="", max_length=50, null=False)

    def __str__(self):
        return str(f'{self.lga_name} {self.entered_by_user}')

class Announced_pu_results(models.Model):
    polling_unit_uniqueid = models.CharField(default="", max_length=50, null=True)
    party_abbreviation = models.CharField(default="", max_length=4, null=True)
    party_score = models.IntegerField(null=True)
    entered_by_user = models.CharField(default="", max_length=50, null=True)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(default="", max_length=50, null=True)

    def __str__(self):
        return str(f'{self.party_abbreviation} {self.polling_unit_uniqueid}')

class Announced_state_results(models.Model):
    state_name = models.CharField(default="", max_length=50, null=True)
    party_abbreviation = models.CharField(default="", max_length=4, null=True)
    party_score = models.IntegerField(null=True)
    entered_by_user = models.CharField(default="", max_length=50, null=True)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(default="", max_length=50, null=True)

    def __str__(self):
        return str({self.state_name})

class Announced_ward_results(models.Model):
    ward_name = models.CharField(default="", max_length=50, null=True)
    party_abbreviation = models.CharField(default="", max_length=4, null=True)
    party_score = models.IntegerField(null=True)
    entered_by_user = models.CharField(default="", max_length=50, null=True)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(default="", max_length=50, null=True)

    def __str__(self):
        return str({self.ward_name})

class LGA(models.Model):
    lga_id = models.IntegerField(null=True)
    lga_name = models.CharField(default="", max_length=50, null=True)
    state_id = models.IntegerField(null=True)
    lga_description = models.TextField(default="", max_length=255, null=True)
    entered_by_user = models.CharField(default="", max_length=50, null=True)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(default="", max_length=50, null=True)

    def __str__(self):
        return str(self.lga_name)

class Party(models.Model):
    partyid = models.CharField(max_length=11, null=True)
    partyname = models.CharField(max_length=11, null=True)

class Polling_unit(models.Model):
    polling_unit_id = models.IntegerField(null=True)
    ward_id = models.IntegerField(null=True)
    lga_id = models.IntegerField(null=True, blank=True)
    uniquewardid = models.IntegerField(null=True)
    polling_unit_number = models.CharField(default="", max_length=50, null=True)
    # polling_unit_number = models.CharField(default="", max_length=50, null=True)
    polling_unit_name = models.CharField(default="", max_length=50, null=True)
    polling_unit_description = models.TextField(default="")
    lat = models.CharField(default="", max_length=255,null=True)
    long = models.CharField(default="", max_length=255,null=True)
    entered_by_user = models.CharField(default="", max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(default="", max_length=50)

    def __str__(self):
        return str(self.lga_id)

class States(models.Model):
    state_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.state_name)

class Ward(models.Model):
    ward_id = models.IntegerField(null=True)
    ward_name = models.CharField(max_length=50, null=True)
    lga_id = models.IntegerField(null=True)
    ward_description = models.TextField(default="")
    entered_by_user = models.CharField(default="", max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(default="", max_length=50, null=True)

    def __str__(self):
        return str(self.ward_name)