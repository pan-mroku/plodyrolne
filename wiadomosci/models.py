from django.contrib.auth.models import User
from django.db import models
from django_markdown.models import MarkdownField
from django_markdown.fields import MarkdownFormField
from django_markdown.widgets import MarkdownWidget


class Wiadomosc(models.Model):
    nadawca = models.OneToOneField(User, related_name='nadawca')
    adresat = models.OneToOneField(User, related_name='adresat')
    temat = models.TextField()
    tresc = MarkdownField()
    data = models.DateTimeField(auto_now=True)
