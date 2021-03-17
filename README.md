# Formpy
Librería para crear formularios en HTML desde Python.

## Preferencias

Python >= 3

## Instalación 🛠

### Con pip

```
pip install Formpy
```

## Importación 📦

Importa el archivo en tu codigo de Python.

```python
from formpy import Form
```

## Empezando 🚀

### Crear carpeta forms (Obligatoria antes de empezar)


### Instanciar nuevo formulario

#### Form()

#### Parametros

La clase Form puede recibir distintos parametros, pero solamente el parametro **formName** es obligatorio para intanciar un nuevo formulario.

formName

- String
- Estable el formulario/archivo .html

formId

- String
- Estable el atributo id del formulario

onlyForm

- Boolean
- Si el parametro es True unicamente mostrara el archivo con etiqueta <form>
- Si es parametro es False mostrara las etiquetas comunes de un archivo HTML junto con la etiqueta <form>

styleLink

- String
- Estable el link stylesheet (css) que tendra el archivo

action

- String
- Estable el atributo action del formulario

method

- String
- Estable el atributo method del formulario



```python
from formpy import Form

fUsers = Form("Users")


```
