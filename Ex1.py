class Disciplina:

    def __init__(self,id,nome,professor,horario,):
        self.aluno = []
        self.professor = professor
        self.horario = horario
        self.nome = nome
        self.__id = id
    
    def adicionar_alunos(self,aluno):
        self.aluno.append(aluno)
   
    def __str__ (self):
         alunos_formatados = ", ".join(self.aluno) if self.aluno else "Nenhum aluno"
         return(f"Os alunos {alunos_formatados} estão matriculados na disciplina {self.nome} dada pelo professor {self.professor} no horario {self.horario}")        
    
    def get_id(self):
        return self.__id

calculo = Disciplina(id=1, nome="Matemática", professor= "Rodrigo", horario="11:00")

calculo.adicionar_alunos("João")
calculo.adicionar_alunos("Maria")
calculo.adicionar_alunos("José")

print(calculo)
print("ID da disciplina:", calculo.get_id())