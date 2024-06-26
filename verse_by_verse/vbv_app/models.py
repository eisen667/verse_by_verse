from django.db import models

# Create your models here.

class Sura(models.Model):
    """
    Model for a Sura (Chapter) of the Quran.
    """
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=128)
    englishName = models.CharField(max_length=128)
    englishNameTranslation = models.CharField(max_length=128)
    numberofAyahs = models.IntegerField()
    revelationType = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.number} : {self.name} : {self.englishName}"
    
class Aya(models.Model):
    """
    Model for verse (Ayah) of the Quran.
    """
    verse_key = models.CharField(primary_key=True, default=0, max_length=128)
    sura = models.ForeignKey(Sura, on_delete=models.CASCADE)
    aya_number = models.IntegerField()
    arabic_text = models.TextField()
    english_translation = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Sura {self.sura.name}, Ayah {self.aya_number}"

class Qari(models.Model):
    """
    Model for a Quran reciter (Qari).
    """
    qari_name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.qari_name

"""
Data importing using http://api.alquran.cloud/v1/ API
"""



