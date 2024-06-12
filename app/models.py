from django.db import models


class Logo(models.Model):
    title = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.title


class ConferenceSection(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    logo = models.ImageField(upload_to='conference_logos/')

    def __str__(self):
        return self.title
