from django.db import models
from legislators.models import Legislator


class Bill(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=500)
    primary_sponsor = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'bills_bill'

