import streamlit as st
import pandas as pd

st.title("Estadística Fácil - Introducción a la Estadística Descriptiva")

# Agregar el texto de bienvenida debajo del título con formato Markdown
st.markdown("""
**Bienvenidos a la aplicación de Estadística Fácil.** 

En esta aplicación podrás realizar un análisis 
exploratorio de tus datos de manera rápida y sencilla. Para comenzar, sube tu archivo de datos en formato Excel.
""")

uploaded_file = st.file_uploader("Subir Archivo Excel", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("1. Exploración inicial de los datos")
    st.write(df.head())

    st.write("Tipos de variables")
    st.write(df.dtypes)

    st.write("2. Estadísticos descriptivos")
    st.write(df.describe())

    st.write("3. Tablas de frecuencias variables categóricas")
    cat_vars = df.select_dtypes(include=['object'])
    for col in cat_vars.columns:
        st.write(f"Tabla de frecuencias para {col}")
        freq_table = cat_vars[col].value_counts().reset_index()
        freq_table.columns = ['Categoría', 'Frecuencia']
        freq_table['Porcentaje'] = (freq_table['Frecuencia'] / freq_table['Frecuencia'].sum()) * 100
        st.write(freq_table)
