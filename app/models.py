from dataclasses import dataclass
from django.db import models

@dataclass
class Actor(models.Model):
    first_name: str
    last_name: str
# add dataclass here