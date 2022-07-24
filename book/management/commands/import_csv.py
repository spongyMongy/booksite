import csv
import os
from django.apps import apps
from django.core.management.base import BaseCommand, CommandError
from book.models import Books, Opinions


class Command(BaseCommand):

    def __init__(self, model_name):
        super().__init__()
        self.model_name = model_name

    @staticmethod
    def get_csv_file(filename):
        app_path = apps.get_app_config('book').path
        file_path = os.path.join(app_path, "management", filename)
        return file_path

    def add_arguments(self, parser):
        parser.add_argument('filenames',
                            nargs='+',
                            type=str,
                            help="Inserting  CSV files names")
        parser.add_argument(
            '--books',
            action='store_true',
            help='Insert Books csv files',
        )
        parser.add_argument(
            '--opinions',
            action='store_true',
            help='Insert Opinions csv files',
        )

    def handle(self, *args, **options):
        if options['books']:
            self.model_name = Books

        if options['opinions']:
            self.model_name = Opinions

        for filename in options['filenames']:
            self.stdout.write(self.style.SUCCESS('Reading:{}'.format(filename)))
            file_path = self.get_csv_file(filename)
            try:
                with open(file_path, encoding='utf8') as opened_file:
                    # opened_file = open(file_path, encoding='utf8')
                    read = csv.reader(opened_file)
                    number = 0
                    split_row = row[0].split(';')
                    for row in read:
                        if number != 0:
                            if self.model_name == Books:
                                try:
                                    book_objects = Books.objects.get_or_create(
                                        ISBN=split_row[0],
                                        title=split_row[1],
                                        author=split_row[2],
                                        type=split_row[3])
                                except:
                                    print("there was a problem with lineBooks")

                            elif self.model_name == Opinions:
                                try:
                                    corresponding_book = Books.objects.get(
                                        ISBN=split_row[0])
                                    opinion_objects = Opinions. \
                                        objects.get_or_create \
                                            (
                                            ISBN=corresponding_book,
                                            rating=split_row[1],
                                            description=split_row[2]
                                        )
                                except Exception as exception:
                                    print(exception)
                                    print(
                                        "!Please be sure .CSV typed 'Book' "
                                        "file is uploaded first")
                                    return
                        number += 1

            except FileNotFoundError:
                raise CommandError(
                    "File at {} does not exist, "
                    "please be sure it exists in this"
                    " location ".format(
                        'file_path'))
