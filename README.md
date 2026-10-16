Clase de Backend con Django

1. La creación del Ambiente (environment) Virtual.

    El ambiente virtual te permite mantener aislado el desarrollo de cada proyecto y sus configuraciones
    para crear el ambiente virtual, 

    ejecutamos el siguiente comando en nuestro terminal para crearlo:
    
    python -m venv nombre_ambiente
    

2. Activación del Ambiente Virtual.
    
    El ambiente virtual debe permanecer activo durante todo el tiempo de desarrollo para mantener aislada la configuración y los cambios efectuados en el ambiente.

    - Si sale un error de permisos para ejecutar scripts hay que darle permisos especiales a nuestro terminal mediante la siguiente instrucción:
    
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    
    - Si funciono podemos volver a ejecutar el comando anterior.

    - Si trabajamos en varios proyectos y debemos cambiar de un ambiente a otro, desactivaremos el ambiente con el siguiente comando:
    
    deactivate
    

3. Creación del centro de Django
    - Para trabajar con Django hay que crear la estructura de directorios y la instalación de las dependencias principales.
    - Debemos ubicarnos en la carpeta raíz del proyecto y crearemos un nuevo proyecto Django con el siguiente comando:
    
    pip install django
    
    - Despues de que las dependencias de Django ya estan instaladas crearemos nuestro primer proyecto Django ejecutando el siguiente comando:
    
    django-admin startproject nombre_django .
    
    - nombre_django debe ser reemplazado por el nombre que le dará a su motor Django idealmente debe ser un nombre corto, porque deberemos ocuparlo en más de alguna oportunidad.

4. Creación de Aplicación
    - Cuando ya tenemos un motor Django funcional podemos crear nuestra aplicación particular que contendrá los controladores, las vistas y los modelos.
    - Para crear nuestra aplicación nos ubicamos mediante el terminal en la carpeta raíz del proyecto y ejecutamos el siguiente comando:
    
    django-admin startapp nombre_aplicacion
    
    - nombre_aplicacion debe ser cambiado por el nombre que le dará a su aplicación tiene que ser descriptivo para seguir normativas de buenas prácticas.
    - Una vez creada la aplicación hay que agregar el nombre de la aplicación a la lista de INSTALLED_APPS de setting.py de nuestro núcleo django.
    - Ya creada la aplicación iniciamos el servidor para confirmar que todo está funcionando bien.
    - El servidor se inicia con el siguiente comando mediante terminal:
    
    python manage.py runserver
    
    - Debiera cargar una vista genérica de Django al iniciar el servidor.