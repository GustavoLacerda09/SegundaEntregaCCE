from objetos import Professor, Turma

def menu_de_turmas():
    print ('************************************')
    print ('********** Menu de Turmas **********')
    print ('************************************')
    print ("Selecione uma opção abaixo \n")
    print ("1 - Cadastro de uma nova turma")
    print ("2 - Designar professor para uma nova turma")
    print ("3 - Adicionar alunos em uma turma")
    print ("4 - Remover alunos de uma turma")
    print ("5 - Dar a nota final dos alunos de uma turma")
    print ("6 - Mostrar todos os alunos de uma turma")
    print ("7 - Mostras todas as turmas cadastradas")
    print ("8 - Voltar ao Menu Principal\n")
    print ('Escolha: ')
    y = int (input())

    if y==1: 
        turma = Turma()
        turma.cadastrar
        menu_de_turmas()
    elif y==2: 
        turma = Turma()
        turma.designar()
        menu_de_turmas()
    elif y==3: 
        print ("3 - Adicionar alunos em uma turma")
        menu_de_turmas()
    elif y==4:
         print ("4 - Remover alunos de uma turma") 
         menu_de_turmas()
    elif y==5:
        print ("5 - Dar a nota final")
        menu_de_turmas()
    elif y==6:
        print ("6 - Mostrar todos os alunos de uma turma")
        menu_de_turmas()
    elif y==7:
        Turma.mostrar
        menu_de_turmas()
    elif y==8:
         return
    else :
        print('Opção Inválida: [Enter]')
        return
