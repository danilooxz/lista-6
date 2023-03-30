qtde = int(input("Informe a quatidade comprada:"))
valorUnit = float(input("Informe o valor unitário"))
desconto = float(input("Informe o desconto"))

totalSemDesconto = qtde * valorUnit
valorDesconto = totalSemDesconto * desconto/100
totalComDesconto = totalSemDesconto - valorDesconto

print(f'O total sem desconto será R$ {totalSemDesconto:.2f}')
print(f"O valor do desconto será R$ {valorDesconto:.2f}")
print(f'O total com o desconto será R${totalComDesconto:.2f}')
