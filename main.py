import streamlit as st
import plotly.express as px
import pandas as pd
from capturar_entradas import capturar_entradas  # Importa a função para capturar entradas
from calculo_lucro import calcular_lucro  # Importa a função para calcular o lucro
from armazena_dados import armazenar_dados  # Importa a função para armazenar os dados

# Configurando a página principal do Streamlit
def main():
    st.title("Simulação de Lucro Acumulado")

    # Captura os parâmetros de entrada usando a função de captura
    (
        clientes_iniciais,
        cac,
        ticket_primeira_compra,
        ticket_recompra,
        margem,
        meses,
        prob_recompra_primeiro_mes,
        prob_recompra_meses_seguintes
    ) = capturar_entradas()

    # Botão para armazenar os dados
    if st.sidebar.button("Armazenar Dados"):
        armazenar_dados(
            cac,
            ticket_primeira_compra,
            ticket_recompra,
            margem,
            clientes_iniciais,
            prob_recompra_primeiro_mes,
            prob_recompra_meses_seguintes
        )

    # Calcular o lucro usando a função de cálculo
    lucro_mes, receita_mes = calcular_lucro(
        meses, 
        clientes_iniciais, 
        cac, 
        ticket_primeira_compra, 
        ticket_recompra, 
        margem, 
        prob_recompra_primeiro_mes, 
        prob_recompra_meses_seguintes
    )

    # Criar o DataFrame com os resultados
    df = pd.DataFrame({
        'Mês': list(range(1, meses + 1)),
        'Lucro Acumulado': lucro_mes,
        'Receita Mensal': receita_mes,
    })

    # Criar o gráfico interativo
    st.subheader("Gráfico de Lucro Acumulado")
    fig = px.line(df, x='Mês', y='Lucro Acumulado', title="Lucro Acumulado ao Longo dos Meses")
    st.plotly_chart(fig)

    # Informar o primeiro mês lucrativo
    mes_lucrativo = next((i for i, x in enumerate(df['Lucro Acumulado']) if x > 0), None)
    if mes_lucrativo is None:
        st.write("O grupo de clientes nunca se torna lucrativo.")
    else:
        st.write(f"O grupo de clientes se torna lucrativo no mês {mes_lucrativo + 1}.")

if __name__ == "__main__":
    main()
