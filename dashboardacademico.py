from time import sleep

#dicionários de cada área
curso = {}
disciplina = {}
professor = {}
aluno = {}
notas = {}
media_notas = 0.0

#-----funções------#
def cadastrar_curso():
    #gerador de chave automática
    codigo = "C" + str(len(curso) + 1)
    nome = input('Digite o nome do curso: ')
    #cadastro do curso no dicionario, utilizando o codigo gerado acima como chave e o nome do curso como valor
    curso[codigo] = {'nome': nome}
    print(f"Curso '{nome}' cadastrado com o código {codigo}!")

def cadastrar_disciplina():
    #verificação se existe curso cadastrado, caso contrário, não é possível cadastrar disciplina
    if len(curso) == 0:
        print("Cadastre um curso primeiro!")
        sleep(3)
        return
    #pede o código do curso para associar a disciplina, verificando se o código existe no dicionário de cursos
    codigo_curso = input('Digite o código do curso: ').upper().strip()
    if codigo_curso not in curso:
        print("Curso não encontrado!")
        sleep(3)
        return
    #gerador de chave automática
    codigo = "D" + str(len(disciplina) + 1)
    #pede o nome da disciplina, verificando se o valor é válido
    try:
        nome = str(input('Digite o nome da disciplina: '))
    except ValueError:
        print("Valor inválido. Digite um nome válido.")
    #cadastro da disciplina, utilizando o codigo gerado acima como chave e o nome da disciplina como valor, alem de usar o código do curso para associar a disciplina ao curso,
    #utilizando o código do curso como valor para a chave curso dentro da discplina, associando a disciplina ao curso
    disciplina[codigo] = {'nome': nome, 'curso': codigo_curso}
    print(f"Disciplina '{nome}' cadastrada com o código {codigo}!")

def cadastrar_professor():
    #verificação se existe disciplina cadastrada, caso contrário, não é possível cadastrar professor
    if len(disciplina) == 0:
        print("Cadastre uma disciplina primeiro!")
        sleep(3)
        return
    #gerador de chave automática
    matricula = "P" + str(len(professor) + 1)
    #pede o nome do professor, verificando se o valor é válido
    nome = str(input('Digite o nome do professor: '))
    #pede o código da disciplina para linkar o professor a disciplina, verificando se o código existe no dicionário de disciplinas
    codigo_disciplina = input('Digite o código da disciplina: ').upper().strip()
    if codigo_disciplina not in disciplina:
            print("Disciplina não encontrada!")
            sleep(3)
            return
    #nao entendi o esse codigo_curso = disciplina[codigo_disciplina]['curso'] 
    codigo_curso = disciplina[codigo_disciplina]['curso']
    #cadastro do professor, utlizando a matricula gerada acima como chave para o dicionario do professor, e utilziando o nome, o código da disciplina e o código do curso como valor, associando o professor a disciplina e ao curso
    professor[matricula] = {'nome': nome, 'disciplina': codigo_disciplina, 'curso': codigo_curso}
    print(f"Professor '{nome}' cadastrado com a matrícula {matricula}!")

def cadastrar_aluno():
    #verificação se existe curso cadastrado, caso contrário, não é possível cadastrar aluno
    if len(curso) == 0:
        print("Cadastre um curso primeiro!")
        sleep(3)
        return
    #gerador de chave automática
    matricula = "A" + str(len(aluno) + 1)
    #pede o nome do aluno, verificando se o valor é válido
    try:
        nome = str(input('Digite o nome do aluno: '))
    except ValueError:
        print("Valor inválido. Digite um nome válido.")
    #pede o código do curso para associar o aluno ao curso, verificando se o código existe no dicionário de cursos
    codigo_curso = input('Digite o código do curso: ').upper().strip()
    if codigo_curso not in curso:
        print("Curso não encontrado!")
        sleep(3)
        return
    #cadastro do aluno, usando a matricula gerada acima como chave para cadastrar no dicionario do aluno, e usando o nome dele e o codigo do curso como valor para associar o aluno ao curso
    aluno[matricula] = {'nome': nome, 'curso': codigo_curso}
    print(f"Aluno '{nome}' cadastrado com a matrícula {matricula}!")

def cadastrar_nota():
    #verificação se existe aluno e disciplina cadastrados, caso contrário, não é possível cadastrar nota
    if len(aluno) == 0 or len(disciplina) == 0:
        print("Cadastre alunos e disciplinas primeiro!")
        sleep(3)
        return
    #pede a matrícula do aluno para associar a nota ao aluno, verificando se a matrícula existe no dicionário de alunos
    matricula_aluno = input('Digite a matrícula do aluno: ').upper().strip()
    if matricula_aluno not in aluno:
        print("Aluno não encontrado!")
        sleep(3)
        return
    #pede o código da disciplina para associar a nota à disciplina, verificando se o código existe no dicionário de disciplinas
    codigo_disciplina = input('Digite o código da disciplina: ').upper().strip()
    if codigo_disciplina not in disciplina:
        print("Disciplina não encontrada!")
        sleep(3)
        return
    #pede a nota do aluno, verificando se o valor é válido e convertendo para float, caso contrário, exibe uma mensagem de erro e retorna para o menu principal
    try:
        nota = float(input('Digite a nota do aluno: '))
    except ValueError:
        print("Valor inválido. Digite uma nota válida.")
        return
    #cadastro das notas, usando a matricula do aluno e o código da disciplina como chave para o dicionário de notas, e usando a nota como valor, associando a nota ao aluno e à disciplina
    notas[(matricula_aluno, codigo_disciplina)] = nota
    #calculo da media das notas e verificação se o aluno foi aprovado direto, se está de final ou está reprovado
    media_notas = sum(notas.values()) / len(notas)  
    print("Nota lançada com sucesso!")
    #input para saber se o usuário deseja lançar outra nota, caso contrário, retorna para o menu principal
    while True:
        resposta = input("Deseja lançar outra nota? (s/n): ").lower().strip()
        if resposta == 's':
            cadastrar_nota()
            break
        elif resposta == 'n':
            break
        else:
            print("Resposta inválida. Digite 's' para sim ou 'n' para não.")
while True:
#loop presente com o menu de opções para o usuário
    print("="*30)
    print("DASHBOARD ACADÊMICO")
    print("="*30)   
    print('''
ESCOLHA UMA OPÇÃO:
1. Cadastrar curso
2. Cadastrar disciplina
3. Cadastrar professor
4. Cadastrar aluno
5. Lançar nota
0. Sair''')
#escolha do usuário, verificando se o valor é um número inteiro, caso contrário, exibe uma mensagem de erro e retorna para o menu principal
    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")
        sleep(3)
        continue
    #baseado na escolha do usuário, chama a função correspondente para realizar a ação desejada, ou sai do programa caso a opção seja 0
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
