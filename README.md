# Figuras basicas

usando python para realizar figuras

- lineas
  - horizontal
  - vertical

en progreso ...

## Como Graficar

Primero importamos el modulo `draw` y a la funcion requerida le asignas un entero este argumento sera la longitud de caracteres que tendra

```python
from draw import Draw # importamos el modulo

draw = Draw() # instanciamos el objeto
```

Usando `print` para graficar:

### linea horizontal

```python
out = draw.line.horizontal(8)
print(out)
```

produce el siguiente resultado:

```cmd
********
```

### linea vertical

```python
print(draw.line.vertical(8))
```

produce el siguiente resultado:

```cmd
*
*
*
*
*
*
*
*

```
