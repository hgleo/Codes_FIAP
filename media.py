# Definindo a struct Aluno
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

# Função para receber as notas dos alunos
def receber_notas(num_alunos):
    alunos = []
    for i in range(num_alunos):
        nome = input("Digite o nome do aluno {}: ".format(i+1))
        nota = float(input("Digite a nota do aluno {}: ".format(i+1)))
        aluno = Aluno(nome, nota)
        alunos.append(aluno)
    return alunos

# Função para verificar quem foi aprovado
def verificar_aprovacao(alunos, nota_minima):
    aprovados = []
    for aluno in alunos:
        if aluno.nota >= nota_minima:
            aprovados.append(aluno)
    return aprovados

# Recebendo as notas dos alunos
num_alunos = int(input("Digite o número de alunos: "))
alunos = receber_notas(num_alunos)

# Verificando quem foi aprovado
nota_minima = 6.0
aprovados = verificar_aprovacao(alunos, nota_minima)

# Imprimindo os resultados
print("\nLista de alunos aprovados:")
for aluno in aprovados:
    print("Nome: {}, Nota: {}".format(aluno.nome, aluno.nota))
