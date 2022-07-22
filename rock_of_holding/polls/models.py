from django.db import models
from django.utils import timezone
import string, random

def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Poll.objects.filter(code=code).count() == 0:
            return code

class Poll(models.Model):
    code = models.CharField(max_length=8, default=generate_unique_code, unique=True, null=False)
    host = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now, null=False)
