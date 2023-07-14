import streamlit as st
from pages.pages import plots, recomend

df_Beer = recomend.df_Beer

st.write('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" rel="stylesheet">',

         # Estilo personalizado para el ícono de flecha
         '<style>',
         '.custom-select .fas {',
         '    font-size: 16px;',
         '    margin-left: 4px;',
         '}',
         '</style>',

         # Contenedor de selección personalizado con ícono de flecha
         '<div class="custom-select">',
         '    <select>',
         '        <option>Opción 1</option>',
         '        <option>Opción 2</option>',
         '        <option>Opción 3</option>',
         '    </select>',
         '    <i class="fas fa-chevron-down"></i>',  # Icono de flecha hacia abajo de FontAwesome
         '</div>',

         # Script de JavaScript para inicializar el contenedor de selección personalizado
         '<script>',
         '    document.addEventListener("DOMContentLoaded", function() {',
         '        var select = document.querySelector(".custom-select select");',
         '        select.addEventListener("change", function() {',
         '            console.log("Seleccionado:", this.value);',
         '        });',
         '    });',
         '</script>',
         sep='\n')

def main():
    # Mostrar enlaces para elegir entre plots.py y app.py
    opcion = st.radio("Seleccione una opción:", ["App", "Gráficos"])

    if opcion == "App":
        recomend.main()
    elif opcion == "Gráficos":
        plots.intro()
        plots.get_top_25_beer_styles(df_Beer)
        plots.plot_most_common_beer_bar(df_Beer)
        plots.plot_most_reviewed_beers(df_Beer)
        plots.plot_sentiment_distribution(df_Beer)
        plots.plot_most_common_beer_treemap(df_Beer)
        plots.plot_sentiment_beer_style_bubble(df_Beer)
        plots.plot_review_features_correlation(df_Beer)
        plots.plot_abv_beer_style_box(df_Beer)
        plots.plot_3d_scatter_aroma_palate_abv(df_Beer)
        plots.plot_beer_wordcloud(df_Beer)

if __name__ == '__main__':
    main()
