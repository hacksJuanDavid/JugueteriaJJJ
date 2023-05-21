# Import sidebar
import frontend.sideBar as SideBar

# Importar footer
import frontend.footer as InterfaceFooter

# Importar streamlit
import streamlit as st

# Función principal


def main():

    # Favicon of the app interface
    st.set_page_config(
        page_title="JugueteriaJJJ",
        page_icon="🧸",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Call the function SideBar
    SideBar.SideBar()

    # Call the function InterfaceFooter
    InterfaceFooter.InterfaceFooter()


# Ejecutar función principal
if __name__ == '__main__':
    main()
