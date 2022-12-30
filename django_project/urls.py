from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404

from pages.views import error404


urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),#para el rendimiento de nuestra aplicacion
    path('hola/', admin.site.urls),
    #para todo lo que tenga que ver con registro inicio de secion y mas cosas  como restaurar contrasenas etc 
    #path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("allauth.urls")), #ahora usamos este para django allauth
    #aplicaciones
    path("accounts/", include("accounts.urls")), 
    path("", include("pages.urls")),
    path("books/", include("books.urls")),
]+ static( #para pillow
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

handler404 =error404.as_view()
