# -*- coding: utf-8 -*-
import time, random, os
from readchar import readchar
from collections import Counter

n = 0
correct = True
breakvar = False
progress = 0
astyped = ''
m = []



os.system('clear')

print('Svårighetsgrad?')
print('1: lätt')
print('2: medel')
print('3: svår')
diffn = input()
if diffn == '1':
    diff = 'lätt'
elif diffn == '2':
    diff = 'medel'
elif diffn == '3':
    diff = 'svår'
else:
    print('Det där är inte en giltig siffra. Det blir automatiskt en svår nu')
    diff = 'svår'

os.system('clear')

textfiles = os.listdir(f'texts/{diff}')

print('Textval:')
for i in textfiles:
    print(i)



choice = input('(enter för slumpmässig text): \n\n')
if choice == '':
    text = open(f'texts/{diff}/{textfiles[random.randint(0,len(textfiles)-1)]}', 'r').read()
else:
    try:
        text = open(f'texts/{diff}/{choice}', 'r').read()
    except:
        print('Den texten finns inte. Här kommer en slumpmässig text')
        text = open(f'texts/{diff}/{textfiles[random.randint(0,len(textfiles)-1)]}', 'r').read()

words = text.split(' ')

for i in range(len(words)-1): #tried to remove strange char at end
    words[i] = words[i] + ' '

words[-1] = words[-1][:-1] #still some strange char at end

input('Tryck enter för att starta')
os.system('clear')
t0 = time.time()
print(text)
print('Tryck ctrl-S för att stanna')
for i in words:
    correct = True
    for a in range(len(i)):
        s = readchar()
        if s == i[a]:
            os.system('clear')
            astyped += f'\033[42m{s}\033[00m'
        elif s == '\x13':
            breakvar = True
            correct = False
            break
        else:
            os.system('clear')
            astyped += f'\033[41m{s}\033[00m'
            correct = False

        progress += 1
        print(astyped, end='')
        print(text[progress:])
        print('Tryck ctrl-S för att stanna')
    if correct == True:
        n += 1
    else:
        m.append(i)
    if breakvar == True:
        break

t = (time.time()-t0)/60
score = round(n/t,1)

hs = eval(open('highscores', 'r').read())

try:
    hs[choice]
except:
    hs[choice] = 0

os.system('clear')

if score > hs[choice]:
    print('\033[42mNY HIGHSCORE\033[00m')
    hs[choice] = score
    with open('highscores', 'w') as file:
        file.write(str(hs))

print(f'Hastighet: {score} ord per minut')
print(f'Tidigare bästa tid: {hs[choice]} ord per minut')
print(f'{len(m)} missade ord: ')
m = Counter(m)
keys = [*m.keys()]
values = [*m.values()]

for i in range(len(keys)):
    print(f'{keys[i]}- {values[i]}')
