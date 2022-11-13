import time
import random as r

print("Привет! Введите верхнюю границу")
max= int(input())
print("Загадываю целое число 0 до ", max )
time.sleep(1)
X = r.randint(0,max)
total = 0
print("Число загадано, человек!")
print("Игра началась")

i = True
while i:
  player_nomber = int(X)
  print(X)
  time.sleep(1)
  total +=1
  if player_nomber == X:
    print("В точку! Число:",X,"Попыток:", total)
    time.sleep(1)
    if total > 10:
      print("Тренируйся больше")
    elif 5<total<10 :
      print("Хороший результат")
    elif 1<total <5:
      print("Супер результат")
    elif total==1:
      print("Вай красавецъ!!!!!")  
    i = False
  elif player_nomber < 0 or player_nomber > max:
    print("Ай ай за границы не вылезай!") 
  elif player_nomber > X:
    print("Много")
    time.sleep(2)
  elif player_nomber < X:
    print("Мало")
    time.sleep(2)