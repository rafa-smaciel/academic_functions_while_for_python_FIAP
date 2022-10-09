#Criar um programa que solicite ao usuario o faturamento médio de sua empresa ao longo de 12 meses do ano.
#Ao final, o programa deve exibir a media anual de faturamento e o maior faturamento do ano.

print("Faturamento médio Anual")
faturamento_medio = 0
menor_faturamento = 0
maior_faturamento = 0

for mes in range(1, 13, 1):
    faturamento = float(input(f"Informe o faturamento do mês {mes}: "))
    faturamento_medio = faturamento_medio + faturamento
    if mes == 1:
        maior_fatuamento = faturamento
        menor_faturamento = faturamento
    else:
        if menor_faturamento > faturamento:
            menor_faturamento = faturamento
        
        if maior_faturamento < faturamento:
            maior_faturamento = faturamento
    
media_faturamento = faturamento_medio /12
print(f"Você teve um faturamento de {media_faturamento:.2f}")
print(f"O menor faturamento foi de R${menor_faturamento:.2f}")
print(f"O maior faturamento foi de R${maior_faturamento:.2f}")