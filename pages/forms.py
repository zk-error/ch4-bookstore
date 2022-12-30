from django import forms
from django.core.exceptions import ValidationError
from  books.models import Book

class LibroForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ('categoria','title','author','cover','descripcion','cantidad','fecha_publicacion')
      
        labels = {
            'title':'',
            'author': '',
            'cover':'',
            'descripcion':'',
            'fecha_publicacion': 'Fecha de Publciación del Libro'
        }

        widgets = {

              'categoria': forms.Select(
                attrs = {
                    'class': 'form-control2',

                }
            ),
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese título de libro'
                }
            ),
            'author': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese el nombre del autor'
                }
            ),
            'fecha_publicacion': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control3'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class':'descripcion',
                    'placeholder': 'Ingrese una pequeña descripcion del libro'
                }
            ),
            'cantidad': forms.NumberInput(
                attrs = {
                    'class':'form-control2',
                }
            )
        }

        
