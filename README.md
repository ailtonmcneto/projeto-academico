# 🎓 Dashboard Acadêmico

Sistema de gerenciamento acadêmico desenvolvido em Python, capaz de cadastrar cursos, disciplinas, professores e alunos, lançar e gerenciar notas, e emitir relatórios e certificados de conclusão.

---

## 📋 Funcionalidades

### Cadastros
- **Curso** — código gerado automaticamente e nome
- **Disciplina** — código gerado automaticamente, nome e vínculo com curso
- **Professor** — matrícula gerada automaticamente, nome, disciplina e curso
- **Aluno** — matrícula gerada automaticamente, nome e curso

### Notas
- Lançamento de notas por aluno e disciplina
- Cálculo automático de média e situação:
  - **Média ≥ 7.0** → Aprovado
  - **Média entre 4.0 e 6.9** → Sem nota suficiente (com opção de modificar)
  - **Média < 4.0** → Reprovado
- Modificação de notas quando o aluno está em situação de "Sem nota suficiente"
- Validação de notas: apenas valores entre 0 e 10 são aceitos

### Certificado
- Emitido automaticamente quando o aluno é aprovado em **10 ou mais disciplinas**
- Contém nome do aluno, curso e data de emissão

### Relatórios
- **Relatório Geral** — lista todos os cursos, disciplinas, professores e alunos cadastrados
- **Relatório Individual** — exibe todas as disciplinas cursadas por um aluno com notas, média e situação
- **Relatório por Curso** — exibe todos os alunos matriculados e disciplinas de cada curso

---

## 🚀 Como executar

### Pré-requisitos
- Python 3.6 ou superior

### Execução
```bash
python sistema_academico.py
```

### Menu principal
```
==============================
DASHBOARD ACADÊMICO
==============================

ESCOLHA UMA OPÇÃO:
1. Cadastrar curso
2. Cadastrar disciplina
3. Cadastrar professor
4. Cadastrar aluno
5. Lançar nota
6. Relatório geral
7. Relatório do aluno
8. Relatório do curso
0. Sair
```

---

## 🗂️ Estrutura dos dados

O sistema utiliza dicionários Python para armazenar os dados em memória durante a execução:

```python
curso = {}       # { "C1": { "nome": "Análise e Desenvolvimento" } }
disciplina = {}  # { "D1": { "nome": "Algoritmos", "curso": "C1" } }
professor = {}   # { "P1": { "nome": "Carlos", "disciplina": "D1", "curso": "C1" } }
aluno = {}       # { "A1": { "nome": "João Silva", "curso": "C1" } }
notas = {}       # { ("A1", "D1"): { "notas": [8.0, 7.0], "media": 7.5, "situacao": "Aprovado" } }
```

> ⚠️ Os dados não são persistidos entre execuções — ao fechar o programa, todas as informações são perdidas.

---

## 📁 Estrutura do projeto

```
sistema_academico.py   # arquivo principal com todo o código
README.md              # documentação do projeto
```

---

## 🔍 Exemplo de uso

**1. Cadastrar um curso:**
```
Digite o nome do curso: Análise e Desenvolvimento
Curso 'Análise e Desenvolvimento' cadastrado com o código C1!
```

**2. Lançar uma nota:**
```
Digite a matrícula do aluno: A1
Digite o código da disciplina: D1
Digite a nota do aluno: 8.5
8.50 - Aprovado para o aluno João Silva na disciplina Algoritmos.
```

**3. Certificado emitido automaticamente:**
```
CERTIFICADO DE CONCLUSÃO DE CURSO
Certificamos que João Silva concluiu com êxito o curso de Análise e Desenvolvimento. Data de emissão: 2026-06-10
```

---

## 🛠️ Tecnologias utilizadas

- **Python 3** — linguagem principal
- **datetime** — para data de emissão do certificado
- **time** — para pausas de usabilidade no terminal

---

## 👨‍💻 Autor

Desenvolvido como projeto acadêmico para a disciplina de introdução à programação.
