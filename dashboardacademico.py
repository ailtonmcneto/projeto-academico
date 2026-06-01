from time import sleep

#dicionários de cada área
curso = {}
disciplina = {}
professor = {}
aluno = {}
notas = {}
media_notas = 0.0


def cadastrar_curso():

    codigo = "C" + str(len(curso) + 1)
    nome = input('Digite o nome do curso: ')
    
    curso[codigo] = {'nome': nome}
    print(f"Curso '{nome}' cadastrado com o código {codigo}!")

def cadastrar_disciplina():
    
    if len(curso) == 0:
        print("Cadastre um curso primeiro!")
        sleep(3)
        return
    
    codigo_curso = input('Digite o código do curso: ').upper().strip()
    if codigo_curso not in curso:
        print("Curso não encontrado!")
        sleep(3)
        return
    
    codigo = "D" + str(len(disciplina) + 1)
   

    nome = str(input('Digite o nome da disciplina: '))
    
    disciplina[codigo] = {'nome': nome, 'curso': codigo_curso}
    print(f"Disciplina '{nome}' cadastrada com o código {codigo}!")

def cadastrar_professor():
    
    if len(disciplina) == 0:
        print("Cadastre uma disciplina primeiro!")
        sleep(3)
        return
    
    matricula = "P" + str(len(professor) + 1)
    
    nome = str(input('Digite o nome do professor: '))
   
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
  
    matricula = "A" + str(len(aluno) + 1)

  
    nome = str(input('Digite o nome do aluno: '))
  
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
   
    try:
        nota = float(input('Digite a nota do aluno: '))
    except ValueError:
        print("Valor inválido. Digite uma nota válida.")
        return
   
   
    if (matricula_aluno, codigo_disciplina) not in notas:
        notas[(matricula_aluno, codigo_disciplina)] = {"notas": [] , "media": 0.0, "situacao": situacao}
    
    notas[(matricula_aluno, codigo_disciplina)]["notas"].append(nota)
    
    lista_notas = notas[(matricula_aluno, codigo_disciplina)]["notas"]
    media_notas, situacao = calcular_situacao(lista_notas)

    print(f"{media_notas:.2f} - {situacao} para o aluno {aluno[matricula_aluno]['nome']} na disciplina {disciplina[codigo_disciplina]['nome']}.")
    if situacao == "Final":
        modificacao_nota = input("O Aluno {} está em situação de Final. desejaria modificar alguma nota? (s/n): ".format(aluno[matricula_aluno]['nome']))
        if modificacao_nota == 's':
            modificar_nota()

    while True:
        resposta = input("Deseja lançar outra nota? (s/n): ").lower().strip()
        if resposta == 's':
            cadastrar_nota()
            break
        elif resposta == 'n':
            break
        else:
            print("Resposta inválida. Digite 's' para sim ou 'n' para não.")

def calcular_situacao(lista_notas):
    
    media_notas = sum(lista_notas) / len(lista_notas)
    if media_notas >= 7.0:
        situacao = "Aprovado"
    elif media_notas >= 4.0:
        situacao = "Final"
    else:
        situacao = "Reprovado"
    return media_notas, situacao

while True:
#loop presente com o menu de opções para o usuário
    print("="*30)
    print("DASHBOARD ACADÊMICO")
    print("="*30)   
    print('''
ESCOLHA UMA OPÇÃO:
1. Cadastrar curso
2. Cadastrar disciplinaz
3. Cadastrar professor
4. Cadastrar aluno
5. Lançar nota
0. Sair''')

    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")
        sleep(3)
        continue

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
print(disciplina)
print(professor)
print(aluno)
print(notas)
print(notas.keys())