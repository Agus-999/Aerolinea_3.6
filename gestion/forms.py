from django import forms
from .models import Avion

class AvionForm(forms.ModelForm):
    class Meta:
        model = Avion
        fields = ['modelo', 'capacidad', 'filas', 'columnas']

from django import forms
from .models import Vuelo

class VueloForm(forms.ModelForm):
    class Meta:
        model = Vuelo
        # Removemos 'duracion' de los fields
        fields = ['avion', 'origen', 'destino', 'fecha_salida', 'fecha_llegada', 'estado', 'precio_base']
        widgets = {
            'fecha_salida': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_llegada': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        salida = cleaned_data.get('fecha_salida')
        llegada = cleaned_data.get('fecha_llegada')
        if salida and llegada and llegada < salida:
            raise forms.ValidationError("La fecha de llegada no puede ser anterior a la de salida.")
        return cleaned_data
