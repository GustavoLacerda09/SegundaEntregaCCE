from menu_de_turmas import menu_de_turmas
from objetos import A, Materia, Professor, Aluno, Turma

def menu_principal():
    print ('************************************')
    print ('********** Menu Principal **********')
    print ('************************************')
    print ("Selecione uma opção abaixo \n")
    print ("1 - Cadastro de uma nova matéria")
    print ("2 - Cadastro de um novo professor")
    print ("3 - Cadastro de um novo aluno")
    print ("4 - Mostrar todos as matérias cadastradas")
    print ("5 - Mostrar todos os professores cadastrados")
    print ("6 - Mostrar todos os alunos cadastrados")
    print ("7 - Abrir Menu de Turmas")
    print ("8 - Sair do Programa \n")
    print ('Escolha: ')
    x = int (input())

    if x==1: 
        Materia.cadastrar()
        menu_principal()
    elif x==2: 
        Professor.cadastrar()
        menu_principal()
    elif x==3: 
        Aluno.cadastrar()
        menu_principal()
    elif x==4:
         Materia.mostrar()
         menu_principal()
    elif x==5:
        Professor.mostrar()
        menu_principal()
    elif x==6:
        Aluno.mostrar()
        menu_principal()
    elif x==7:
        menu_de_turmas()
    
    elif x==8:
        return 0
    else :
        print('Opção Inválida: [Enter]')
        menu_principal()
menu_principal()