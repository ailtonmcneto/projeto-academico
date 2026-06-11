from time import sleep
from datetime import date
curso = {}
disciplina = {}
professor = {}
aluno = {}
notas = {}
media_notas = 0.0


def cadastrar_curso():

    codigo_curso = "C" + str(len(curso) + 1)
    nome = input('Digite o nome do curso: ').strip()
    
    curso[codigo_curso] = {'nome': nome}
    print(f"Curso '{nome}' cadastrado com o código {codigo_curso}!")

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
    
    codigo_disciplina = "D" + str(len(disciplina) + 1)

    nome = str(input('Digite o nome da disciplina: ')).strip()
    
    disciplina[codigo_disciplina] = {'nome': nome, 'curso': codigo_curso}
    print(f"Disciplina '{nome}' cadastrada com o código {codigo_disciplina}!")

def cadastrar_professor():
    
    if len(disciplina) == 0:
        print("Cadastre uma disciplina primeiro!")
        sleep(3)
        return
    
    matricula_professor = "P" + str(len(professor) + 1)
    
    nome = str(input('Digite o nome do professor: ')).strip()
   
    codigo_disciplina = input('Digite o código da disciplina: ').upper().strip()
    if codigo_disciplina not in disciplina:
            print("Disciplina não encontrada!")
            sleep(3)
            return
   
    codigo_curso = disciplina[codigo_disciplina]['curso']
    
    professor[matricula_professor] = {'nome': nome, 'disciplina': codigo_disciplina, 'curso': codigo_curso}
    print(f"Professor '{nome}' cadastrado com a matrícula {matricula_professor}!")

def cadastrar_aluno():
   
    if len(curso) == 0:
        print("Cadastre um curso primeiro!")
        sleep(3)
        return
  
    matricula_aluno = "A" + str(len(aluno) + 1)

    nome = str(input('Digite o nome do aluno: ')).strip()
  
    codigo_curso = input('Digite o código do curso: ').upper().strip()
    if codigo_curso not in curso:
        print("Curso não encontrado!")
        sleep(3)
        return
    
    aluno[matricula_aluno] = {'nome': nome, 'curso': codigo_curso}
    print(f"Aluno '{nome}' cadastrado com a matrícula {matricula_aluno}!")

def cadastrar_nota():
    while True:
        if len(aluno) == 0 or len(disciplina) == 0:
            print("Cadastre alunos e disciplinas primeiro!")
            sleep(3)
            break
    
        matricula_aluno = input('Digite a matrícula do aluno: ').upper().strip()
        if matricula_aluno not in aluno:
            print("Aluno não encontrado!")
            sleep(3)
            continue
        
        codigo_disciplina = input('Digite o código da disciplina: ').upper().strip()
        if codigo_disciplina not in disciplina:
            print("Disciplina não encontrada!")
            sleep(3)
            continue   
    
        try:
            nota = float(input('Digite a nota do aluno: '))
        except ValueError:
            print("Valor inválido. Digite uma nota válida.")
            continue
        if nota < 0 or nota > 10:
            print("Nota inválida. Digite um valor entre 0 e 10.")
            continue
    
        if (matricula_aluno, codigo_disciplina) not in notas:
            notas[(matricula_aluno, codigo_disciplina)] = {"notas": [] , "media": 0.0, "situacao": ""}
        
        notas[(matricula_aluno, codigo_disciplina)]["notas"].append(nota)
        
        lista_notas = notas[(matricula_aluno, codigo_disciplina)]["notas"]
        media_notas, situacao = calcular_situacao(lista_notas)

        notas[(matricula_aluno, codigo_disciplina)]["media"] = media_notas
        notas[(matricula_aluno, codigo_disciplina)]["situacao"] = situacao
    
        print(f"{media_notas:.2f} - {situacao} para o aluno {aluno[matricula_aluno]['nome']} na disciplina {disciplina[codigo_disciplina]['nome']}.")
        if situacao == "Sem nota suficiente":
            modificacao_nota = input("O Aluno {} está em situação de Sem nota suficiente. desejaria modificar alguma nota? (s/n): ".format(aluno[matricula_aluno]['nome'])).lower().strip()
            if modificacao_nota == 's':
                modificar_nota(matricula_aluno, codigo_disciplina, lista_notas, media_notas)

        verificar_situacao_curso(matricula_aluno)

        resposta = input("Deseja lançar outra nota? (s/n): ").lower().strip()
        if resposta == 's':
            continue
        elif resposta == 'n':
            break
        else:
            print("Resposta inválida. Digite 's' para sim ou 'n' para não.")

def calcular_situacao(lista_notas):
    
    media_notas = sum(lista_notas) / len(lista_notas)
    if media_notas >= 7.0:
        situacao = "Aprovado"
    elif media_notas >= 4.0:
        situacao = "Sem nota suficiente"
    else:
        situacao = "Reprovado"
    return media_notas, situacao


def verificar_situacao_curso(matricula_aluno):
    reprovado_em = []
    aprovado_em = []
    for (mat, cod_disc), dados in notas.items():
        if mat == matricula_aluno:
            nome_disc = disciplina[cod_disc]['nome']
            if dados.get("situacao") == "Reprovado":
                reprovado_em.append(nome_disc)
            elif dados.get("situacao") == "Aprovado":
                aprovado_em.append(nome_disc)
    if len(reprovado_em) > 0: 
        print("O aluno {} está reprovado nas seguintes disciplinas: {}".format(aluno[matricula_aluno]['nome'], ", ".join(reprovado_em)))
    if len(aprovado_em) >= 10:
        print("O aluno {} está aprovado no curso e aqui está o certificado: ".format(aluno[matricula_aluno]['nome']))
        print("CERTIFICADO DE CONCLUSÃO DE CURSO")
        print("Certificamos que {} concluiu com êxito o curso de {}. Data de emissão: {}".format(aluno[matricula_aluno]['nome'], curso[aluno[matricula_aluno]['curso']]['nome'], date.today()))
    

