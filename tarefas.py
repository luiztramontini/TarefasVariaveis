#CÁLCULO DE BÔNUS DE VENDAS

#Calcular valor do bônus sobre o faturamento 

faturamento = 50.000
bonus = 0.10 

valor_bonus = faturamento * bonus
faturamento_final = faturamento - valor_bonus

print('Valor do bônus:', valor_bonus)
print('Faturamento final:', faturamento_final)

#CONTROLE DE ESTOQUE 

estoque = 250 
vendidos = 78 
fornecedor = 100

saldo = estoque - vendidos 
print('O saldo é de', saldo, 'unidades')

saldo_final = saldo + fornecedor
print('O saldo final é de', saldo_final, 'unidades')

#DIVISÃO DE CARGAS 

carga_total = 1250 
carga_caminhoes = carga_total // 12
carga_restante =  carga_total % 12 

print('O número de caminhões foi de', carga_caminhoes)
print('A carga restante é de', carga_restante)

#MARGEM DE LUCRO 

faturamento_total = 15000
custos_fixos = 5000
imposto = 0.15 

lucro_liquido = faturamento_total - custos_fixos - imposto * faturamento_total
margem_lucro = lucro_liquido / faturamento_total

print('O lucro líquido foi de', lucro_liquido)
print('A margem de lucro foi', margem_lucro)

meta = 0.30
meta_atingida = margem_lucro >= meta 

print(meta_atingida)

#CONVERSÃO DE TEMPO DE CONTRATO

contrato = 40 
anos = contrato // 12
meses = contrato %12 

print('A duracão do contrato é de', anos, 'anos e', meses, 'meses')