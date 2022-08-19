list = []

for i in range(0, 10):
    list.append(int(input("Digite um número: ")))

##ordenação

def order(list):
    while True:
        for i in range(0, len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                break
        else:
            break
    return list
    
print(order(list))
        