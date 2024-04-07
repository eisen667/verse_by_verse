import requests
from .models import Sura, Aya
"""
Get list of Suras
"""
response = requests.get("http://api.alquran.cloud/v1/surah/1")
surah_data = response.json()

"""
Create Sura model objects for all Suras
"""
for surah in surah_data:
  Sura.objects.create(
      number=surah["number"],
      name=surah["name"],
      englishName = surah["englishName"],
      englishNameTranslation = surah["englishNameTranslation"],
      numbersofAyahs=surah.get("numberOfAyahs", None),
      revelationType = surah["revelationType"]
  )

