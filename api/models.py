from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_future_date(value):
    if value <= timezone.now().date():
        raise ValidationError('Date must be in the future.')

class Event(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()
    date=models.DateField(validators=[validate_future_date])
    location=models.CharField(max_length=20)
