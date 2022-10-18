class Cursos:
    código = ""
    descrição = ""
    carga_horaria = ""
    preço = 0

def inserir_curso(lista_cursos):
    c = Cursos()
    c.codigo = input("Informe o código do curso: ")
    c.descricao = input("Informe a descrição: ")
    c.carga_horaria = float (input("Informe a carga horária: "))
    c.preço = float (input("Informe o preço do curso: "))
    lista_cursos.append(c)
    print ("Curso cadastrado!!!")


def imprime_cursos(c):
    print(c.codigo + " | " + c.descricao + " | " + str(c.carga_horaria) + " | " +  str(c.preço))

def listar_cursos(lista_cursos):
    if len(lista_cursos) > 0:
        i = 0
        while i < len(lista_cursos):
            imprime_cursos(lista_cursos[i])
            i = i + 1
    else:
        print("Não há cursos cadastrados ainda")

def buscar_umcurso(lista_cursos):
    if len(lista_cursos) > 0:
        i = 0
        busca = input ("Digite o código do curso a ser buscado: ")
    
        while i < len(lista_cursos):
            if lista_cursos[i].codigo == busca:
                print ("Sua busca retornou o item a seguir: ")
                imprime_cursos(lista_cursos[i])
            i = i + 1
    else:
        print("Não há cursos cadastrados ainda")

def alterar_curso(lista_cursos):
    if len(lista_cursos) > 0:
        i = 0
        busca = input ("Digite o código do curso a ser buscado: ")
    
        while i < len(lista_cursos):
            if lista_cursos[i].codigo == busca:
                print ("Digite os novos dados a serem inseridos")
                lista_cursos[i].codigo = input("Informe o código do curso: ")
                lista_cursos[i].descricao = input("Informe a descrição: ")
                lista_cursos[i].carga_horaria = float (input("Informe a carga horária: "))
                lista_cursos[i].preço = float (input("Informe o preço do curso: "))
                print ("Informações alteradas!!!")
            i = i + 1


def menu():
    print("**********VOCÊ ESTÁ NO SUBMENU DE CURSOS**********")
    print("Adicionar cursos................1")
    print("Listar todos os cursos..........2")
    print("Buscar um curso.................3")
    print("alterar dados de um curso.......4")
    print("Sair............................0")
    
    opção = input("INSIRA O NÚMERO DE ACORDO COM A OPÇÃO DESEJADA: ")
    return opção


def main():
    cursos = []
    op = ''
    while op != '0':
        op =  menu()
        if op == '1':
            inserir_curso(cursos)
        elif op =='2':
            listar_cursos(cursos)
        elif op =='3':
            buscar_umcurso(cursos)
        elif op == '4':
            alterar_curso(cursos)
        elif op =='0':
            print ("Você escolheu sair")
            print ("Obrigado por usar nosso sistema")

        else:
            print ("opção inválida")
    print("Programa encerrado... ")


main()