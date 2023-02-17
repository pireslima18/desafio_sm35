#definindo a variavel que vai conter o resultado da soma
soma_multiplos = 0

#Começamos com um laço de repetição "for num in range(1, 1000)" que vai de um até 999.
#Logo em seguida entramos com condicional "if(num % 3 == 0 or num % 5 == 0)" que vai vericar quais números são múltiplos de 3 e 5
#Após a verificação, a soma dos múltiplos é registrada na variável "soma_multiplos"
#A soma de todos os números múltiplos de 3 é: 166833
#A soma de todos os números múltiplos de 5 é: 99500
#Porém , como alguns números podem ser múltiplos de 3 e 5, eles são somados apenas uma vez
#O resultado final é: 233168

for num in range(1, 1000):
    if( num % 3 == 0 or num % 5 == 0):
        soma_multiplos += num
print(soma_multiplos)
