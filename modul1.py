def lists (string):
    count = int(input("Введите кол-во элементов " + string + " списка: "))
    list1 = []
    for i in range(count):
        number = int(input())
        list1.append(number)
    print("Элементы " + string + " списка: ", list1)
    return list1