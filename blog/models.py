from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
