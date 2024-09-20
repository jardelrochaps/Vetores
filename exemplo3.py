num_alunos = 5
notas = []
nomes = []
media = 0
for i in range(num_alunos):
    nomes.append(input('Digite o nome do ' + str(i + 1) + 'º aluno: '))
    notas.append(float(input('Digite a nota do ' + str(i + 1) + 'º aluno: ')))
    media = media + notas[i]

media = media / num_alunos
print('A média da turma é: ', media)

for i in range(num_alunos):
    if notas[i] > media:
        print('Parabéns ',nomes[i]) 