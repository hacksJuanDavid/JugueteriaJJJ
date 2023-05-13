# Importamos streamlit
import streamlit as st

# Creamos una funcion para buscar juguetes
def InterfaceSearch():
    # Crear un input para buscar juguetes
    search = st.text_input('',placeholder='Buscar juguetes...')

    # Boton para buscar juguetes
    button = st.button('Buscar')

    # Si el boton es presionado
    if button:
        # Texto
        st.text('Buscando juguetes...')
