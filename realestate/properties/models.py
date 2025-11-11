from django.db import models
from django.conf import settings


class Property(models.Model):
 owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
title = models.CharField(max_length=200)
description = models.TextField(blank=True)
address = models.CharField(max_length=300)
price = models.DecimalField(max_digits=12, decimal_places=2)
created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
 return f"{self.title} - {self.address}"