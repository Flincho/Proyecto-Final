# Proyecto desarrollado por Alex Ernst

- Notas
```bash
Si no me olvidé de nada, creeria que todo lo que se muestra en la web tiene una función

En la parte de "sales" todavía faltan programar algunas funciones, como que te 
calcule el precio final y reste del stock, pero por falta de tiempo no lo pude hacer

Otra funcinalidad que podria agregar es que al seleccionar el "client" o "product" 
herede para la sección de details algunos de los datos de estos y no solo el nombre.
```

## Instrucciones para ejecutar este proyecto

- Clonar el proyecto
```bash
git clone https://github.com/Flincho/Proyecto-Final.git

cd Project
```

- Instalar Django
```bash
pip install Django
```

- Crear base de datos con los Modelos (hacer migraciones y migrar)
```bash
python manage.py makemigrations main

python manage.py migrate
```

- Crear super-usuario
```bash
python manage.py createsuperuser
```

- Ejecutar proyecto
```bash
python manage.py runserver
```
