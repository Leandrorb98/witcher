from django import forms
from ejemplo.models import Persona
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre','apellido', 'fecha_de_nacimiento']
