import streamlit as st
import plotly.express as px
import pandas as pd

def criar_dashboard(df):
    # Verifica se as colunas necessárias existem no DataFrame
    if 'Mês' not in df.columns or 'Lucro Acumulado' not in df.columns:
        st.error("O DataFrame precisa conter as colunas 'Mês' e 'Lucro Acumulado'.")
        return

    # Verifica se o DataFrame está vazio
    if df.empty:
        st.error("O DataFrame está vazio.")
        return
    
    # Garantir que a coluna 'Mês' seja numérica para evitar erros na visualização
    df["Mês"] = pd.to_numeric(df["Mês"], errors="coerce")
    df = df.dropna()  # Remove possíveis valores não numéricos

    # Título do dashboard
    st.title("Simulação de Lucro e Receita")

    # Gráfico de lucro acumulado
    st.write("### Lucro Acumulado ao Longo dos Meses")
    fig_lucro = px.line(df, x="Mês", y="Lucro Acumulado", title="Lucro Acumulado", markers=True)
    st.plotly_chart(fig_lucro)

    # Encontrar o mês em que o grupo de clientes se torna lucrativo
    mes_lucrativo = (df["Lucro Acumulado"] > 0).idxmax() if (df["Lucro Acumulado"] > 0).any() else None

    # Exibir resultado sobre a lucratividade
    if mes_lucrativo is None:
        st.write("O grupo de clientes nunca se torna lucrativo.")
    else:
        st.write(f"O grupo de clientes se torna lucrativo no mês {mes_lucrativo + 1}.")
