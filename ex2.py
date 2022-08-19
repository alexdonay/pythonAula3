import os
clear = lambda: os.system('cls')



alunos ={}
total = 0
clear()
for i in range(0,3):
    
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a nota: "))
    alunos[nome] = [nota1]
    clear()

for campo, valor in alunos.items():
    total += (valor[0])
clear()

print(f'A média dos alunos é {total/len(alunos)}')