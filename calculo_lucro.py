import numpy as np

def calcular_lucro(
    meses, clientes_iniciais, cac, ticket_primeira_compra, 
    ticket_recompra, margem, prob_recompra_primeiro_mes, prob_recompra_meses_seguintes
):
    # Validação de inputs
    if meses < 1:
        raise ValueError("O número de meses deve ser maior ou igual a 1.")
    
    if clientes_iniciais < 0 or cac < 0 or ticket_primeira_compra < 0 or ticket_recompra < 0:
        raise ValueError("Valores negativos não são permitidos para clientes_iniciais, cac, ticket_primeira_compra ou ticket_recompra.")
    
    if not (0 <= prob_recompra_primeiro_mes <= 1) or not (0 <= prob_recompra_meses_seguintes <= 1):
        raise ValueError("As probabilidades de recompra devem estar entre 0 e 1.")

    # Definição das probabilidades de recompra para cada mês
    if meses <= 9:
        prob_recompra = np.linspace(prob_recompra_primeiro_mes, prob_recompra_meses_seguintes, meses).tolist()
    else:
        prob_recompra = (
            np.linspace(prob_recompra_primeiro_mes, prob_recompra_meses_seguintes, 9).tolist() + 
            [prob_recompra_meses_seguintes] * (meses - 9)
        )

    # Inicializa variáveis
    lucro_acumulado = -clientes_iniciais * cac  # Custo inicial de aquisição de clientes
    clientes_atuais = clientes_iniciais
    lucro_mes = []
    receita_mes = []

    # Cálculo do lucro e receita mês a mês
    for mes in range(1, meses + 1):
        prob = prob_recompra[mes - 1]  # Probabilidade de recompra para o mês corrente
        novos_clientes = clientes_atuais * prob  # Número de clientes que realizaram recompra
        
        receita_mes_atual = novos_clientes * ticket_recompra  # Receita do mês
        lucro_mes_atual = receita_mes_atual * margem  # Lucro do mês considerando a margem

        # Atualiza os valores acumulados
        lucro_acumulado += lucro_mes_atual
        lucro_mes.append(lucro_acumulado)
        receita_mes.append(receita_mes_atual)
        
        # Atualiza o número de clientes atuais para o próximo mês
        clientes_atuais += novos_clientes  
    
    return lucro_mes, receita_mes
