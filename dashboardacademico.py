from time import sleep

#dicionários de cada área
curso = {}
disciplina = {}
professor = {}
aluno = {}
notas = {}


#-----funções------#
def cadastrar_curso():
    #gerador de chave automática
    codigo = "C" + str(len(curso) + 1)
    nome = input('Digite o nome do curso: ')
    curso[codigo] = {'nome': nome}
    print(f"Curso '{nome}' cadastrado com o código {codigo}!")

def cadastrar_disciplina():
    if len(curso) == 0:
        print("Cadastre um curso primeiro!")
        return
    codigo_curso = input('Digite o código do curso: ').upper().strip()
    if codigo_curso not in curso:
        print("Curso não encontrado!")
        sleep(3)
        return
    #gerador de chave automática
    codigo = "D" + str(len(disciplina) + 1)
    nome = input('Digite o nome da disciplina: ')
    disciplina[codigo] = {'nome': nome, 'curso': codigo_curso}
    print(f"Disciplina '{nome}' cadastrada com o código {codigo}!")

def cadastrar_professor():
    if len(disciplina) == 0:
        print("Cadastre uma disciplina primeiro!")
        sleep(3)
        return
    #gerador de chave automática
    matricula = "P" + str(len(professor) + 1)
    nome = input('Digite o nome do professor: ')
    codigo_disciplina = input('Digite o código da disciplina: ').upper().strip()
    if codigo_disciplina not in disciplina:
        print("Disciplina não encontrada!")
        sleep(3)
        return
    codigo_curso = disciplina[codigo_disciplina]['curso']
    professor[matricula] = {'nome': nome, 'disciplina': codigo_disciplina, 'curso': codigo_curso}
    print(f"Professor '{nome}' cadastrado com a matrícula {matricula}!")

def cadastrar_aluno():
    if len(curso) == 0:
        print("Cadastre um curso primeiro!")
        sleep(3)
        return
    #gerador de chave automática
    matricula = "A" + str(len(aluno) + 1)
    nome = input('Digite o nome do aluno: ')
    codigo_curso = input('Digite o código do curso: ').upper().strip()
    if codigo_curso not in curso:
        print("Curso não encontrado!")
        sleep(3)
        return
    aluno[matricula] = {'nome': nome, 'curso': codigo_curso}
    print(f"Aluno '{nome}' cadastrado com a matrícula {matricula}!")

def cadastrar_nota():
    if len(aluno) == 0 or len(disciplina) == 0:
        print("Cadastre alunos e disciplinas primeiro!")
        sleep(3)
        return
    matricula_aluno = input('Digite a matrícula do aluno: ').upper().strip()
    if matricula_aluno not in aluno:
        print("Aluno não encontrado!")
        sleep(3)
        return
    codigo_disciplina = input('Digite o código da disciplina: ').upper().strip()
    if codigo_disciplina not in disciplina:
        print("Disciplina não encontrada!")
        sleep(3)
        return
    nota = float(input('Digite a nota do aluno: '))
    notas[(matricula_aluno, codigo_disciplina)] = nota
    print("Nota lançada com sucesso!")

while True:
    print('''
=== SISTEMA ACADÊMICO ===
1. Cadastrar curso
2. Cadastrar disciplina
3. Cadastrar professor
4. Cadastrar aluno
5. Lançar nota
0. Sair''')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        cadastrar_curso()
    elif opcao == 2:
        cadastrar_disciplina()
    elif opcao == 3:
        cadastrar_professor()
    elif opcao == 4:
        cadastrar_aluno()
    elif opcao == 5:
        cadastrar_nota()
    elif opcao == 0:
        break
print(curso)