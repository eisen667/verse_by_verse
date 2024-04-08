from django.core.management.base import BaseCommand
from requests import get
from ...models import Sura

class Command(BaseCommand):
    help = "Fetches Quran Surah data from the API and populates the Sura model."

    def handle(self, *args, **options):
        response = get("http://api.alquran.cloud/v1/surah")
        if response.status_code == 200:
            data = response.json()
            for surah_info in data['data']:
                sura, created = Sura.objects.get_or_create(
                    number=surah_info['number'],
                    defaults={
                        'name': surah_info['name'],
                        'englishName': surah_info['englishName'],
                        'englishNameTranslation': surah_info['englishNameTranslation'],
                        'numberofAyahs': surah_info['numberOfAyahs'],
                        'revelationType': surah_info['revelationType'],
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Sura {sura.number} - {sura.name} created."))
                else:
                    self.stdout.write(self.style.WARNING(f"Sura {sura.number} - {sura.name} already exists, skipping update."))
        else:
            self.stdout.write(self.style.ERROR(f"API request failed with status code: {response.status_code}"))

