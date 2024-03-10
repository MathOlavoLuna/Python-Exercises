from time import sleep

hInicio = -1
hFinal = -1

while (hInicio > hFinal) or (hInicio < 0) or hInicio > 23 or hFinal < 0 or hFinal > 23:
    hInicio = int(input('Que horas deseja começar?: '))
    hFinal = int(input('Que horas deseja terminar?: '))

for h in range(hInicio, hFinal, 1):
    for m in range(0, 60, 1):
        for s in range(0, 60, 1):
            print(f'{h} : {m} : {s} hrs')