from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Load seed data for categories, brands, and products."

    def handle(self, *args, **options):
        call_command("loaddata", "seed.json", app_label="core")
        self.stdout.write(self.style.SUCCESS("Seed data loaded."))
