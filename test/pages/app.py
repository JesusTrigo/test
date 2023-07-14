import streamlit as st
from pages.pages import plots
from pages.pages import recomend

def show():
    # Mostrar enlaces para elegir entre plots.py y app.py
    st.markdown("## Recommendations")
    if st.button("Plots"):
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
    elif st.button("App"):
        app.run()

# Ejecutar la función show() cuando se llama al archivo
if __name__ == '__main__':
    show()
