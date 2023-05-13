# Import streamlit
import streamlit as st

# Crear una funcion para el admin
def InterfaceAdmin():
    # Titulo
    st.title('Administrador')
    
    # Subtitulo
    st.subheader('Controlar la jugueteria JJJ')

    # Crear tabs
    tab1, tab2, tab3, tab4 = st.tabs(['Agregar juguetes', 'Eliminar juguetes', 'Actualizar juguetes', 'Ver juguetes'])

    # Si el tab seleccionado es 'Agregar juguetes'
    with tab1:
        # Titulo
        st.title('Agregar juguetes')
        # Subtitulo
        st.subheader('Agregar juguetes')
    
    # Si el tab seleccionado es 'Eliminar juguetes'
    with tab2:
        # Titulo
        st.title('Eliminar juguetes')
        # Subtitulo
        st.subheader('Eliminar juguetes')
    
    # Si el tab seleccionado es 'Actualizar juguetes'
    with tab3:
        # Titulo
        st.title('Actualizar juguetes')
        # Subtitulo
        st.subheader('Actualizar juguetes')

    # Si el tab seleccionado es 'Ver juguetes'
    with tab4:
        # Titulo
        st.title('Ver juguetes')
        # Subtitulo
        st.subheader('Ver juguetes')

