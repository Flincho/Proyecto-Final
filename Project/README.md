# Proyecto desarrollado por Alex Ernst

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
python manage.py makemigrations app_1

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
