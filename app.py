import streamlit as st
import pandas as pd
import numpy as np
import openpyxl, sys

# Función para convertir tipos de datos a tipos compatibles con Arrow
def convert_types(df):
    for col in df.columns:
        if pd.api.types.is_integer_dtype(df[col]):
            df[col] = df[col].astype('Int64')
        elif pd.api.types.is_float_dtype(df[col]):
            df[col] = df[col].astype('Float32')
        elif pd.api.types.is_object_dtype(df[col]):
            df[col] = df[col].astype('string')
    return df

# Diseño del encabezado con imagen y título
col1, col2 = st.columns([1, 6])
with col1:
    st.image('logo.jpg', width=100)
with col2:
    st.title("Estadística Fácil - Una herramienta para una exploración rápida de datos")

# Panel lateral con botones
st.sidebar.title("Menú")
option = st.sidebar.radio("Seleccione una sección", ('Generalidades', 'Exploración inicial', 'Estadísticos descriptivos', 'Tablas de frecuencias'))

# Sección de Generalidades
if option == 'Generalidades':
    st.markdown("""
    **Bienvenidos a Estadística Fácil.** 

    Bienvenidos a Estadística Fácil, una herramienta diseñada para simplificar el análisis estadístico de datos, 
    especialmente para aquellos que están dando sus primeros pasos en el mundo de la estadística. 
    Con esta aplicación, podrás realizar un análisis exploratorio de tus datos de manera rápida y sencilla. 
    Solo necesitas subir tu archivo de datos en formato Excel y la aplicación te guiará a través de diversas funcionalidades, 
    como la exploración inicial de los datos, la identificación de tipos de variables, 
    la generación de estadísticos descriptivos y la creación de tablas de frecuencias para variables categóricas. 
    Estadística Fácil está pensada para hacer accesible y comprensible el análisis estadístico, 
    proporcionando una primera aproximación clara y amigable a la estadística descriptiva.
    """)

# Carga del archivo Excel
uploaded_file = st.sidebar.file_uploader("Subir Archivo Excel", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, engine="openpyxl")
    df = convert_types(df)  # Convertir los tipos de datos
    
    # Sección de Exploración inicial
    if option == 'Exploración inicial':
        st.write("1. Exploración inicial de los datos")
        st.write(df.head())

        st.write("Tipos de variables")
        st.write(df.dtypes)
    
    # Sección de Estadísticos descriptivos
    elif option == 'Estadísticos descriptivos':
        st.write("2. Estadísticos descriptivos")
        st.write(df.describe())
    
    # Sección de Tablas de frecuencias
    elif option == 'Tablas de frecuencias':
        st.write("3. Tablas de frecuencias variables categóricas")
        cat_vars = df.select_dtypes(include=['string'])
        for col in cat_vars.columns:
            st.write(f"Tabla de frecuencias para {col}")
            freq_table = cat_vars[col].value_counts().reset_index()
            freq_table.columns = ['Categoría', 'Frecuencia']
            freq_table['Porcentaje'] = (freq_table['Frecuencia'] / freq_table['Frecuencia'].sum()) * 100
            st.write(freq_table)
else:
    st.write("Por favor, sube un archivo Excel para comenzar el análisis.")
