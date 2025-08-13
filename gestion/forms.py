from django import forms
from .models import Avion, Pasajero

class AvionForm(forms.ModelForm):
    class Meta:
        model = Avion
        fields = ['modelo', 'capacidad', 'filas', 'columnas', 'imagen']
        widgets = {
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

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


from django import forms
from .models import Vuelo

class ReservaForm(forms.Form):
    vuelo = forms.ModelChoiceField(
        queryset=Vuelo.objects.all(),
        required=True,
        label="Vuelo"
    )

    nombre = forms.CharField(
        max_length=100,
        label="Nombre",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Ingresa tu nombre', 'class': 'form-control'})
    )
    documento = forms.CharField(
        max_length=50,
        label="Documento",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Ej: 45302185', 'class': 'form-control'})
    )
    email = forms.EmailField(
        required=True,  # Poner true si querés que sea obligatorio
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'Ej: ejemplo@correo.com', 'class': 'form-control'})
    )
    telefono = forms.CharField(
        max_length=20,
        required=True,  # Poner true si es obligatorio
        label="Teléfono",
        widget=forms.TextInput(attrs={'placeholder': 'Ej: 54935531261', 'class': 'form-control'})
    )
    fecha_nacimiento = forms.DateField(
        required=True,  # Poner true si obligatorio
        label="Fecha de nacimiento",
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    tipo_documento = forms.ChoiceField(
        choices=[('dni', 'DNI'), ('pasaporte', 'Pasaporte'), ('otro', 'Otro')],
        required=True,  # Poner true si obligatorio
        label="Tipo de documento",
        widget=forms.Select(attrs={'class': 'form-select'})
    )


class PasajeroForm(forms.ModelForm):
    class Meta:
        model = Pasajero
        fields = ['nombre', 'documento', 'email', 'telefono', 'fecha_nacimiento', 'tipo_documento']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }