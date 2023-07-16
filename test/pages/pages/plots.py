import matplotlib.pyplot as plt
import seaborn as sns
import squarify
from PIL import Image
from wordcloud import WordCloud
import plotly.express as px
import numpy as np
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import recomend

df_Beer = recomend.df_Beer


def main():
    def intro():
        st.title("Gráficos recomendador de cervezas")
        st.write("""
        A continuación se muestran una serie de gráficos que relacionan diversas variables de la base de datos.
        """)

    def get_top_25_beer_styles(df_Beer):
        return df_Beer['beer/style'].value_counts().head(25).index

    def plot_most_common_beer_bar(df_Beer):
        beer_counts = df_Beer['beer/style'].value_counts().nlargest(25)

        fig = go.Figure(data=[go.Bar(
            x=beer_counts.values,
            y=beer_counts.index,
            orientation='h'
        )])
        fig.update_layout(
            title="25 tipos de cerveza más comunes",
            xaxis_title="Cantidad",
            yaxis_title="Tipo de cerveza",
            template='plotly_white'
        )
        st.plotly_chart(fig)

    def plot_beer_wordcloud(df_Beer):
        beer_counts = df_Beer['beer/name'].value_counts()
        beer_mask = np.array(Image.open('ruta/a/tu/imagen.png'))
        wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=100, mask=beer_mask, contour_width=3, contour_color='black')
        wordcloud.generate_from_frequencies(beer_counts)
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        fig.tight_layout()
        st.pyplot(fig)

    def plot_most_common_beer_treemap(df_Beer):
        beer_counts = df_Beer['beer/style'].value_counts().nlargest(25).reset_index()
        beer_counts.columns = ['Beer Style', 'Count']

        fig = px.treemap(beer_counts, path=['Beer Style'], values='Count', title='Distribución de las 25 cervezas más comunes por tipo (Treemap)')
        fig.update_layout(margin=dict(t=50, l=0, r=0, b=0))

        st.plotly_chart(fig)

    def plot_most_reviewed_beers(df_Beer):
        top_beers = df_Beer['beer/name'].value_counts().head(10)

        fig = go.Figure(data=[go.Pie(labels=top_beers.index, values=top_beers.values)])

        fig.update_layout(
            title='Las 10 cervezas más revisadas',
            height=600,
            width=800,
        )

        st.plotly_chart(fig)
        plt.title("Nube de palabras de nombres de cervezas")

    intro()
    
    get_top_25_beer_styles(df_Beer)
    
    plot_most_common_beer_bar(df_Beer)

    plot_beer_wordcloud(df_Beer)

    plot_most_common_beer_treemap(df_Beer)

    plot_most_reviewed_beers(df_Beer)


if __name__ == "__main__":
    main()
    
