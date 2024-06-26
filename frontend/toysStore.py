# Import streamlit
import base64
import streamlit as st
from PIL import Image
import io
# Importar search
import frontend.search as InterfaceSearch

# Importar buscar juguetes de backend/searchToy.py
from backend.searchToy import searchToyCategoria


# Crear una carta para los juguetes
def CardToy(juguete):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(juguete["imagen"], width=180)
    with col2:
        st.write(
            f"<h1 style='color: #49A0E8'>{juguete['nombre']}</h1>", unsafe_allow_html=True)
        st.write(
            f"<h3>Edad recomendada: {juguete['edad_recomendada']}</h3>", unsafe_allow_html=True)
        st.write(f"<p>{juguete['descripcion']}</p>", unsafe_allow_html=True)
        st.write(f"Precio: {juguete['precio']}")
        st.write(f"Stock: {juguete['stock']}")
        st.write(f"Marca: {juguete['marca']}")
        st.write(f"Categoria: {juguete['categoria']}")
        st.divider()


# Crear una funcion para buscar el juguete por categoria y mostrarlo en una carta
def searchToyCategoriaCard(categoria):
    # Buscar el juguete por categoria
    juguetes = searchToyCategoria(categoria)

    # Si no se encuentran juguetes
    if juguetes == None:
        # Mostrar mensaje de error
        st.error('No se encontraron juguetes')
    # Si se encuentran juguetes
    else:
        # Mostrar los juguetes en una carta
        for juguete in juguetes:
            CardToy(juguete)

# Crear una funcion para la pagina principal de la app


def Home():
    # Cargar la imagen de la juguetería
    image = Image.open("public/imagenJ.jpg")

    # Convertir la imagen en un búfer de bytes
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")

    # Obtener el contenido de la imagen en base64
    b64_img = base64.b64encode(buffer.getvalue()).decode()

    # Crear el fragmento HTML para la imagen centrada
    img_logo_jjj = f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/jpeg;base64,{b64_img}" width="700" alt="Imagen de la juguetería">
    </div>
    """

    # Mostrar el fragmento HTML en la página
    st.markdown(img_logo_jjj, unsafe_allow_html=True)

    # Titulo
    st.title('Bienvenido a la jugueteria')

    # Crear 2 columnas
    col1, col2 = st.columns(2)

    with col1:
        # Subtitulo
        st.subheader('Busca tu juguete favorito')

    with col2:
        # Call the function InterfaceSearch
        InterfaceSearch.InterfaceSearch()

    # Crear tabs
    tab1, tab2, tab3 = st.tabs(
        ['Juguetes para niñas', 'Juguetes para niños', 'Juguetes Didacticos'])

    # Si el tab seleccionado es 'Juguetes para niñas'
    with tab1:
        # Titulo
        st.title('Juguetes para niñas')
        # Subtitulo
        st.subheader('Juguetes para niñas')

        # Buscar los juguetes de la categoria 'Niñas'
        searchToyCategoriaCard('Niñas')

    # Si el tab seleccionado es 'Juguetes para niños'
    with tab2:
        # Titulo
        st.title('Juguetes para niños')
        # Subtitulo
        st.subheader('Juguetes para niños')

        # Buscar los juguetes de la categoria 'Niños'
        searchToyCategoriaCard('Niños')

    # Si el tab seleccionado es 'Juguetes Didacticos'
    with tab3:
        # Titulo
        st.title('Juguetes Didacticos')
        # Subtitulo
        st.subheader('Juguetes Didacticos')

        # Buscar los juguetes de la categoria 'Niños'
        searchToyCategoriaCard('Didacticos')

# Crear una funcion para la pagina de juguetes


def InterfaceHome():
    # Call the function PagPrincipal
    Home()
