import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuración de la página
st.set_page_config(page_title="Mi Primera Web Pública", layout="centered")

st.title("¡Hola Mundo desde Internet! 🚀")
st.write("Esta página fue creada desde Jupyter, guardada en GitHub y desplegada en Streamlit Cloud.")

# 2. Datos simulados generados por Python
datos_ventas = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'Transacciones_Seguras': [500, 700, 650, 900, 850],
    'Alertas_Fraude': [5, 12, 4, 18, 9]
}
df = pd.DataFrame(datos_ventas)

# 3. Crear un gráfico interactivo con Python (Plotly)
grafico = px.line(
    df, 
    x='Mes', 
    y='Alertas_Fraude', 
    title='Evolución de Alertas de Fraude (Datos Simulados)',
    markers=True,
    template='plotly_white'
)

# 4. Mostrar el gráfico en la web
st.plotly_chart(grafico, use_container_width=True)

# 5. Un botón interactivo
if st.button("Púlsame para saludar"):
    st.success("¡Saludos chamo! El motor de Python en la nube está corriendo perfectamente. 🐣")
