# Importar la conexion a la base de datos
import config.db as db

# Importar streamlit
import streamlit as st

# Crear la funcion para insertar juguetes a la base de datos con pymongo
def insertToy(name, edad_recomendada, descripcion, imagen, precio, stock, marca, categoria):
    # Crear el diccionario con los datos del juguete
    toy = {
        "nombre": name,
        "edad_recomendada": edad_recomendada,
        "descripcion": descripcion,
        "imagen": imagen,
        "precio": precio,
        "stock": stock,
        "marca": marca,
        "categoria": categoria
    }

    # Insertar el juguete en la base de datos
    db.db["juguetes"].insert_one(toy)

    # Mostrar mensaje de exito
    st.success('El juguete se ha agregado con exito')

# Crear una funcion para insertar juguetes
def InterfaceInsert():
    # Titulo
    st.title('Agregar juguetes')

    # Crear un input para nombre y edad recomendada del juguete en una misma linea
    name, edad_recomendada = st.columns(2)
    name = name.text_input('Nombre', key='input_name', type='default')
    edad_recomendada = edad_recomendada.text_input('Edad recomendada', key='input_edad_recomendada', type='default')

    # Crear un input para la descripcion y la imagen del juguete
    descripcion = st.text_area('Descripcion', key='input_descripcion')
    imagen = st.text_input('Imagen', key='input_imagen', type='default')

    # Crear un input para el precio, stock y marca del juguete en una misma linea
    precio, stock, marca = st.columns(3)
    precio = precio.text_input('Precio', key='input_precio', type='default')
    stock = stock.text_input('Stock', key='input_stock', type='default')
    marca = marca.text_input('Marca', key='input_marca', type='default')

    # Crear un select para la categoria
    categoria = st.selectbox('Categoria', ['Niñas', 'Niños', 'Didacticos'])

    # Crear un boton para agregar el juguete
    button = st.button('Agregar')

    # Si el boton es presionado
    if button:
        # Texto
        st.text('Agregando juguete...')
        # Texto
        st.success(f'Juguete agregado: {name}')

        # Insertar el juguete en la base de datos
        insertToy(name, edad_recomendada, descripcion, imagen, precio, stock, marca, categoria)
        