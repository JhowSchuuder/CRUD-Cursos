from datetime import date
import os


class Aluno:
    nome = ""
    cpf = ""
    dtNasc = [0, 0, 0]
    sexo = ""
    email = ""
    telefone = ""

class Curso:
    codigo = ""
    nome = ""
    cargaHoraria = 0.0
    preco = 0.0

class Matricula:
    cpfAluno = ""
    codigoCurso = ""
    dataInicio = [0, 0, 0]
    dataFim = [0, 0, 0]
    desconto = 0.0

#-------------------------------------------------------------------------------------------------------------------------------------

#funcao verifica se arquivo existe
def existe_arquivo(nome_arquivo):
    if os.path.exists(nome_arquivo):
          return True
    else:
          return False

#funcao menu de categorias
def menu():
    print("**********************")
    print("Alunos...............1")
    print("Cursos...............2")
    print("Matriculas...........3")
    print("Relatorios...........4")
    print("Sair.................0")
    opcao = input("-> ")
    return opcao

#funcao menu de acoes
def menu_fazer():
    print("**********************")
    print("Inserir..............1")
    print("Listar um............2")
    print("Listar todos.........3")
    print("Alterar..............4")
    print("Excluir..............5")
    print("Sair.................0")
    fazer = input("-> ")
    return fazer

#funcao menu de relatorios
def menu_relatorio():
    print("**********************")
    print("Funcao a.............1")
    print("Funcao b.............2")
    print("Funcao c.............3")
    print("Sair.................0")
    fazer = input("-> ")
    return fazer
#-------------------------------------------------------------------------------------------------------------------------------------

#funcoes para area de alunos

#funcao para inserir um aluno
def inserir_aluno():
    print("Menu Inserir Aluno")
    a = Aluno()
    a.nome = input("Informe o nome do aluno: ")
    a.cpf = verificar_cpf()
    print("Padrao de data: AAAA-MM-DD")
    componentes_data = input("Informe a data de nascimento: ").split("-")
    a.dtNasc = date(int(componentes_data[0]), int(componentes_data[1]), int(componentes_data[2]))
    a.sexo = input("Informe o sexo(F/M): ")
    a.email = input("Informe o email: ")
    a.telefone = input("Informe o telefone: ")
    arq = open("Alunos.txt","a")
    arq.write(a.nome + " | " + a.cpf + " | " + str(a.dtNasc) + " | " + a.sexo + " | " + a.email + " | " + a.telefone + "\n")
    arq.close()
    print("Aluno inserido com sucesso!")

#funcao para verificar cpf
def verificar_cpf():
    cpf = input("Informe o cpf do aluno: ")
    if len(cpf) == 11:
        if existe_arquivo("Alunos.txt"):
            arq = open("Alunos.txt","r")
            for linha in arq:
                if linha.find(cpf) != -1:
                    print("CPF já cadastrado!")
                    cpf = verificar_cpf()
            arq.close()
    else:
        print("CPF inválido!")
        cpf = verificar_cpf()
    return cpf    

#funcao que imprime os dados de um aluno na tela
def imprimir_aluno(a):
  print("Nome: ", a.nome, " | CPF: ", a.cpf, " | Data nasc: ", str(a.dtNasc), " | Sexo: ", a.sexo, " | Email: ", a.email, " | Telefone: ", a.telefone)

#funcao para buscar um aluno pelo cpf
def listar_1_aluno():
    print("Menu Listar 1 Aluno")
    if existe_arquivo("Alunos.txt"):
        arq = open("Alunos.txt","r")
        cpf = input("Informe o cpf do aluno: ")
        for linha in arq:
            if linha.find(cpf) != -1:
                a = Aluno()
                componentes = linha.split(" | ")
                a.nome = componentes[0]
                a.cpf = componentes[1]
                componentes_data = componentes[2].split("-")
                a.dtNasc = date(int(componentes_data[0]), int(componentes_data[1]), int(componentes_data[2]))
                a.sexo = componentes[3]
                a.email = componentes[4]
                a.telefone = componentes[5]
                imprimir_aluno(a)
        arq.close()
    else:
        print("Não há alunos cadastrados!")
    
