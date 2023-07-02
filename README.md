![Texto alternativo](https://github.com/zk-error/ch4-bookstore/blob/master/ejemplo.png)
# Biblioteca en línea

La Biblioteca en línea es una plataforma que permite a los usuarios reservar libros de una biblioteca pública. Está diseñada para ser utilizada por una universidad u otra institución educativa. Los usuarios pueden acceder a la biblioteca en línea, buscar libros, realizar reservas, dejar comentarios y utilizar otras funciones interactivas.

## Características principales

- Registro de usuarios: Los usuarios pueden registrarse en la plataforma de manera convencional o utilizando su cuenta de Google.
- Búsqueda de libros: Los usuarios pueden buscar libros por título, autor, género u otros criterios.
- Reserva de libros: Los usuarios pueden reservar libros disponibles en la biblioteca.
- Comentarios y calificaciones: Los usuarios pueden dejar comentarios y calificaciones en los libros que han leído.
- Favoritos: Los usuarios pueden guardar libros en su lista de favoritos para acceder rápidamente a ellos más tarde.
- Interacción social: Los usuarios pueden dar "me gusta" a los comentarios de otros usuarios y seguir a otros usuarios.



## Instalación y configuración del proyecto Biblioteca

Sigue estos pasos para configurar el proyecto Biblioteca en tu entorno local:

1. Clona el repositorio del proyecto:

2. Accede a la carpeta del proyecto:

3. Ejecuta el siguiente comando para iniciar los contenedores de Docker:

   ```shell
   docker-compose up -d
   ```

   Esto creará y ejecutará los contenedores de Docker necesarios para el proyecto.

4. Una vez que los contenedores estén en ejecución, ejecuta las migraciones de la base de datos:

   ```shell
   docker-compose exec web python manage.py migrate
   ```

   Esto aplicará las migraciones y creará las tablas necesarias en la base de datos.

5. Crea una cuenta de administrador utilizando el siguiente comando:

   ```shell
   docker-compose exec web python manage.py createsuperuser
   ```

   Sigue las instrucciones en la consola para ingresar un nombre de usuario, dirección de correo electrónico y contraseña para el administrador.

¡Listo! Ahora has configurado el proyecto Biblioteca en tu entorno local. Puedes acceder a él en tu navegador y comenzar a utilizarlo.
Abre tu navegador web e ingresa la siguiente URL: http://127.0.0.1:8000/

Esto te llevará a la página principal del proyecto Biblioteca, donde podrás explorar las funcionalidades y utilizar las diferentes características del sistema.
