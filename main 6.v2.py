qtde = int(input("Informe a quatidade comprada:"))
valorUnit = float(input("Informe o valor unitário"))
desconto = float(input("Informe o desconto"))

totalSemDesconto = qtde * valorUnit
totalComDesconto = totalSemDesconto - (totalSemDesconto * desconto/100)

print(f'O total sem desconto será R$ {totalSemDesconto:.2f}')
print(f'O total com o desconto será R${totalComDesconto:.2f}')
