# Questão 1)
# Resposta: K começa em 0 e enquanto for menor que 13 ele é incrementado, a cada incremento o valor de K é somado à variável SOMA.
# no final, SOMA será a soma de todos os números de 1 a 13, ou seja, 91.


# Questão 2)
numero = int(input("Digite o número que será analisado: "))

def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or a == n


if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci")


# Questão 3)
import json

faturamento_json = '''[
	{
		"dia": 1,
		"valor": 22174.1664
	},
	{
		"dia": 2,
		"valor": 24537.6698
	},
	{
		"dia": 3,
		"valor": 26139.6134
	},
	{
		"dia": 4,
		"valor": 0.0
	},
	{
		"dia": 5,
		"valor": 0.0
	},
	{
		"dia": 6,
		"valor": 26742.6612
	},
	{
		"dia": 7,
		"valor": 0.0
	},
	{
		"dia": 8,
		"valor": 42889.2258
	},
	{
		"dia": 9,
		"valor": 46251.174
	},
	{
		"dia": 10,
		"valor": 11191.4722
	},
	{
		"dia": 11,
		"valor": 0.0
	},
	{
		"dia": 12,
		"valor": 0.0
	},
	{
		"dia": 13,
		"valor": 3847.4823
	},
	{
		"dia": 14,
		"valor": 373.7838
	},
	{
		"dia": 15,
		"valor": 2659.7563
	},
	{
		"dia": 16,
		"valor": 48924.2448
	},
	{
		"dia": 17,
		"valor": 18419.2614
	},
	{
		"dia": 18,
		"valor": 0.0
	},
	{
		"dia": 19,
		"valor": 0.0
	},
	{
		"dia": 20,
		"valor": 35240.1826
	},
	{
		"dia": 21,
		"valor": 43829.1667
	},
	{
		"dia": 22,
		"valor": 18235.6852
	},
	{
		"dia": 23,
		"valor": 4355.0662
	},
	{
		"dia": 24,
		"valor": 13327.1025
	},
	{
		"dia": 25,
		"valor": 0.0
	},
	{
		"dia": 26,
		"valor": 0.0
	},
	{
		"dia": 27,
		"valor": 25681.8318
	},
	{
		"dia": 28,
		"valor": 1718.1221
	},
	{
		"dia": 29,
		"valor": 13220.495
	},
	{
		"dia": 30,
		"valor": 8414.61
	}
]'''

dados = json.loads(faturamento_json)
faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]

menor_valor = min(faturamento)
maior_valor = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)
dias_acima_da_media = len([dia for dia in faturamento if dia > media_mensal])

print(f"O menor valor de faturamento ocorrido em um dia do mês: {menor_valor:.2f}")
print(f"O maior valor de faturamento ocorrido em um dia do mês; {maior_valor:.2f}")
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {dias_acima_da_media}")


# Questão 4)
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento_estados.values())

for estado, valor in faturamento_estados.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")


# Questão 5)
s = input("Digite uma string: ")
s = s[::-1]
print(f"String invertida: {s}")