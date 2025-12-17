from django.db import models
from bills.models import Bill


class Vote(models.Model):
    id = models.IntegerField(primary_key=True)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, db_column='bill_id')

    class Meta:
        db_table = 'votes_vote'

