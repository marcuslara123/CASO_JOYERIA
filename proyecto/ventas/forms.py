from .models import Articulo
from django.forms import ModelForm

class ArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        fields = ["articulo",]
        labels = {"articulo":"Artículo",}

