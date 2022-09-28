numerot = []

while True:
    syote = input('numero: ')
    if syote == 'lopeta':
        break
    numerot.append(float(syote))

if len(numerot) > 0:
    print(f"max: {max(numerot)}, min: {min(numerot)}")
