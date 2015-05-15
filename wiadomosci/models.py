from django.contrib.auth.models import User
from django.db import models
from django_markdown.models import MarkdownField
from django_markdown.fields import MarkdownFormField
from django_markdown.widgets import MarkdownWidget


class Wiadomosc(models.Model):
    temat = models.TextField(default="")
    tresc = MarkdownField()
    data = models.DateTimeField(auto_now=True)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.data)+": "+self.temat