#funcao para buscar todos os alunos
def listar_todos_aluno():
    print("Menu Listar Todos Alunos")
    if existe_arquivo("Alunos.txt"):
        arq = open("Alunos.txt","r")
        for linha in arq:
            a = Aluno()
            componentes = linha.split(" | ")
            a.nome = componentes[0]
            a.cpf = componentes[1]
            componentes_data = componentes[2].split("-")
            a.dtNasc = date(int(componentes_data[0]), int(componentes_data[1]), int(componentes_data[2]))
            a.sexo = componentes[3]
            a.email = componentes[4]
            a.telefone = componentes[5]
            imprimir_aluno(a)
        arq.close()
    else:
        print("Não há alunos cadastrados!")
    
#funcao para alterar os dados de um aluno
def alterar_aluno():
    print("Menu Alterar Aluno")
    if existe_arquivo("Alunos.txt"):
        arq = open("Alunos.txt","r")
        cpf = input("Informe o cpf do aluno: ")
        for linha in arq:
            if linha.find(cpf) != -1:
                a = Aluno()
                componentes = linha.split(" | ")
                a.nome = componentes[0]
                a.cpf = componentes[1]
                componentes_data = componentes[2].split("-")
                a.dtNasc = date(int(componentes_data[0]), int(componentes_data[1]), int(componentes_data[2]))
                a.sexo = componentes[3]
                a.email = componentes[4]
                a.telefone = componentes[5]
                imprimir_aluno(a)
        arq.close()
        print("Informe os novos dados do aluno: ")
        a.nome = input("Informe o nome do aluno: ")
        a.cpf = alterar_cpf(cpf)
        componentes_data = input("Informe a data de nascimento no formato YYYY-MM-DD: ").split("-")
        a.dtNasc = date(int(componentes_data[0]), int(componentes_data[1]), int(componentes_data[2]))
        a.sexo = input("Informe o sexo(F/M): ")
        a.email = input("Informe o email: ")
        a.telefone = input("Informe o telefone: ")
        arq = open("Alunos.txt","r")
        linhas = arq.readlines()
        arq.close()
        arq = open("Alunos.txt","w")
        for linha in linhas:
            if linha.find(cpf) == -1:
                arq.write(linha)
            else:
                arq.write(a.nome + " | " + a.cpf + " | " + str(a.dtNasc) + " | " + a.sexo + " | " + a.email + " | " + a.telefone + "\n")
        arq.close()
        print("Aluno alterado com sucesso!")
    else:
        print("Não há alunos cadastrados!")
    
#funcao altera cpf
def alterar_cpf(antigo_cpf):
    alterar = input("Deseja alterar o cpf do aluno? (S/N): ")
    if alterar == "S":
        cpf = input("Informe o cpf do aluno: ")
        if len(cpf) == 11:
            if existe_arquivo("Alunos.txt"):
                arq = open("Alunos.txt","r")
                for linha in arq:
                    if linha.find(cpf) != -1:
                        print("CPF já cadastrado!")
                        cpf = verificar_cpf()
                arq.close()
        else:
            print("CPF inválido!")
            cpf = verificar_cpf()
    else:
        cpf = antigo_cpf
    return cpf

#funcao para excluir o cadastro de um aluno
def excluir_aluno():
    print("Menu Excluir Aluno")
    if existe_arquivo("Alunos.txt"):
        arq = open("Alunos.txt","r")
        cpf = input("Informe o cpf do aluno: ")
        for linha in arq:
            if linha.find(cpf) != -1:
                a = Aluno()
                componentes = linha.split(" | ")
                a.nome = componentes[0]
                a.cpf = componentes[1]
                componentes_data = componentes[2].split("-")
                a.dtNasc = date(int(componentes_data[0]), int(componentes_data[1]), int(componentes_data[2]))
                a.sexo = componentes[3]
                a.email = componentes[4]
                a.telefone = componentes[5]
                imprimir_aluno(a)
        arq.close()
        excluir = input("Deseja excluir o aluno? (S/N): ")
        if excluir == "S":
            with open("Alunos.txt","r") as f:
                linhas = f.readlines()
            with open("Alunos.txt","w") as f:
                for linha in linhas:
                    if linha.find(cpf) == -1:
                        f.write(linha)
            print("Aluno excluído com sucesso!")
        else:
            print("Aluno não excluído!")
    else:
        print("Não há alunos cadastrados!")
    
#-------------------------------------------------------------------------------------------------------------------------------------

#funcoes para area de cursos

#funcao para inserir um curso
def inserir_curso():
    print("Menu Inserir Curso")
    c = Curso()
    c.nome = input("Informe o nome do curso: ")
    c.codigo = verificar_codigo()
    c.cargaHoraria = input("Informe a carga horária do curso: ")
    c.valor = input("Informe o valor do curso: ")
    arq = open("Cursos.txt","a")
    arq.write(c.nome + " | " + c.codigo + " | " + c.cargaHoraria + " | " + c.valor + "\n")
    arq.close()
    print("Curso inserido com sucesso!")

