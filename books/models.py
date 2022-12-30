from datetime import timedelta
import uuid
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save,pre_save
from django.db import models
from django.urls import reverse

class Categoria(models.Model):
    slug = models.SlugField(max_length=50)
    nombre = models.CharField('Nombre de la Categoría',max_length = 100, null = False,blank = False)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'



    def __str__(self):
        return self.nombre

class Book(models.Model):
    id = models.UUIDField(primary_key=True,db_index=True,default=uuid.uuid4,editable=False) #para que las url tengan un UUID en vez de un id icremental y sea mas seguro
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    cover = models.ImageField(upload_to="covers/", blank=True) #blank esque podemos dejar el campo vacio al llenar el farmulirio
    descripcion = models.TextField('Descripción',null = True,blank = True)
    cantidad = models.PositiveIntegerField('Cantidad o Stock',default = 1)
    fecha_publicacion = models.DateField('Fecha de publicación', blank = False, null = False)


    #este es para agregar un permiso al administrador 
    class Meta: 
        indexes = [ models.Index(fields=["id"], name="id_index"),]
        permissions = [("special_status", "Can read all books"),]

    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self): 
        return reverse("book_detail", args=[str(self.id)])

    @property
    def get_view_count(self):
        return self.bookview_set.select_related().all().count()    

    @property
    def get_like_count(self):
        return self.likes_set.select_related().all().count()
       

class Review(models.Model): 
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name="reviews",)
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,)

    def __str__(self):
        return self.review
        


class Reserva(models.Model):
    id = models.AutoField(primary_key = True)
    libro = models.ForeignKey(Book, on_delete=models.CASCADE)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cantidad_dias = models.SmallIntegerField('Cantidad de Dias a Reservar',default = 7) #7 dies es lo maximo que va a poder reservar el libro para usarlo
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
    fecha_vencimiento = models.DateField('Fecha de vencimiento de la reserva', auto_now=False, auto_now_add=False, null = True, blank = True)
    estado = models.BooleanField(default = True, verbose_name = 'Estado')

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f'Reserva de Libro {self.libro} por {self.usuario}'


class likes(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='usuariolikes')
    book = models.ForeignKey(Book,on_delete=models.CASCADE)


class bookview(models.Model):
    usuariovistas = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='usuarioviews')
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.usuariovistas

#------------------------------------------------------signals -------------------------------------------------------------------------

def reducir_cantidad_libro(sender,instance,**kwargs):
    
    libro = instance.libro
    if libro.cantidad > 0 and instance.fecha_vencimiento is None or instance.fecha_vencimiento == '':
        libro.cantidad = libro.cantidad - 1
        libro.save()
        instance.fecha_vencimiento = instance.fecha_creacion + timedelta(days = instance.cantidad_dias)
        instance.save()
        print("hola soy un signal ")
        





post_save.connect(reducir_cantidad_libro,sender = Reserva)
