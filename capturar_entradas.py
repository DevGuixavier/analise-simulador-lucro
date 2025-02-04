import streamlit as st

def capturar_entradas():
    st.sidebar.header("Parâmetros")

    # Parâmetros gerais
    clientes_iniciais = st.sidebar.number_input(
        "Clientes Iniciais",
        min_value=0,
        value=100,
        help="Número inicial de clientes."
    )

    cac = st.sidebar.number_input(
        "CAC (R$)",
        min_value=0,
        value=150,
        help="Custo de Aquisição por Cliente."
    )

    ticket_primeira_compra = st.sidebar.number_input(
        "Ticket Médio Primeira Compra (R$)",
        min_value=0,
        value=100,
        help="Valor médio gasto pelo cliente na primeira compra."
    )

    ticket_recompra = st.sidebar.number_input(
        "Ticket Médio Recompra (R$)",
        min_value=0,
        value=200,
        help="Valor médio gasto pelo cliente em recompras."
    )

    margem = st.sidebar.slider(
        "Margem de Lucro (%)",
        min_value=0,
        max_value=100,
        value=30,
        help="Margem de lucro em porcentagem."
    ) / 100

    meses = st.sidebar.number_input(
        "Número de Meses",
        min_value=1,
        value=36,
        help="Período de análise em meses."
    )

    # Probabilidades de recompra
    prob_recompra_primeiro_mes = st.sidebar.slider(
        "Probabilidade de Recompra no 1º Mês",
        0.0, 1.0, 0.2,
        help="Probabilidade de o cliente realizar uma recompra no primeiro mês."
    )

    prob_recompra_meses_seguintes = st.sidebar.slider(
        "Probabilidade de Recompra nos Meses Seguintes",
        0.0, 1.0, 0.05,
        help="Probabilidade de o cliente realizar uma recompra nos meses seguintes."
    )

    return (
        clientes_iniciais,
        cac,
        ticket_primeira_compra,
        ticket_recompra,
        margem,
        meses,
        prob_recompra_primeiro_mes,
        prob_recompra_meses_seguintes
    )
