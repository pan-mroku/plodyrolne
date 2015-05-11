from django import forms
from django_markdown.fields import MarkdownFormField
from django_markdown.widgets import MarkdownWidget


class WiadomoscForm(forms.Form):
    subject = forms.CharField(label="Temat")
    content = forms.CharField(widget=MarkdownWidget(), label="Tresc wiadomosci")