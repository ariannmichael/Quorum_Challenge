from django.db import models

class LegislatorORM(models.Model):
  name = models.CharField(max_length=255)