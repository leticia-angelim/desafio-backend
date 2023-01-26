from django.db import models


class Cnab(models.Model):
    type = models.CharField(max_length=1)
    date = models.CharField(max_length=8)
    value = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.CharField(max_length=6)
    owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)

    def __str__(self) -> str:
        return self.store_name
