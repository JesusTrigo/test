import streamlit as st
from pages.pages import plots, recomend

def main():
    # Mostrar enlaces para elegir entre plots.py y app.py
    opcion = st.radio("Seleccione una opción:", ["App", "Gráficos"])

    if opcion == "App":
        recomend.main()
    elif opcion == "Gráficos":
        plots.main()

if __name__ == '__main__':
    main()
