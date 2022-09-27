# Käytetty .reverse() metodia
k = input('anna lukuja: ').split(',')
k.reverse()
print(k)

# Vaihtoehtoinen ratkaisu
x = input('anna lukuja: ').split(',')[::-1]
print(x)

# Onelinerit on villejä...

print(input('anna lukuja: ').split(',')[::-1])