#funcao para verificar codigo
def verificar_codigo():
    codigo = input("Informe o código do curso: ")
    if len(codigo) == 5:
        if existe_arquivo("Cursos.txt"):
            arq = open("Cursos.txt","r")
            for linha in arq:
                if linha.find(codigo) != -1:
                    print("Código já cadastrado!")
                    codigo = verificar_codigo()
            arq.close()
    else:
        print("Código inválido!")
        codigo = verificar_codigo()
    return codigo

#funcao que imprime os dados de um curso na tela
def imprimir_curso(c):
    print("Codigo: ", c.codigo, " | Nome: ", c.nome, " | Carga horaria: ", str(c.cargaHoraria), " | Valor: ", c.valor)

#funcao para buscar um curso pelo codigo
def listar_1_curso():
    print("Menu Listar 1 Curso")
    if existe_arquivo("Cursos.txt"):
        arq = open("Cursos.txt","r")
        codigo = input("Informe o código do curso: ")
        for linha in arq:
            if linha.find(codigo) != -1:
                c = Curso()
                componentes = linha.split(" | ")
                c.nome = componentes[0]
                c.codigo = componentes[1]
                c.cargaHoraria = componentes[2]
                c.valor = componentes[3]
                imprimir_curso(c)
        arq.close()
    else:
        print("Não há cursos cadastrados!")

#funcao para buscar todos os cursos
def listar_todos_curso():
    print("Menu Listar Todos Cursos")
    if existe_arquivo("Cursos.txt"):
        arq = open("Cursos.txt","r")
        for linha in arq:
            c = Curso()
            componentes = linha.split(" | ")
            c.nome = componentes[0]
            c.codigo = componentes[1]
            c.cargaHoraria = componentes[2]
            c.valor = componentes[3]
            imprimir_curso(c)
        arq.close()
    else:
        print("Não há cursos cadastrados!")

#funcao para alterar os dados de um curso
def alterar_curso():
    print("Menu Alterar Curso")
    if existe_arquivo("Cursos.txt"):
        arq = open("Cursos.txt","r")
        codigo = input("Informe o código do curso: ")
        for linha in arq:
            if linha.find(codigo) != -1:
                c = Curso()
                componentes = linha.split(" | ")
                c.nome = componentes[0]
                c.codigo = componentes[1]
                c.cargaHoraria = componentes[2]
                c.valor = componentes[3]
                antigo_codigo = c.codigo
                imprimir_curso(c)
        arq.close()
        alterar = input("Deseja alterar o curso? (S/N): ")
        if alterar == "S":
            c.nome = input("Informe o nome do curso: ")
            c.codigo = alterar_codigo(codigo)
            c.cargaHoraria = input("Informe a carga horária do curso: ")
            c.valor = input("Informe o valor do curso: ")
            arq = open("Cursos.txt","r")
            linhas = arq.readlines()
            arq.close()
            arq = open("Cursos.txt","w")
            for linha in linhas:
                if linha.find(antigo_codigo) == -1:
                    arq.write(linha)
                else:
                    arq.write(c.nome + " | " + c.codigo + " | " + c.cargaHoraria + " | " + c.valor + "\n")
            arq.close()
            print("Curso alterado com sucesso!")
        else:
            print("Curso não alterado!")
    else:
        print("Não há cursos cadastrados!")

#funcao alterar codigo
def alterar_codigo(codigo_antigo):
    alterar = input("Deseja alterar o código do curso? (S/N): ")
    if alterar == "S":
        codigo = input("Informe o código do curso: ")
        if len(codigo) == 5:
            if existe_arquivo("Cursos.txt"):
                arq = open("Cursos.txt","r")
                for linha in arq:
                    if linha.find(codigo) != -1:
                        print("Código já cadastrado!")
                        codigo = alterar_codigo()
                arq.close()
        else:
            print("Código inválido!")
            codigo = alterar_codigo()
    else:
        codigo = codigo_antigo
    return codigo
    
