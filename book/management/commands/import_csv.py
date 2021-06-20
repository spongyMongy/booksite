import csv
import os
from django.apps import apps
from django.core.management.base import BaseCommand, CommandError
from book.models import Books,Opinions



class Command(BaseCommand):
    help = "Insert Books and Opinions CSV file. " \
           "Be sure that Books file is uploaded first. " \


    def get_csv_file(self, filename):
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
                ifile = open(file_path, encoding='utf8')
                read = csv.reader(ifile)
                i = 0
                for row in read:

                    if i != 0:
                        if self.model_name ==Books:
                            try:
                                book_objects = Books.objects.get_or_create(ISBN=row[0].split(';')[0], title=row[0].split(';')[1],
                                                                author=row[0].split(';')[2], type=row[0].split(';')[3])
                                book_objects[0].save()
                            except:
                                print("there was a problem with lineBooks")

                        elif self.model_name ==Opinions:
                            try:
                                corresponding_book = Books.objects.get(ISBN=row[0].split(';')[0])
                                opinion_objects = Opinions.objects.get_or_create(ISBN=corresponding_book, rating=row[0].split(';')[1],
                                                            description=row[0].split(';')[2])

                                opinion_objects[0].save()
                            except Exception as e:
                                print (e)
                                print("!Please be sure .CSV typed 'Book' file is uploaded first")
                                return
                    i += 1

            except FileNotFoundError:
                raise CommandError("File at {} does not exist, please be sure it exists in this location ".format(
                    'file_path'))