def modificar_nota(matricula_aluno, codigo_disciplina, lista_notas, media_notas):
    print("Notas atuais do aluno {} na disciplina {}: {}".format(aluno[matricula_aluno]['nome'], disciplina[codigo_disciplina]['nome'], lista_notas))
    while True:
        try:
            indice_nota = int(input("Digite o número da nota que deseja modificar (1, 2, ...): ")) - 1
            if indice_nota < 0 or indice_nota >= len(lista_notas):
                print("Índice de nota inválido.")
                return
            nova_nota = float(input("Digite a nova nota: "))
            lista_notas[indice_nota] = nova_nota
            media_notas, situacao = calcular_situacao(lista_notas)
            notas[(matricula_aluno, codigo_disciplina)]["media"] = media_notas
            notas[(matricula_aluno, codigo_disciplina)]["situacao"] = situacao
            print(f"Nota modificada. Nova média: {media_notas:.2f} - Situação: {situacao}.")
            if situacao == "Sem nota suficiente":
                resposta = input(f"O aluno {aluno[matricula_aluno]['nome']} ainda está sem nota suficiente. Deseja modificar outra nota? (s/n): ").lower().strip()
                if resposta == 's':
                    continue
                elif resposta == 'n':
                    break
                else:
                    break
            if situacao == "Aprovado":
                print("Aluno aprovado. Não é possível modificar mais notas.")
                break
            elif situacao == "Reprovado":                
                print("Aluno reprovado. Não é possível modificar mais notas.")
                break
        except ValueError:
            print("Valor inválido. Digite um número válido.")

def relatorio_geral():
    print("="*30)
    print("RELATÓRIO GERAL:")
    print("="*30) 
    print(f"""
    CURSOS CADASTRADOS: 
""")
    if len(curso) == 0:
        print("  Nenhum curso cadastrado.")
    else:
        for codigo in curso:
            print(f"  {codigo} - {curso[codigo]['nome']}")

    print(f"""DISCIPLINAS CADASTRADAS: """)
    if len(disciplina) == 0:
        print("  Nenhuma disciplina cadastrada.")
    else:
        for codigo_disciplina in disciplina:
            print(f"  {codigo_disciplina} - {disciplina[codigo_disciplina]['nome']}")

    print(f"""PROFESSORES CADASTRADOS: """)
    if len(professor) == 0:
        print("  Nenhum professor cadastrado.")
    else:
        for matricula_professor in professor:
            print(f"  {matricula_professor} - {professor[matricula_professor]['nome']}")
    print(f"""ALUNOS CADASTRADOS: """)
    if len(aluno) == 0:
        print("  Nenhum aluno cadastrado.")
    else:
        for matricula_aluno in aluno:
            print(f"  {matricula_aluno} - {aluno[matricula_aluno]['nome']}")
    sleep(4)

def relatorio_aluno():
    matricula_aluno = input("Digite a matrícula do aluno: ").upper().strip()
    if matricula_aluno not in aluno:
        print("Matrícula não encontrada.")
        sleep(3)
        return
    
    print("="*30)
    print(f"RELATÓRIO DO ALUNO: {aluno[matricula_aluno]['nome']}")
    print(f"Curso: {curso[aluno[matricula_aluno]['curso']]['nome']}")
    print("="*30)
    
    encontrou_disciplina = False
    for (matricula, codigo_disciplina), valores in notas.items():
        if matricula == matricula_aluno:
            encontrou_disciplina = True
            print(f"  Disciplina: {disciplina[codigo_disciplina]['nome']}")
            print(f"  Notas: {', '.join(str(n) for n in valores['notas'])}")
            print(f"  Média: {valores['media']:.2f}")
            print(f"  Situação: {valores['situacao']}")
            print("-"*30)
    
    if not encontrou_disciplina:
        print("  Nenhuma nota lançada ainda.")   

def relatorio_curso():
    print(f"""CURSOS CADASTRADOS: """)
    for codigo_curso in curso:
        print(f"  CURSO: - {curso[codigo_curso]['nome']}")

        print("  Alunos matriculados:")
        encontrou_alunos = False
        for matricula_aluno in aluno:
            if aluno[matricula_aluno]['curso'] == codigo_curso:
                print(f"- {aluno[matricula_aluno]['nome']}")
                encontrou_alunos = True
        if not encontrou_alunos:
            print("  Nenhum aluno matriculado neste curso.")

        print("  Disciplinas do curso:")
        encontrou_disciplinas = False
        for codigo_disciplina in disciplina:
            if disciplina[codigo_disciplina]['curso'] == codigo_curso:
                print(f"- {disciplina[codigo_disciplina]['nome']}")
                encontrou_disciplinas = True
        if not encontrou_disciplinas:
            print("  Nenhuma disciplina cadastrada para este curso.")
                                 

while True:

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
6. Relatório geral
7. Relatório do aluno
8. Relatório do curso
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
    elif opcao == 6:
        relatorio_geral()
    elif opcao == 7:
        relatorio_aluno()
    elif opcao == 8:
        relatorio_curso()
    elif opcao == 0:
        break

