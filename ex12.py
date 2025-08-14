import random

lista = ('\33[35mMaria\33[m'
         , '\33[31mJoão\33[m' 
         , '\33[34mMarcos\33[m' 
         , '\33[33mKelly\33[m')

quem = random.choice(lista)

print('Quem vai pegar o coco do nick é {} ' .format(quem))