from django.forms import ModelForm
from .models import OilChange

class OilChangeForm(ModelForm):
    class Meta:
        model = OilChange
        fields = ('date', 'change')
        