fat = 1
cont = 1
for cont in range (1,11):
    if cont % 2 == 1:
        for cont1 in range (1,cont):
            fat = fat * cont1
            print("A fatorial do número",cont,"é",fat)