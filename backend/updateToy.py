import config.db as db
import streamlit as st
import pandas as pd

# Crear una funcion para editar los datos de un juguete


def InterfaceEdit():
    # Titulo
    st.title('Editar juguetes')

    # Crear un input para buscar el juguete
    search_term = st.text_input(
        'Buscar juguete por nombre:', key='search_term')
    button = st.button('Actualizar datos')

    if button:
        # Si se ha ingresado un termino de busqueda
        if search_term:
            # Buscar el juguete en la base de datos por su nombre
            result = db.db["juguetes"].find_one({'nombre': search_term})

            toy = pd.DataFrame([result]).stack().reset_index()

            st.write(toy)

            # Si se encontró el juguete
            if result:

                # Mostrar los inputs para editar los campos
                st.subheader('Editar los datos del juguete')
                name, edad_recomendada = st.columns(2)
                name = name.text_input(
                    'Nombre', key='input_names', type='default', value=result["nombre"])
                edad_recomendada = edad_recomendada.text_input(
                    'Edad recomendada', key='input_edad_recomendadas', type='default', value=result["edad_recomendada"])
                descripcion = st.text_area(
                    'Descripcion', key='input_descripciones', value=result["descripcion"])
                imagen = st.text_input(
                    'Imagen', key='input_imagenes', type='default', value=result["imagen"])
                precio, stock, marca = st.columns(3)
                precio = precio.text_input(
                    'Precio', key='input_precios', type='default', value=result["precio"])
                stock = stock.text_input(
                    'Stock', key='input_stocks', type='default', value=result["stock"])
                marca = marca.text_input(
                    'Marca', key='input_marcas', type='default', value=result["marca"])
                categoria = st.selectbox('Categoria', ['Niñas', 'Niños', 'Didacticos'], index=[
                    'Niñas', 'Niños', 'Didacticos'].index(result["categoria"]))

                # Crear un boton para actualizar los datos del juguete
                button = st.button('Actualizar datos')

                # Si se ha presionado el boton para actualizar los datos
                if button:
                    # Actualizar los campos del juguete en la base de datos
                    db.db["juguetes"].update_one(
                        {'nombre': search_term},
                        {'$set': {
                            'nombre': name,
                            'edad_recomendada': edad_recomendada,
                            'descripcion': descripcion,
                            'imagen': imagen,
                            'precio': precio,
                            'stock': stock,
                            'marca': marca,
                            'categoria': categoria
                        }}
                    )

                    # Mostrar mensaje de exito
                    st.success(
                        'Los datos del juguete se han actualizado con exito')
