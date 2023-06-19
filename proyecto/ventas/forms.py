from .models import Articulo
from django.forms import ModelForm

class ArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        fields = ["nombre_articulo",]
        labels = {"nombre_articulo":"Artículo",}

