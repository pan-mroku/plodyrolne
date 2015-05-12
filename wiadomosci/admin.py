from django.contrib import admin
from wiadomosci.models import Wiadomosc
from django_markdown.admin import MarkdownModelAdmin

admin.site.register(Wiadomosc, MarkdownModelAdmin)