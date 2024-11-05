from django.db import models
from django.utils import timezone

class PasswordResetToken(models.Model):
    Email = models.EmailField()
    token = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        # Token is valid for 1 hour
        expiration_time = self.created_at + timezone.timedelta(hours=1)
        return timezone.now() < expiration_time
