from django import forms
from drillbox.models import Tool


class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['name']

