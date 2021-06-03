from django.db import models


class Listing(models.Model):

    city = models.CharField(
        verbose_name='city',
        max_length=255,
    )

    def __str__(self):
        return f'Listing de {self.city}'
