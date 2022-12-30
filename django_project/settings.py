import environ
import os
from pathlib import Path


#cosas para env
env = environ.Env()


BASE_DIR = Path(__file__).resolve().parent.parent

#default=False

SECRET_KEY = env("SECRET_KEY")
#debug
#cuando debug es true si ponemos una ruta mal nos mostrara un hoja de rutas esto es malo ya que es como un mapa para un hacker
#DEBUG = env("DJANGO_DEBUG")
DEBUG = True
#para personalizar las paginas de error
ALLOWED_HOSTS = [".herokuapp.com", "localhost", "127.0.0.1"]



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',  #para el registro y login de usuarios esta viene por defecto
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.sites", # para django allauth

    #apps de apps externas
    "allauth", # para django allauth
    "allauth.account", # para django allauth
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    "debug_toolbar", # para medir el rendimiento
    #apps
    "accounts.apps.AccountsConfig",
    "pages.apps.PagesConfig",
    "books.apps.BooksConfig", 
]

MIDDLEWARE = [
    'books.middleware.PruebaMiddleware', #difinemios que en esta runta tendremos un middleware personalizado
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware", # para medir el rendimiento
]

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"], #para los archivos estaticos 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_project.wsgi.application'




DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",
        "PORT": 5432,
    }
}




AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]




LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_TZ = True



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#para archivos estaticos----------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"] 

#modela personalizado-----
AUTH_USER_MODEL = "accounts.CustomUser" 

#para rediriguir al usuario despues de iniciar secion y cerrarla---------------
LOGIN_REDIRECT_URL = "home"
#LOGOUT_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT = "home"  # este se usa en allauht ya que  tiene configuracion para cerrar cesion

# django-allauth configuracion ------------------------------
SITE_ID = 1 
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend", #esto es para poder poder cambiar la configuracion ejem iniciar secion con correo
)
ACCOUNT_SESSION_REMEMBER = True #para que no muestre el cuadro de recordar contrasena
#ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False # esta opcion es por si no queremos que cuando se registren confirmen la contrasena
ACCOUNT_USERNAME_REQUIRED = False #para que el nombre de usuario sea opcional
ACCOUNT_AUTHENTICATION_METHOD = "email" #para que se inicie secion con el email
ACCOUNT_EMAIL_REQUIRED = True #para hacer al email requererido
ACCOUNT_UNIQUE_EMAIL = True #para que todos los email sean unicos
ACCOUNT_EMAIL_VERIFICATION = "mandatory" #este es para no pueda entrar a su cuenta hasta que verifique su correo
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1 #este es para ver en cuanto tiempo expira la verificacion por defecto viene 3 dias
ACCOUNT_LOGOUT_ON_GET= True #este para cuando cerremos secion no nos pregunte si estamos seguros


#para combiar el correo electronico de los gmail que nos llega para comfirmar nuestra cuenta
DEFAULT_FROM_EMAIL = "lolapaluza@gmail.com"

#para modificar el formulario de singup de allauth

ACCOUNT_FORMS = {
'signup': 'books.forms.MyCustomSignupForm',
}


#correos en consola-------------------
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" #para recibir correos en la consola

#pillow -----------------------------------------------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media" 

# django-debug-toolbar
if DEBUG:
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

# #parte HTTPS/SSL seguridad
# SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)

# #parte de HTTP Strict Transport Security (HSTS)
# SECURE_HSTS_SECONDS = env.int("DJANGO_SECURE_HSTS_SECONDS", default=2592000) # 30 days
# SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS",default=True)
# SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
# #parte de Secure Cookies
# SESSION_COOKIE_SECURE = env.bool("DJANGO_SESSION_COOKIE_SECURE", default=True)
# CSRF_COOKIE_SECURE = env.bool("DJANGO_CSRF_COOKIE_SECURE", default=True)
