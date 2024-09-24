# Proyecto web con DRF para hacer web_scrapin de cuentas de instagram.

## 1. pip install django + la creacion del proyecto, superuser y la app instagram_feed
* Luego de la creación del entorno virtual, creo mi proyecto django web_scraping.
* Creo un superuser para mi django-admin.
* Creo mi app instagram_feed y la agrego y la agrego al proyecto en settings.py

## 2. Comienzo a trabajar en mis modelos
* usuario de instagram
* foto de perfil
* last_update: de los datos de la cuenta(nuevo post, nueva foto de perfil.)
* Los Post que suba la cuenta añadida.
* Se instalan las librerias Pillow para procesamiento de imagenes y python-magic que ayuda a 
identificar tipo de archivo sin depender de la extensión.

### Decido finalme usar ImageField en vez de URLField a ImageField como solución a problemas CORS: 
* Los modelos  almacenan las imágenes de Instagram de forma local en el servidor, en lugar de 
* utilizar solo la URL. Esto resuelve los problemas causados por las restricciones de CORS de Instagram, 
que impedían cargar las imágenes correctamente.

### Realizo las migraciones necesarias.
* python manage.py makemigrations : Crea un registro de los cambios realizados en los modelos.
* python manage.py migrate  : Aplica esos cambios a la base de datos.


### Creo la carpeta media y en settings.py las configuraciones. 
* MEDIA_URL define la parte de la URL que se mostrará en el navegador. 
* MEDIA_ROOT indica la ubicación real del archivo en el servidor.


## 3. Configuro mi admin.py y lo personalizo
- Desde el panel de django será posible agregar cuentas de instagram. 
- De cada cuenta veo su username, last_update y la foto de perfil. + los post de la cuenta.
- De cada post tengo foto/ videos y descripción del post.

## 4. Comienzo a trabajar en la lógica que me permita interactuar con la api de instagram. 
- Creo mi archivo utils.py el cual se encargará de acceder a la api de instagram usando la libreria instaloader y sus diferentes métodos.
- pip install instaloader 

### Hasta aqui se puede considerar que el back esta medianamente hecho pero esto tiene que conectar con un front
## 5. pip install djangorestframework  
* Django-rest-framework me proporcionará una capa de abstracción sobre las vistas y los serializadores 
de Django, simplificando la creación de endpoints para realizar 
operaciones CRUD (Crear, Leer, Actualizar, Eliminar)sobre mis modelos de datos y gracias a serializers 
convertirá los objetos de mis modelo en formatos de datos fácilmente transportables, 
como JSON o XML, para que puedan ser consumidos (mi front).
## 6. Creo el archivo serializers.py 
* En serializers.py defino cómo se traducirán los datos de mis 
modelos a un formato adecuado para la comunicación a través de la API.

## 7. Creo mi views.py 
* En el que defino un endpoint para obtener una lista de todas las cuentas de  
Instagram en la base de datos. Al hacer una solicitud GET a este endpoint 
obtengo una lista de todas las cuentas de Instagram, sus post, etc en formato JSON.

## 8. Creo instagram_feed/urls.py
* En este archivo defino los patrones de URL para mi aplicación instagram_feed. 
Estos patrones mapean URLs específicas a funciones de vista que manejan las 
solicitudes entrantes. En este caso defino un patrón que se activa cuando 
la URL entrante contiene get_posts/. Cuando se activa este patrón, 
Django ejecuta la función account_list definida en views.py.
* Actualizo el archivo urls.py ubicado en la raíz de mi proyecto Django 
incorporando la URL definidas en instagram_feed/urls.py.



