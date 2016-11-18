from django import forms
from blib.models import Libro

class PostForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('li_ISBN', 'li_Titulo', 'li_Autor', 'li_Editorial', 'li_Pais', 'li_anio')
