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

    # Buscar el juguete en la base de datos
    result = db.db["juguetes"].find_one({'nombre': search_term})

    # Crear un tabla vertical para mostrar los datos del juguete
    if result:
        # Crear un dataframe con los datos del juguete
        df = pd.DataFrame(result, index=[0])

        # Rename columns to spanish
        df = df.rename(columns={
            'nombre': 'Nombre',
            'edad_recomendada': 'Edad recomendada',
            'descripcion': 'Descripcion',
            'imagen': 'Imagen',
            'precio': 'Precio',
            'stock': 'Stock',
            'marca': 'Marca',
            'categoria': 'Categoria'
        })

        # Rename index to spanish
        df = df.rename(index={0: 'Datos del juguete'})

        # Vertical table
        st.table(df.T)

    # Si el flag es verdadero se muestran los datos del juguete
    if result:
        # Crear un formulario para editar los datos del juguete
        with st.form(key='edit_form'):
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
                'Niñas', 'Niños', 'Didacticos'].index(result["categoria"]), key='input_categorias')

            # Crear un boton para actualizar los datos del juguete
            submit_button = st.form_submit_button(label='Actualizar')

            # al presionar el boton de actualizar se actualizan los datos del juguete
            if submit_button:
                # Actualizar los datos del juguete
                db.db["juguetes"].update_one({'nombre': search_term}, {
                    '$set': {
                        'nombre': name,
                        'edad_recomendada': edad_recomendada,
                        'descripcion': descripcion,
                        'imagen': imagen,
                        'precio': precio,
                        'stock': stock,
                        'marca': marca,
                        'categoria': categoria
                    }
                })

                # Mostrar un mensaje de exito
                st.success('Juguete actualizado con exito')
    # Si el flag es falso se muestra un mensaje de error
    else:
        st.error('Ingrese un nombre de juguete')
