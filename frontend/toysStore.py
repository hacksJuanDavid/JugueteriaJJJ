# Import streamlit
import streamlit as st

# Importar search
import frontend.search as InterfaceSearch



# Crear una carta para los juguetes
def CardToy(juguete):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(juguete["imagen"], width=180)
    with col2:
        st.write(f"<h1 style='color: #9B0707'>{juguete['nombre']}</h1>", unsafe_allow_html=True)
        st.write(f"<h3>Edad recomendada: {juguete['edad_recomendada']}</h3>", unsafe_allow_html=True)
        st.write(f"<p>{juguete['descripcion']}</p>", unsafe_allow_html=True)
        st.write(f"Precio: {juguete['precio']}")
        st.write(f"Stock: {juguete['stock']}")
        st.write(f"Marca: {juguete['marca']}")
        st.write(f"Categoria: {juguete['categoria']}")
        st.divider()

# Crear una funcion para la pagina principal de la app
def Home():
    # Cargar la imagen de la jugueteria
    file = open("public/imagenJ.jpg", "rb")
    # Cargar una imagen en la pagina principal
    st.image(file.read(), width=700)
    
    # Crear 2 columnas
    col1, col2 = st.columns(2)

    with col1:
        # Subtitulo
        st.subheader('Bienvenido a la jugueteria')
    
    with col2:
        # Subtitulo
        st.subheader('Busca tu juguete favorito')
        # Call the function InterfaceSearch
        InterfaceSearch.InterfaceSearch()

    # Crear tabs 
    tab1, tab2, tab3 = st.tabs(['Juguetes para niñas', 'Juguetes para niños','Juguetes Didacticos'])

    # Si el tab seleccionado es 'Juguetes para niñas'
    with tab1:
        # Titulo
        st.title('Juguetes para niñas')
        # Subtitulo
        st.subheader('Juguetes para niñas')
        
        # Call the function CardToy
        CardToy({
            "nombre": "Barbie Mascotas",
            "edad_recomendada": "3+",
            "descripcion": "Barbie es una muñeca de plástico fabricada por la compañía estadounidense Mattel, Inc. y lanzada en marzo de 1959. Las muñecas Barbie fueron creadas por Ruth Handler, quien co-fundó Mattel con su esposo Elliot Handler, junto con la diseñadora de muñecas de Mattel Charlotte Johnson.",
            "imagen": "http://cdn.shopify.com/s/files/1/0600/0141/9429/products/qe2any0ugvfgve4ljq6k_17d9c54b-edd3-4cb7-96c2-3472b389e5ff.jpg?v=1674180824",
            "precio": "$ 100.000",
            "stock": "10",
            "marca": "Mattel",
            "categoria": "Muñecas"
        })

        # Call the function CardToy
        CardToy({
            "nombre": "Barbie",
            "edad_recomendada": "3+",
            "descripcion": "Barbie es una muñeca de plástico fabricada por la compañía estadounidense Mattel, Inc. y lanzada en marzo de 1959. Las muñecas Barbie fueron creadas por Ruth Handler, quien co-fundó Mattel con su esposo Elliot Handler, junto con la diseñadora de muñecas de Mattel Charlotte Johnson.",
            "imagen": "http://cdn.shopify.com/s/files/1/0600/0141/9429/products/qe2any0ugvfgve4ljq6k_17d9c54b-edd3-4cb7-96c2-3472b389e5ff.jpg?v=1674180824",
            "precio": "$ 100.000",
            "stock": "10",
            "marca": "Mattel",
            "categoria": "Muñecas"
        })


    # Si el tab seleccionado es 'Juguetes para niños'
    with tab2:
        # Titulo
        st.title('Juguetes para niños')
        # Subtitulo
        st.subheader('Juguetes para niños')
        # Texto
        st.text('Aquí encontrarás los mejores juguetes para niños')
        # Imagen
        st.image('https://www.abc.es/Media/201505/20/juguetes--644x362.jpg')
        # Texto
        st.text('Aquí encontrarás los mejores juguetes para tus hijos')

    # Si el tab seleccionado es 'Juguetes Didacticos'
    with tab3:
        # Titulo
        st.title('Juguetes Didacticos')
        # Subtitulo
        st.subheader('Juguetes Didacticos')
        # Texto
        st.text('Aquí encontrarás los mejores juguetes Didacticos')
        # Imagen
        st.image('https://www.abc.es/Media/201505/20/juguetes--644x362.jpg')
        # Texto
        st.text('Aquí encontrarás los mejores juguetes Didacticos')

# Crear una funcion para la pagina de juguetes
def InterfaceHome():
    # Call the function PagPrincipal
    Home()



    

    

