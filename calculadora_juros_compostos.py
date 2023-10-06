# inputs iniciais para pegar as informações de capital inicial, taxa de juros mensal, aportes mensais, periodo em meses.
capital_inicial = float(input('Capital inicial: '))
taxa_juros_mensal = float(input('Taxa de juros mensal: '))
aporte_mensal = float(input('Aporte mensal: '))
periodo_mensal = int(input('Período em meses: '))

# calcula a porcentagem e o valor final do primeiro mês
capital_porcentagem = capital_inicial + (taxa_juros_mensal * capital_inicial / 100)
valor_final = capital_porcentagem + aporte_mensal

# looping de repetição while para fazer mês a mês o calculo de porcentagem do valor inicial com o aporte mensal
contador = 1
while contador < periodo_mensal:
    valor_final = valor_final + (taxa_juros_mensal * valor_final / 100)
    valor_final = valor_final + aporte_mensal
    contador = contador + 1

# calcula todos valors finais de valor investido e total de juros acumulados durante todo o período para serem mostrados na tela
valor_investido = capital_inicial + (aporte_mensal * periodo_mensal)
total_juros = valor_final - valor_investido

# pega o resultado e mostra na tela o valor final, valor investido e total de juros acomulado
print(f'\nResultado: \n\nValor final: {valor_final :.2f}\t\tValor investido: {valor_investido :.2f}\t\tTotal em juros: {total_juros :.2f}')

input()
