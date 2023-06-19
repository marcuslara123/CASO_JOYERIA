from .models import Region
from django.forms import ModelForm

class RegionForm(ModelForm):
    class Meta:
        model = Region
        fields = ["region",]
        labels = {"region":"Region",}

