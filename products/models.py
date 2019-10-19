from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    date = models.DateTimeField()
    votes_total = models.IntegerField(default = 1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='icons/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] + '...Click to read more'

    def new_date(self):
        return self.date.strftime('%b %e, %Y')