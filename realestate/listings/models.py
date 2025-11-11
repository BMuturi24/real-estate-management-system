from django.db import models
from properties.models import Property


class Listing(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='listings')
    is_active = models.BooleanField(default=True)
    listed_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)


    def __str__(self):
        return f"Listing for {self.property.title} ({'active' if self.is_active else 'inactive'})"