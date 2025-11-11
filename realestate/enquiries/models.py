from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
