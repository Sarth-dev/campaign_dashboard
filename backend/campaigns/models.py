from django.db import models

# Create your models here.

class Campaign(models.Model):
    PLATFORM_CHOICES = [
        ('Instagram', 'Instagram'),
        ('Facebook', 'Facebook'),
        ('Google', 'Google'),
    ]

    name = models.CharField(max_length=100)
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    clicks = models.IntegerField()
    impressions = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.platform})"
