import datetime
from allauth.account.forms import SignupForm
from django import forms
from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError
from .models import Review,Reserva

class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':('Nombre Completo')}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':('Apellido')}))


    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class  formcomentarios(forms.ModelForm):
    review = forms.CharField(widget=forms.TextInput(attrs={'class':'crearcamentario','placeholder':'Agrege un comentario..'}),required=True)
    class   Meta:
        model = Review
        fields = ('review',)     


class ReservaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Reserva
        fields = '__all__'
    
    def clean_libro(self):
        libro = self.cleaned_data['libro']
        if libro.cantidad < 1:
            raise ValidationError('No se puede reservar este libro, deben existir unidades disponibles.')
        return libro

    def clean_fecha_vencimiento(self):
        hola = self.cleaned_data['fecha_vencimiento']
        if hola == datetime.date.today():
            raise ValidationError('No puede poner la fecha de hoy')
        # if hola < datetime.date.today():
        #     raise ValidationError('No puede poner una fecha anterior a hoy')
  
        return hola