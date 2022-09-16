from random import choice
c = 0
alunos = list()
for c in range(1,5):
    nome = str(input(f'{c}° Aluno: '))
    c += 1
    alunos.append(nome)
print(f'O aluno(a) escolhido(a) foi {choice(alunos)}.')
