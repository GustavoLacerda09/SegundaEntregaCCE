n=0
o=0 
p=0 
q=0   
class Materia():
    def __init__(self, materia = None):
        self.materia = materia
   
    def cadastrar(self):
        print('Digite o nome da matéria:')
        self.materia = str (input())
        return self.materia
    def mostrar():
        print (A)
A=[]
lista= [None]
a = Materia()
lista[n] = a.cadastrar()
n=n+1
A.append(lista)

    
class Professor(): 
    def __init__(self, professor = None):
        self.professor = professor 
   
    def cadastrar(self):
        print('Digite o nome do professor:')
        self.professor = str (input())
        return self.professor
    def mostrar():
        print (B)
B=[None]
b = Professor()
B[o]= b.cadastrar()
o= o+1

class Aluno():
    def __init__(self, aluno = None):
        self.aluno = aluno
   
    def cadastrar(self):
        print('Digite o nome do aluno:')
        self.aluno = str (input())
        return self.aluno
    def mostrar():
        print (C)
C=[None]
c = Aluno()
C[p]= c.cadastrar()
p= p+1

class Turma():
    def __init__(self, turma = None):
        self.turma = turma
   
    def cadastrar(self):
        print('Digite o nome da turma:')
        self.turma = str (input())
        return self.turma
    def mostrar():
        print (D)

    def designar(self, turma, professor):
        self.professor = professor
        self.turma = turma
        Professor.mostrar()
        Turma.mostrar()
        print ("Para designar um professor para uma nova turma digite designar(turma, nome_do_professor): ")
D=[None]
d = Turma()
D[q]= d.cadastrar()
q= q+1