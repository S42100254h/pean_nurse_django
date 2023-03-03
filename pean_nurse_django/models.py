from django.db import models


class User(models.Model):
    name = models.CharField(blank=False, max_length=32)
    email = models.EmailField(null=True)

    def __str__(self):
        return "{}: {}".format(self.pk, self.name)
