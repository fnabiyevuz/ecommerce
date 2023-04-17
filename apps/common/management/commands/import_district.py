import yaml
from django.core.management.base import BaseCommand, CommandError

from ...models import District


class Command(BaseCommand):
    help = "Import districts from a yaml file"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.HTTP_NOT_MODIFIED(
                "Import districts... wait...",
            )
        )
        # District.objects.all().delete()
        try:
            with open(
                    "apps/common/management/source/districts.yaml",
                    "r",
            ) as yaml_file:
                data = yaml.safe_load(yaml_file)
                i = 0
                for item in data:
                    District.objects.create(region_id=item["region_id"],
                                            name=item["name_uz"],
                                            )
                    i += 1
        except FileNotFoundError as e:
            raise CommandError("File districs yaml doesn't exists") from e

        self.stdout.write(self.style.SUCCESS(f"{str(i)} districts successfully imported"))
