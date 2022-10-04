# Tehtävä 4. Pyydä käyttäjältä muutamia sanoja. Jos sana ‘koira’ on syötettyjen sanojen joukossa, tulosta teksti ‘koira löydetty <n> sanan 
# joukosta’. Jos sanaa ‘koira’ ei löydy, tulosta ‘<n> sanaa ja yksikään niistä ei ole koira’. Korvaa <n> syötettyjen sanojen määrällä.

sanoja = []

k_sanoja = ''

while len(sanoja) <= 19 and k_sanoja != 'koira':
    k_sanoja = input('Anna sana: ')

    if k_sanoja != 'koira':
        sanoja.append(k_sanoja)        

if k_sanoja == 'koira':
    print(f'koira löydetty {len(sanoja)} sanan joukosta')
else:
    print(f'{len(sanoja)} sanaa ja yksikään ei ollut koira')
