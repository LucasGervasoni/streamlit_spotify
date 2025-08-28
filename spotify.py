import streamlit as st
import pandas as pd

st.set_page_config(page_title="Spotify Songs", page_icon=":bar_chart:", layout="wide")

@st.cache_data
def load_data():
  df = pd.read_csv("01 Spotify.csv")
  return df

df = load_data()

st.session_state["df_spotify"] = df
df.set_index("Track", inplace=True)

artists = df["Artist"].value_counts().index
artist = st.sidebar.selectbox("Artista", artists)
df_filtered = df[df["Artist"] == artist]


albuns = df_filtered["Album"].value_counts().index
album = st.selectbox("Album", albuns)

df_filtered2 = df[df["Album"] == album]

show_chart = st.checkbox("Mostrar gráfico")

if show_chart:
  st.bar_chart(df_filtered2["Stream"])
