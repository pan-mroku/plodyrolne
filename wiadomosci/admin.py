from django.contrib import admin
from wiadomosci.forms import WiadomoscForm
from wiadomosci.models import Wiadomosc
from django_markdown.admin import MarkdownModelAdmin


class WiadomoscModelAdmin(admin.ModelAdmin):
    form = WiadomoscForm

admin.site.register(Wiadomosc, WiadomoscModelAdmin)