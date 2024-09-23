Proyecto web con django para hacer web scrapin de cuentas de insta.

# 1. pip install django + la creacion del proyecto, superuser y la app instagram_feed
- TIME_ZONE = 'Europe/Madrid'

# 2. Comienzo a trabajar en mis modelos
* usuario de instagram
* foto de perfil
* last_update: de los datos de la cuenta(nuevo post, nueva foto de perfil.)
* Los Post que suba la cuenta añadida.

### Decido finalme usar ImageField en vez de URLField a ImageField como solucion problemas CORS: 
 * Se ha modificado el modelo para almacenar las imágenes de Instagram de forma local en el servidor, 
en lugar de utilizar solo la URL. Esto resuelve los problemas causados por las restricciones de CORS de Instagram, 
que impedían cargar las imágenes correctamente.
### Creo la carpeta media y en settings.py
* MEDIA_URL define la parte de la URL que se mostrará en el navegador. 
* MEDIA_ROOT indica la ubicación real del archivo en el servidor.

# 3. Configuro mi admin.py y lo personalizo
# 4. pip instaloader para trabajar en las descargas.



