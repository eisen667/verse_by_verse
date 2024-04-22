from django.core.management.base import BaseCommand
from requests import get
from ...models import Sura, Aya

# Define API endpoint URLs
arabic_text_url = "https://api.quran.com/api/v4/quran/verses/uthmani_simple?verse_key={verse_key}"
english_translation_url = "https://api.quran.com/api/v4/verses/by_key/{verse_key}?translations=131"

class Command(BaseCommand):
  help = "Fetches Quran Aya data from the API and populates the Aya model with English translation."

  def handle(self, *args, **options):
    # Get all Suras
    suralist = Sura.objects.all()

    all_ayas = []
    for sura in suralist:
      # Iterate through ayah numbers from 1 to numberofAyahs
      for ayah_number in range(1, sura.numberofAyahs + 1):
        # Construct verse key
        verse_key = f"{sura.number}:{ayah_number}"

        # Construct complete URLs with verse key
        arabic_url = arabic_text_url.format(verse_key=verse_key)
        english_url = english_translation_url.format(verse_key=verse_key)

        # Fetch data from both URLs
        arabic_response = get(arabic_url)
        english_response = get(english_url)

          # Check for successful responses
        if arabic_response.status_code == 200 and english_response.status_code == 200:
            arabic_data = arabic_response.json()
            english_data = english_response.json()

            # Extract data from JSON responses
            arabic_text = arabic_data['verses'][0]['text_uthmani_simple']
            english_translation = english_data['verse']['translations'][0]['text']
            
            # Create or update Aya object
            all_ayas.append(Aya(sura=sura, verse_key=verse_key, aya_number=ayah_number, arabic_text=arabic_text, english_translation=english_translation))
            # Print confirmation message (optional)
            Aya.objects.bulk_create(all_ayas)
            print("Aya data imported successfully!")