#funcao para excluir o cadastro de um curso
def excluir_curso():
    print("Menu Excluir Curso")
    if existe_arquivo("Cursos.txt"):
        arq = open("Cursos.txt","r")
        codigo = input("Informe o código do curso: ")
        for linha in arq:
            if linha.find(codigo) != -1:
                c = Curso()
                componentes = linha.split(" | ")
                c.nome = componentes[0]
                c.codigo = componentes[1]
                c.cargaHoraria = componentes[2]
                c.valor = componentes[3]
                imprimir_curso(c)
        arq.close()
        excluir = input("Deseja excluir o curso? (S/N): ")
        if excluir == "S":
            with open("Cursos.txt","r") as f:
                linhas = f.readlines()
            with open("Cursos.txt","w") as f:
                for linha in linhas:
                    if linha.find(codigo) == -1:
                        f.write(linha)
            print("Curso excluído com sucesso!")
        else:
            print("Curso não excluído!")
    else:
        print("Não há cursos cadastrados!")

#-------------------------------------------------------------------------------------------------------------------------------------

#funcoes para area de matriculas

#funcao para cadastrar uma matricula
def cadastrar_matricula():
    print("Menu Cadastrar Matrícula")
    if existe_arquivo("Alunos.txt"):
        if existe_arquivo("Cursos.txt"):
            matricula = Matricula()
            matricula.cpfAluno = verificar_cpf_existe()
            matricula.codigoCurso = verificar_codigo_existe()
            print("Padrao de data: AAAA-MM-DD")
            matricula.dataInicio = input("Informe a data de início: ")
            matricula.dataFim = input("Informe a data de término: ")
            matricula.desconto = input("Informe o valor de desconto: ")
            arq = open("Matriculas.txt","a")
            arq.write(matricula.cpfAluno + " | " + matricula.codigoCurso + " | " + matricula.dataInicio + " | " + matricula.dataFim + " | " + matricula.desconto + "\n")
            arq.close()
            print("Matrícula cadastrada com sucesso!")
        else:
            print("Não há cursos cadastrados!")
    else:
        print("Não há alunos cadastrados!")

#funcao para verificar se o cpf do aluno existe
def verificar_cpf_existe():
    cpf = input("Informe o CPF do aluno: ")
    if existe_arquivo("Alunos.txt"):
        arq = open("Alunos.txt","r")
        for linha in arq:
            if linha.find(cpf) != -1:
                return cpf
        arq.close()
        print("CPF não cadastrado!")
        cpf = verificar_cpf_existe()
    else:
        print("Não há alunos cadastrados!")
    return cpf

#funcao para verificar se o codigo do curso existe
def verificar_codigo_existe():
    codigo = input("Informe o código do curso: ")
    if existe_arquivo("Cursos.txt"):
        arq = open("Cursos.txt","r")
        for linha in arq:
            if linha.find(codigo) != -1:
                return codigo
        arq.close()
        print("Código não cadastrado!")
        codigo = verificar_codigo_existe()
    else:
        print("Não há cursos cadastrados!")
    return codigo

#funcao para imprimir uma matricula
def imprimir_matricula(m):
    print("CPF: ", m.cpfAluno, " | Codigo: ", m.codigoCurso, " | Data inicio: ", str(m.dataInicio), " | Data fim: ", str(m.dataFim), " | Desconto: ", m.desconto)

#funcao para buscar uma matricula
def buscar_1_matricula():
    print("Menu Buscar 1 Matrícula")
    if existe_arquivo("Matriculas.txt"):
        arq = open("Matriculas.txt","r")
        cpf = input("Informe o CPF do aluno: ")
        codigo = input("Informe o código do curso: ")
        for linha in arq:
            if linha.find(cpf) != -1 and linha.find(codigo) != -1:
                m = Matricula()
                componentes = linha.split(" | ")
                m.cpfAluno = componentes[0]
                m.codigoCurso = componentes[1]
                m.dataInicio = componentes[2]
                m.dataFim = componentes[3]
                m.desconto = componentes[4]
                imprimir_matricula(m)
        arq.close()
    else:
        print("Não há matrículas cadastradas!")

#funcao para buscar todas as matriculas
def buscar_todas_matriculas():
    print("Menu Buscar Todas as Matrículas")
    if existe_arquivo("Matriculas.txt"):
        arq = open("Matriculas.txt","r")
        for linha in arq:
            m = Matricula()
            componentes = linha.split(" | ")
            m.cpfAluno = componentes[0]
            m.codigoCurso = componentes[1]
            m.dataInicio = componentes[2]
            m.dataFim = componentes[3]
            m.desconto = componentes[4]
            imprimir_matricula(m)
        arq.close()
    else:
        print("Não há matrículas cadastradas!")

