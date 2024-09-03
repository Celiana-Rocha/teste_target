# Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import json

def calcular_faturamento(dados):
    # Extrai os valores de faturamento
    faturamento_diario = [item['valor'] for item in dados]

    # Converte todos os valores de faturamento para inteiros
    faturamento_inteiros = [int(valor) for valor in faturamento_diario]

    # Calcula o menor e o maior valor de faturamento
    menor_valor = min(faturamento_inteiros) if faturamento_inteiros else 0
    maior_valor = max(faturamento_inteiros) if faturamento_inteiros else 0

    # Calcula a média mensal
    media_mensal = sum(faturamento_inteiros) / len(faturamento_inteiros) if faturamento_inteiros else 0

    # Conta o número de dias com faturamento acima da média mensal
    dias_acima_da_media = sum(1 for valor in faturamento_inteiros if valor > media_mensal)

    return menor_valor, maior_valor, dias_acima_da_media

# Ler o arquivo JSON
with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

# Chama a função e exibe os resultados
menor_valor, maior_valor, dias_acima_da_media = calcular_faturamento(dados)

print(f"Menor valor de faturamento (valores inteiros): R${menor_valor:.2f}")
print(f"Maior valor de faturamento (valores inteiros): R${maior_valor:.2f}")
print(f"Número de dias com faturamento (valores inteiros) acima da média mensal: {dias_acima_da_media}")


