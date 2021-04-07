'''
author = Jan Richter
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]


OODELOVAC = 40 * '-'
LOGIN = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

print(OODELOVAC)

# I. KROK

print('Welcome to the app. Please log in:')

# II. KROK

pocitadlo1 = 0
while pocitadlo1 < 3:
    username = input('USERNAME: ')
    password = input('PASSWORD: ')

    # III. KROK
    if LOGIN.get(username) != password:
        print('You have chosen wrong username or password.')
        pocitadlo1 += 1

        if pocitadlo1 == 3:
            print('The program will close itself now.')
            quit()

    else:
        break

print(OODELOVAC)
print('We have 3 texts to be analyzed.')

# IV. KROK
pocitadlo2 = 0
while pocitadlo2 < 3:
    choice = input('Enter a number btw. 1 and 3 to select: ')

    if choice not in ('1', '2', '3'):
        print('You have not followed rules above.')
        pocitadlo2 += 1

        if pocitadlo2 == '3':
            print('The program will close itself now.')
            quit()

    else:
        choice = int(choice) - 1
        break

print(OODELOVAC)

# V. KROK

odstavec = TEXTS[choice].split()

total_words = len(odstavec)
titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0

while odstavec:
    wordcheck = odstavec.pop(0)
    if wordcheck.istitle():
        titlecase += 1
    elif wordcheck.isupper():
        uppercase += 1
    elif wordcheck.islower():
        lowercase += 1
    elif wordcheck.isnumeric():
        numeric += 1

print('There are', total_words, 'words in the selected text.')
print('There are', titlecase, 'titlecase words.')
print('There are', uppercase, 'uppercase words.')
print('There are', lowercase, 'lowercase words.')
print('There are', numeric, 'numeric strings.')
print(OODELOVAC)

# VI. KROK

#choice = 1
odstavec2 = TEXTS[choice].split()
pouzita_slova = {}
x = 0

while odstavec2:
    wordcheck = odstavec2.pop()
    wordcheck = wordcheck.strip(',.!?')
    pouzita_slova[len(wordcheck)] = pouzita_slova.get(len(wordcheck), 0) + 1

for i in sorted(pouzita_slova):
    print(i, pouzita_slova[i] * '*', pouzita_slova[i])

print(OODELOVAC)

# VII. KROK

odstavec3 = TEXTS[choice].split()
suma = 0

while odstavec3:
    wordcheck = odstavec3.pop(0)

    if wordcheck.isnumeric():
        suma = suma + int(wordcheck)

print('If we summed all the numbers in this text we would get:', float(suma))
print(OODELOVAC)


