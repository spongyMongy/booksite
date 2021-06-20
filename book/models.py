from django.db import models

# ISBN;Tytuł;Autor;Gatunek;
class Books(models.Model):
    ISBN = models.IntegerField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.title



# ISNB;Ocena;Opis;
class Opinions(models.Model):
    ISBN = models.ForeignKey(
        'Books',
        on_delete=models.CASCADE,
    )
    rating = models.IntegerField()
    description = models.CharField(max_length=100)

    @property
    def star_finder(self):
        stars=''
        for x in range(self.rating):
            stars=stars+'*'
        return  stars

    @property
    def from_book(self):
        from_bookis= Books.objects.select_related().filter(id=self.ISBN_id).values(('title'))
        return from_bookis[0]['title']

    def __str__(self):
        return self.description

