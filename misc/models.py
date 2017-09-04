from django.db import models


class Software(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Setting(models.Model):
    key = models.CharField(max_length=64, primary_key=True)
    value = models.TextField()

    def __str__(self):
        return self.key

    def get_str(self):
        return self.value

    def get_int(self):
        return int(self.value)

    def get_bool(self):
        return self.value == "True"
