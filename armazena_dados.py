import sqlite3
import streamlit as st

def armazenar_dados(
    CAC, ticket_inicial, ticket_recompra, margem_lucro, 
    clientes_iniciais, prob_recompra_primeiro_mes, prob_recompra_meses_seguintes
):
    try:
        # Validação de inputs
        if any(valor < 0 for valor in [CAC, ticket_inicial, ticket_recompra, margem_lucro, clientes_iniciais]):
            st.error("Valores negativos não são permitidos para CAC, ticket_inicial, ticket_recompra, margem_lucro ou clientes_iniciais.")
            return
        
        if not (0 <= prob_recompra_primeiro_mes <= 1) or not (0 <= prob_recompra_meses_seguintes <= 1):
            st.error("As probabilidades de recompra devem estar entre 0 e 1.")
            return

        # Conectando ao banco de dados SQLite
        with sqlite3.connect("entradas.db") as conn:
            c = conn.cursor()

            # Criando a tabela se não existir, com a chave única para evitar duplicação
            c.execute("""
                CREATE TABLE IF NOT EXISTS entradas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    CAC REAL,
                    ticket_inicial REAL,
                    ticket_recompra REAL,
                    margem_lucro REAL,
                    clientes_iniciais INTEGER,
                    prob_recompra_primeiro_mes REAL,
                    prob_recompra_meses_seguintes REAL,
                    UNIQUE(CAC, ticket_inicial, ticket_recompra, margem_lucro, 
                           clientes_iniciais, prob_recompra_primeiro_mes, prob_recompra_meses_seguintes)
                )
            """)

            # Verifica se os dados já existem no banco para evitar duplicatas (agora redundante, pois a chave UNIQUE já evita)
            c.execute("""
                SELECT 1 FROM entradas
                WHERE CAC = ? AND ticket_inicial = ? AND ticket_recompra = ? 
                AND margem_lucro = ? AND clientes_iniciais = ? 
                AND prob_recompra_primeiro_mes = ? AND prob_recompra_meses_seguintes = ?
            """, (CAC, ticket_inicial, ticket_recompra, margem_lucro, 
                  clientes_iniciais, prob_recompra_primeiro_mes, prob_recompra_meses_seguintes))

            if c.fetchone():
                st.warning("Esses dados já foram armazenados anteriormente no banco de dados.")
                return

            # Inserindo os valores na tabela
            c.execute("""
                INSERT INTO entradas (CAC, ticket_inicial, ticket_recompra, margem_lucro, 
                                     clientes_iniciais, prob_recompra_primeiro_mes, prob_recompra_meses_seguintes)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (CAC, ticket_inicial, ticket_recompra, margem_lucro, 
                  clientes_iniciais, prob_recompra_primeiro_mes, prob_recompra_meses_seguintes))

            # Confirma a transação
            conn.commit()
            st.success("Dados armazenados com sucesso no banco de dados!")

    except sqlite3.Error as e:
        # Tratando erros de conexão ou execução de queries
        st.error(f"Erro ao armazenar dados no banco de dados: {e}")
