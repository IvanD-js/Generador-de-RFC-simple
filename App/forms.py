from django import forms

class RFCForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido_paterno = forms.CharField(label="Apellido Paterno", max_length=100)
    apellido_materno = forms.CharField(label="Apellido Materno", max_length=100, required=False)
    fecha_nacimiento = forms.DateField(
        label="Fecha de nacimiento",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
