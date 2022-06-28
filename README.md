# Proyecto desarrollado por Alex Ernst

- Notas
```bash
Desarrollado en su totalidad en solotario, dado que el compañero asignado desapareció.

El proyecto integra conceptos de un blog web y gestión de empresas, porque siento que me ayudó a explorar 
más en profundidad el funcinamiento en conjuento de Python y Django, aunque no llegue a coumplir los 
requerimientos de ninguno.

Soy conciente que faltan algunas de las funcionalidades requeridas, pero en este mes estuve con prubas 
de mitad de año del secundarío y estudiando para el examen de ingreso de la universidad, que claramente 
estubieron por encima en la escala de prioridades.

Igualmente, espero que sea de su agrado, y le agradezco por loda la dedicacón dada a este curso.

Saludos

Alex Ernst
```

- Archivos
```bash
UnitTest: https://docs.google.com/spreadsheets/d/1LADicdu5gtL5OIwXufLD0z7LoJVfVzmlTvI8qxx1-ew/edit?usp=sharing

Video demostración: https://drive.google.com/file/d/17AHpt4SUkeS6rC1u7-0ZCnqBw35AO5w7/view?usp=sharing
Si tenes problemas con el video, está también subido al repositorio 
```

## Instrucciones para ejecutar el proyecto

- Clonar el proyecto desde GitHub
```bash
git clone https://github.com/Flincho/Proyecto-Final.git

cd Project
```

- Instalar software necesario para la ejecución
```bash
pip install Django
pip install Pillow
pip install django-calculation
```

- Crear base de datos con los Modelos
```bash
python manage.py makemigrations 

python manage.py migrate
```

- Ejecutar proyecto
```bash
python manage.py runserver
```
