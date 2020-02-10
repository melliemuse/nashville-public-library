from django.db import models
from .library import Library
from .librarian import Librarian

# Pascal case FirstLetterUpperAndOthers- indicates that this is a class. Below we are making instances of classes.

class Book(models.Model):
    title = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year_published = models.IntegerField()
    location = models.ForeignKey(Library, on_delete=models.CASCADE)
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)