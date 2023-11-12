from django.db import models

class Profile(models.Model):
    luas_wilayah = models.CharField(max_length=100)
    penduduk = models.CharField(max_length=100)
    pemerintahan = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.luas_wilayah}"

class Sumenep(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    kota = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.kota}"