#funcao para alterar uma matricula
def alterar_matricula():
    print("Menu Alterar Matrícula")
    if existe_arquivo("Matriculas.txt"):
        arq = open("Matriculas.txt","r")
        cpf = input("Informe o CPF do aluno: ")
        codigo = input("Informe o código do curso: ")
        for linha in arq:
            if linha.find(cpf) != -1 and linha.find(codigo) != -1:
                m = Matricula()
                componentes = linha.split(" | ")
                m.cpfAluno = componentes[0]
                m.codigoCurso = componentes[1]
                m.dataInicio = componentes[2]
                m.dataFim = componentes[3]
                m.desconto = componentes[4]
                imprimir_matricula(m)
        arq.close()
        alterar = input("Deseja alterar a matrícula? (S/N): ")
        if alterar == "S":
            arq = open("Matriculas.txt","r")
            linhas = arq.readlines()
            arq.close()
            arq = open("Matriculas.txt","w")
            for linha in linhas:
                if linha.find(cpf) == -1 and linha.find(codigo) == -1:
                    arq.write(linha)
            arq.close()
            cadastrar_matricula()
            print("Matrícula alterada com sucesso!")
        else:
            print("Matrícula não alterada!")
    else:
        print("Não há matrículas cadastradas!")

#funcao para excluir uma matricula
def excluir_matricula():
    print("Menu Excluir Matrícula")
    if existe_arquivo("Matriculas.txt"):
        arq = open("Matriculas.txt","r")
        cpf = input("Informe o CPF do aluno: ")
        codigo = input("Informe o código do curso: ")
        for linha in arq:
            if linha.find(cpf) != -1 and linha.find(codigo) != -1:
                m = Matricula()
                componentes = linha.split(" | ")
                m.cpfAluno = componentes[0]
                m.codigoCurso = componentes[1]
                m.dataInicio = componentes[2]
                m.dataFim = componentes[3]
                m.desconto = componentes[4]
                imprimir_matricula(m)
        arq.close()
        excluir = input("Deseja excluir a matrícula? (S/N): ")
        if excluir == "S":
            with open("Matriculas.txt","r") as f:
                linhas = f.readlines()
            with open("Matriculas.txt","w") as f:
                for linha in linhas:
                    if linha.find(cpf) == -1 and linha.find(codigo) == -1:
                        f.write(linha)
            print("Matrícula excluída com sucesso!")
        else:
            print("Matrícula não excluída!")
    else:
        print("Não há matrículas cadastradas!")

#-------------------------------------------------------------------------------------------------------------------------------------

#funcoes para area de relatorios

#funcao imprimir nome curso e alunos
def funcaoA():
    print("Menu Relatório A")
    busc_codigo = input("Informe o código do curso: ")
    arq = open("Cursos.txt","r")
    for linha in arq:
        if linha.find(busc_codigo) != -1:
            componentes = linha.split(" | ")
            nome_curso = componentes[0]
            print("Curso: ",nome_curso)
    arq.close()
    arq = open("Matriculas.txt","r")
    for linha in arq:
        if linha.find(busc_codigo) != -1:
            componentes = linha.split(" | ")
            cpf_aluno = componentes[0]
            print("CPF do aluno: ",cpf_aluno, end=" | ")
            arq2 = open("Alunos.txt","r")
            for linha2 in arq2:
                if linha2.find(cpf_aluno) != -1:
                    componentes2 = linha2.split(" | ")
                    nome_aluno = componentes2[0]
                    print("Nome do aluno: ",nome_aluno, end=" | ")
                    email_aluno = componentes2[4]
                    print("Email do aluno: ",email_aluno)
            arq2.close()
    arq.close()

#funcao cursos entre duas datas
def funcaoB():
    print("Menu Relatório B")
    arq = open("Matriculas.txt","r")
    print("Padrao de data: AAAA-MM-DD")
    data1 = input("Informe a primeira data: ")
    data2 = input("Informe a segunda data: ")
    for linha in arq:
        componentes = linha.split(" | ")
        data_inicio = componentes[2]
        if data_inicio >= data1 and data_inicio <= data2:
            codigo_curso = componentes[1]
            arq2 = open("Cursos.txt","r")
            for linha2 in arq2:
                if linha2.find(codigo_curso) != -1:
                    componentes2 = linha2.split(" | ")
                    nome_curso = componentes2[0]
                    carga_horaria = componentes2[2]
                    valor_curso = componentes2[3]
                    print("Nome: ", nome_curso, " | Codigo: ", codigo_curso, " | Carga Horaria: ", carga_horaria, " | Valor: ", valor_curso)
            arq2.close()
    arq.close()

