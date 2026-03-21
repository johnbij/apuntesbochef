import streamlit as st
from utils import render_multiple_choice_quiz

# ---------------------------------------------------------------------------
# Base de ejercicios categorizados
# ---------------------------------------------------------------------------

EJERCICIOS = {
    "🐍 Fundamentos": {
        "descripcion": "Variables, tipos de datos y operadores básicos en Python.",
        "teoria": """
### Variables y tipos de datos

En Python no es necesario declarar el tipo de una variable explícitamente.

```python
nombre = "Ingeniería"   # str
semestre = 3            # int
promedio = 5.7          # float
aprobado = True         # bool
```

### Operadores aritméticos

| Operador | Descripción       | Ejemplo   |
|----------|-------------------|-----------|
| `+`      | Suma              | `3 + 2`   |
| `-`      | Resta             | `10 - 4`  |
| `*`      | Multiplicación    | `6 * 7`   |
| `/`      | División real     | `7 / 2`   |
| `//`     | División entera   | `7 // 2`  |
| `%`      | Módulo (resto)    | `7 % 2`   |
| `**`     | Potencia          | `2 ** 8`  |
""",
        "quiz": [
            {
                "question": "¿Cuál es el resultado de `7 // 2` en Python?",
                "options": {"A": "3.5", "B": "3", "C": "4", "D": "2"},
                "answer": "B",
                "explanation": "El operador `//` realiza división entera, descartando la parte decimal.",
            },
            {
                "question": "¿Qué tipo retorna `type(3.14)` en Python?",
                "options": {"A": "int", "B": "str", "C": "float", "D": "double"},
                "answer": "C",
                "explanation": "Los literales con punto decimal son de tipo `float` en Python.",
            },
        ],
    },
    "🔁 Control de Flujo": {
        "descripcion": "Condicionales, bucles y comprensión de listas.",
        "teoria": """
### Condicionales

```python
nota = 5.0
if nota >= 4.0:
    print("Aprobado")
elif nota >= 3.0:
    print("Reprobado por poco")
else:
    print("Reprobado")
```

### Bucles

```python
# for con range
for i in range(5):
    print(i)          # 0 1 2 3 4

# while
contador = 0
while contador < 5:
    contador += 1
```

### Comprensión de listas

```python
cuadrados = [x**2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]
```
""",
        "quiz": [
            {
                "question": "¿Cuántas veces itera `for i in range(3, 9, 2):`?",
                "options": {"A": "2", "B": "3", "C": "6", "D": "4"},
                "answer": "B",
                "explanation": "`range(3, 9, 2)` genera los valores 3, 5, 7 → 3 iteraciones.",
            },
            {
                "question": "¿Qué produce `[x for x in range(4) if x % 2 == 0]`?",
                "options": {"A": "[0, 2]", "B": "[1, 3]", "C": "[0, 1, 2, 3]", "D": "[2, 4]"},
                "answer": "A",
                "explanation": "Filtra los valores pares de 0 a 3: 0 y 2.",
            },
        ],
    },
    "📦 Funciones": {
        "descripcion": "Definición, parámetros, valores por defecto y lambdas.",
        "teoria": """
### Definición de funciones

```python
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}!"

print(saludar("Bochef"))          # Hola, Bochef!
print(saludar("Bochef", "Hey"))   # Hey, Bochef!
```

### Funciones lambda

```python
cuadrado = lambda x: x ** 2
print(cuadrado(5))   # 25
```

### `*args` y `**kwargs`

```python
def suma(*args):
    return sum(args)

print(suma(1, 2, 3, 4))   # 10
```
""",
        "quiz": [
            {
                "question": "¿Qué imprime `(lambda x, y: x + y)(3, 4)`?",
                "options": {"A": "34", "B": "7", "C": "Error", "D": "None"},
                "answer": "B",
                "explanation": "La lambda suma sus dos argumentos: 3 + 4 = 7.",
            },
            {
                "question": "¿Cuál es el resultado de `suma(2, 3)` si `def suma(a, b=10): return a + b`?",
                "options": {"A": "10", "B": "5", "C": "12", "D": "2"},
                "answer": "B",
                "explanation": "Se pasan los dos argumentos (2 y 3), así que b=3, no el valor por defecto. 2+3=5.",
            },
        ],
    },
    "📚 Estructuras de Datos": {
        "descripcion": "Listas, tuplas, diccionarios y conjuntos.",
        "teoria": """
### Listas

```python
notas = [5.0, 6.5, 4.7, 5.5]
notas.append(6.0)
notas.sort()
print(notas[-1])   # último elemento
```

### Diccionarios

```python
alumno = {"nombre": "Ana", "ramo": "Cálculo", "nota": 6.2}
print(alumno["nombre"])          # Ana
alumno["nota"] = 6.5             # actualizar
```

### Tuplas y conjuntos

```python
coordenadas = (3, 4)             # inmutable
colores = {"rojo", "verde", "azul"}  # sin duplicados
```
""",
        "quiz": [
            {
                "question": "¿Qué método elimina y retorna el último elemento de una lista?",
                "options": {"A": "remove()", "B": "delete()", "C": "pop()", "D": "discard()"},
                "answer": "C",
                "explanation": "`list.pop()` sin argumentos elimina y retorna el último elemento.",
            },
            {
                "question": "¿Cuál estructura NO admite elementos duplicados?",
                "options": {"A": "Lista", "B": "Tupla", "C": "Diccionario (valores)", "D": "Set"},
                "answer": "D",
                "explanation": "Los conjuntos (`set`) garantizan elementos únicos.",
            },
        ],
    },
}


def render_ejercicios_python():
    """Renderiza la base de ejercicios Python categorizados."""
    st.markdown("## 🐍 Ejercicios de Python")
    st.caption("Repasa teoría y pon a prueba tus conocimientos con quizzes interactivos.")

    categorias = list(EJERCICIOS.keys())
    categoria = st.selectbox("Selecciona una categoría:", categorias, key="ej_categoria")

    if categoria:
        datos = EJERCICIOS[categoria]
        st.markdown(f"**{datos['descripcion']}**")

        tab_teoria, tab_quiz = st.tabs(["📖 Teoría", "❓ Quiz"])

        with tab_teoria:
            st.markdown(datos["teoria"])

        with tab_quiz:
            st.markdown("### Pon a prueba tus conocimientos")
            render_multiple_choice_quiz(datos["quiz"], key_prefix=f"ej_{categoria}")
