sana = input('sana: ')

viimeinen = sana[-1]

if viimeinen == 'a':
    print('viimeisenä aakkosten ensimmäinen kirjain!')
elif viimeinen == 'ö':
    print('viimeisenä aakkosten viimeinen kirjain!')
else:
    print(f"sanasi loppuu kirjaimeen {viimeinen}")
