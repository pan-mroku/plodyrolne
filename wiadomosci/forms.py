from django import forms
from django_markdown.fields import MarkdownFormField
from django_markdown.widgets import MarkdownWidget


class WiadomoscForm(forms.Form):
    content = forms.CharField(widget=MarkdownWidget(), label="tresc")
    content2 = MarkdownFormField()