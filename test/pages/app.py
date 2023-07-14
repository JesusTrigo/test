import streamlit as st
from app.test.pages.pages.recomend import plots
from app.test.pages.pages.recomend import recomend

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
