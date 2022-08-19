aluno ={}

aluno['Nome'] = input("Digite o nome do aluno: ")
aluno['Curso'] = input("Digite o curso: ")
aluno['Email'] = input("Digite o email: ")
aluno['Telefone'] = input("Digite o telefone: ")
aluno['Rgm'] = input("Digite o Rgm: ")

for campo, valor in aluno.items():
    print(f'{campo}:{valor}')
    