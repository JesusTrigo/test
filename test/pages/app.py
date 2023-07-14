import streamlit as st
from pages import plots
from pages import recomend

def show():
    # Mostrar enlaces para elegir entre plots.py y app.py
    st.markdown("## Recommendations")
    if st.button("Plots"):
        plots.show()
    elif st.button("App"):
        app.run()

# Ejecutar la función show() cuando se llama al archivo
if __name__ == '__main__':
    show()
