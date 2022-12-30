
import datetime
from datetime import timedelta
from .models import Reserva

class PruebaMiddleware:
    
    def __init__(self,get_response):        
        self.get_response = get_response
    
    def __call__(self,request):
        response = self.get_response(request)
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        if request.user.is_authenticated:
            fecha_actual = datetime.date.today() #guardomas la fecha actual
            reservas = Reserva.objects.filter(estado = True,usuario = request.user) #optenemos todos los libros que tengo reservado el usuario actual
            for reserva in reservas:
                fecha_vencimiento = reserva.fecha_creacion + timedelta(days = 7) # a la  fecha actual le sumamos 7 dias que son los que programamos que duren las reservas  
                if fecha_actual > fecha_vencimiento:#si la fecha actual es mayor a la vecha vencimiento 
                    reserva.estado = False
                    reserva.save()