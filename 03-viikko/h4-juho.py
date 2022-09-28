sanat = []

sanat.append(input('anna sana: '))
sanat.append(input('anna sana: '))
sanat.append(input('anna sana: '))

if 'koira' in sanat:
    print(f"koira löydetty {len(sanat)} sanan joukosta")
else:
    print(f"{len(sanat)} sanaa ja yksikään niistä ei ole koira")
