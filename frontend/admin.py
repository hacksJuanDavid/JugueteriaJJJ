# Import streamlit
import streamlit as st

# Importar insertToy de backend/insertToy.py
from backend.insertToy import InterfaceInsert

# Importar viewToy de backend/viewToy.py
from backend.viewToy import InterfaceView

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
        # Insertar juguetes
        InterfaceInsert()
    
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
        # Ver juguetes
        InterfaceView()

