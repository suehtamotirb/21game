from random import randint
cartas = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
y = 'sim'
somaMao1 = 0
mao1 = []
contador = 0
mao2 = []
somaMao2 = 0
while somaMao1 <21 and y=='sim':
    x = randint(0,40 -contador)
    item = cartas.pop(x)
    mao1.append(item)
    print(mao1)
    somaMao1 = sum(mao1)
    print(somaMao1)
    contador = contador + 1 
    if somaMao1 < 21 and y =='sim':
        y = input("Deseja comprar uma nova carta ?\n")
    
while somaMao2 <18:
    x = randint(0,40 -contador)
    item = cartas.pop(x)
    mao2.append(item)
    somaMao2 = sum(mao2)
    print("Jogada do Computador", somaMao2)
    contador = contador +1

if somaMao1 <= 21 and somaMao1 > somaMao2:
    print('Você venceu!!')
elif somaMao1 <=21 and somaMao2 > 21:
    print('Você venceu')
elif somaMao2 <=21 and somaMao1 > 21:
    print('Você perdeu')
elif somaMao2 <= 21 and somaMao2 > somaMao1:
    print('Você perdeu!!')
else:
    print("Empate!!")
