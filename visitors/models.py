from __future__ import unicode_literals
from django.db import models


class Visitor(models.Model):
    username = models.CharField(max_length=20)

    def __str__(self):
        return self.username



