def func(numbers, devider=2):
    numbers2 = []
    for i in range(len(numbers)):
        if numbers[i] % devider == 0:
            numbers2.append(numbers[i])
    print(numbers2)

func([2,3,4,5,6,7,8,9],3)