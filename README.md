# Formpy
Librería para crear formularios en HTML desde Python.

## Preferencias

Python >= 3

Conocimientos basicos acerca HTML

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

Clase Form

#### Parametros

La clase Form puede recibir distintos parametros, pero solamente el parametro **formName** es obligatorio para intanciar un nuevo formulario.

formName

- String
- Estable el nombre del formulario/archivo .html

formId

- String
- Estable el atributo id del formulario

onlyForm

- Boolean
- Si el parametro es True unicamente mostrara el archivo con la etiqueta form
- Si es parametro es False mostrara las etiquetas comunes de un archivo HTML Y la etiqueta form

styleLink

- String
- Estable el link stylesheet (css) que tendra el archivo

action

- String
- Estable el atributo action del formulario

method

- String
- Estable el atributo method del formulario


#### Usos

Primer uso

```python
from formpy import Form

fUsers = Form("Users")


```

Otro uso

```python
from formpy import Form

fUsers = Form("Users", formId= "frmusers", styleLink="../estilos.css")


```

### Metodos directos de Form

setId()

- String
- Estable el atributo id del formulario
- Se puede usar despues de instanciar el Form (con o sin el parametro formId)

```python
from formpy import Form

fUsers = Form("Users")

fUsers.setId("frmusers")


```

setStyleLink()

- List
- Estable mas de un link stylesheet al archivo .html


```python
from formpy import Form

fUsers = Form("Users")

styles = [
    "../estilos.css",
    "../mas-estilos.css"
]

fUsers.setStyleLink(styles)


```

setAction()

- String
- Estable el atributo action del formulario
- Se puede usar despues de instanciar el Form (con o sin el parametro formAction)


```python
from formpy import Form

fUsers = Form("Users")

fUsers.setAction("../mi-form.php")


```

setMethod()

- String
- Estable el atributo method del formulario
- Se puede usar despues de instanciar el Form (con o sin el parametro formMethod)


```python
from formpy import Form

fUsers = Form("Users")

fUsers.setMethod("GET")


```

### Estructurando el formulario

#### Metodos

input()

input() recibe tres parametros opcionales:

dict

- Dict
- Establece los atributos que tendra la etiqueta input

p

- String
- Encierra a la etiqueta input dentro de una etiqueta p con un texto a su derecha

text

- String
- Coloca un texto a la derecha fuera de la etiqueta input

#### Usos

```python
from formpy import Form

fUsers = Form("Users", onlyForm=True)

at = {"type":"number", "name":"nombre"}

fUsers.input(at, p="Ingresa tu edad:", text="(+18)").toHTML()


```

Users.html

```html
  
 <form action='' method='' id=''>
            
    <p> Ingresa tu edad: <input type='number' name='nombre' > (+18) </p>


</form>
            

```






