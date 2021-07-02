from menu_principal import menu_principal

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
        print ("1 - Cadastro de uma nova matéria")
    elif y==2: 
        print ("2 - Cadastro de um novo professor")
    elif y==3: 
        print ("3 - Cadastro de um novo aluno")
    elif y==4:
         print ("4 - Mostrar todos as matérias cadastradas") 
    elif y==5:
        print ("5 - Mostrar todos os professores cadastrados")
    elif y==6:
        print ("6 - Mostrar todos os alunos cadastrados")
    elif y==7:
        print ("7 - Abrir Menu de Turmas")
    elif y==8:
         menu_principal()
    else :
        print('Opção Inválida: [Enter]')
        menu_principal()
