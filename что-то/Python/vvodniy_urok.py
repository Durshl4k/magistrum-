import random as r

print("🤡Do you wanna play with me that game?🤡")


while True:
    answer = input('da/net?')
    if answer == 'da':
        break
    elif answer == 'net':
        print('ну...ладно!')
        exit()
    else:
        print('А если подумать?')

min = int(input("Введите нижнюю границу:"))
max = int(input("Введите верхнюю границу:"))
run = True
num = r.randint(min, max)

player = 0
score = 0


while run:
    print("Введите число:")
    player = int(input())
    score += 1
    
    if player == num:
        print("Молодец! Ты выиграл!")
        break
    else:
        print("Ты не угадал!")
        
print("Ваше количество попыток =", score, '! ', 'теперь ты свободен!)' )