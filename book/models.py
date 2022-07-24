from django.db import models


class Books(models.Model):
    ISBN = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Opinions(models.Model):
    ISBN = models.ForeignKey(
        'Books',
        on_delete=models.CASCADE,
    )
    rating = models.IntegerField()
    description = models.TextField(max_length=100)

    @property
    def star_finder(self):
        stars = ''
        for star in range(self.rating):
            stars = stars + '*'
        return stars

    @property
    def from_book(self):
        from_book_is = Books.objects.select_related().filter(
            id=self.ISBN_id).values('title')
        return from_book_is[0]['title']

    def __str__(self):
        return self.description
