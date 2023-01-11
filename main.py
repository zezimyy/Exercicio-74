from time import sleep
import random

numero = (random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10))

print("Os valores estão sendo sorteados.")
print()
sleep(3)
print("O sorteio acabou, resultado: {}".format(numero))
print()
sleep(3)
print("o maior valor sorteado foi: {}".format(max(numero)))
print("O menor valor sorteado foi: {}".format(min(numero)))