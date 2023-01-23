''' 
Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$7,00 por cada Km acima do limite.
'''
carSpeed = float(input('Insert the speed of the car (Km/h): '))
if carSpeed >= 80:
    fine = float(carSpeed * 7)
    print('Sorry, you have been fined! You will have to pay R${:.2f}'.format(fine))
else:
    print('Very well, you are below the limit!')