#funcao cursos realizados por determinado aluno
def funcaoC():
    print("Menu Relatório C")
    arq = open("Matriculas.txt","r")
    cpf = input("Informe o CPF do aluno: ")
    for linha in arq:
        if linha.find(cpf) != -1:
            componentes = linha.split(" | ")
            codigo_curso = componentes[1]
            arq2 = open("Cursos.txt","r")
            for linha2 in arq2:
                if linha2.find(codigo_curso) != -1:
                    c = Curso()
                    componentes2 = linha.split(" | ")
                    componentes2 = linha2.split(" | ")
                    nome_curso = componentes2[0]
                    carga_horaria = componentes2[2]
                    valor_curso = componentes2[3]
                    print("Nome: ", nome_curso, " | Codigo: ", codigo_curso, " | Carga Horaria: ", carga_horaria, " | Valor: ", valor_curso)
            arq2.close()
    arq.close()

#-------------------------------------------------------------------------------------------------------------------------------------

#funcao menu principal
def main():
    opcoes=['0','1','2','3','4','5']
    op = ''
    while op != '0':
        os.system('cls')
        fazer=''
        op=''
        op = menu()
        if op == '1':
            while fazer != opcoes:
                print("\nMenu Alunos")
                fazer = menu_fazer()
                if fazer == '1':
                    os.system('cls')
                    inserir_aluno()
                elif fazer == '2':
                    os.system('cls')
                    listar_1_aluno()
                elif fazer == '3':
                    os.system('cls')
                    listar_todos_aluno()
                elif fazer == '4':
                    os.system('cls')
                    alterar_aluno()
                elif fazer == '5':
                    os.system('cls')
                    excluir_aluno()
                elif fazer == '0':
                    print("Voltando ao menu principal...")
                    break
                else:
                    print("Opção inválida!")
        elif op == '2':
            while fazer != opcoes:
                print("\nMenu Cursos")
                fazer = menu_fazer()
                if fazer == '1':
                    os.system('cls')
                    inserir_curso()
                elif fazer == '2':
                    os.system('cls')
                    listar_1_curso()
                elif fazer == '3':
                    os.system('cls')
                    listar_todos_curso()
                elif fazer == '4':
                    os.system('cls')
                    alterar_curso()
                elif fazer == '5':
                    os.system('cls')
                    excluir_curso()
                elif fazer == '0':
                    print("Voltando ao menu principal...")
                    break
                else:
                    print("Opção inválida!")
        elif op == '3':
            while fazer != opcoes:
                print("\nMenu Matrículas")
                fazer = menu_fazer()
                if fazer == '1':
                    os.system('cls')
                    cadastrar_matricula()
                elif fazer == '2':
                    os.system('cls')
                    buscar_1_matricula()
                elif fazer == '3':
                    os.system('cls')
                    buscar_todas_matriculas()
                elif fazer == '4':
                    os.system('cls')
                    alterar_matricula()
                elif fazer == '5':
                    os.system('cls')
                    excluir_matricula()
                elif fazer == '0':
                    print("Voltando ao menu principal...")
                    break
                else:
                    print("Opção inválida!")
        elif op == '4':
            while fazer != [1,2,3,0]:
                print("\nMenu Relatorios")
                fazer = menu_relatorio()
                if fazer == '1':
                    os.system('cls')
                    funcaoA()
                elif fazer == '2':
                    os.system('cls')
                    funcaoB()
                elif fazer == '3':
                    os.system('cls')
                    funcaoC()
                elif fazer == '0':
                    print("Voltando ao menu principal...")
                    break
                else:
                    print("Opção inválida!")
        elif op == '0':
            print("Obrigado por usar nosso sistema!")
        else:
            print("Opcao invalida.")

#-------------------------------------------------------------------------------------------------------------------------------------

#inicio do programa
if existe_arquivo("Alunos.txt") == False:
    arq = open("Alunos.txt",'w')
    print("Arquivo de alunos criado e pronto para a escrita")
    
if existe_arquivo("Cursos.txt") == False:
    arq = open("Cursos.txt",'w')
    print("Arquivo de cursos criado e pronto para a escrita")

if existe_arquivo("Matriculas.txt") == False:
    arq = open("Matriculas.txt",'w')
    print("Arquivo de matriculas criado e pronto para a escrita")

main()
