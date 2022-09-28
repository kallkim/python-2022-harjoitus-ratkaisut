numerot = []

while True:
    syote = input('numero: ')
    if syote == 'lopeta':
        break
    numerot.append(int(syote))

if len(numerot) > 0:
    print(sum(numerot) / len(numerot))
