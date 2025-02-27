class Paciente:
    def __init__(self,nome,cpf,idade,queixa,sexo):
        self.nome = nome
        self.__cpf = cpf
        self.idade = idade
        self.queixa = queixa
        self.sexo = sexo
        self.paciente = []

    def get_cpf(self):
        return self.__cpf


    def adicionar_paciente(self,paciente):
        self.paciente.append(paciente)
        
    

    def listar_pacientes(self):
        for paciente in self.paciente:
            print(paciente)

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Queixa: {self.queixa}, Sexo: {self.sexo}"
    
    def listar_todos_pacientes():
        for paciente in Paciente.paciente:
            print(paciente)


class Medico:
    def __init__ (self,crm,nome,especialidade,telefone):
        self.__crm = crm
        self.nome = nome 
        self.especialidade = especialidade
        self.telefone = telefone
        self.medico = []

    def get_crm(self):  
        return self.__crm
    
    def adicionar_medico(self,medico):
        self.medico.append(medico)
    
    def __str__(self):
        return f"Nome: {self.nome}, Especialidade: {self.especialidade}, Telefone: {self.telefone}"

class Consulta:
    def __init__(self,data,hora,medico,paciente):
        self.data = data
        self.hora = hora
        self.medico = medico
        self.paciente = paciente
        self.consulta = []

    def adicionar_consulta(self,consulta):
        self.consulta.append(consulta)

    def listar_consultas(self):
        for consulta in self.consulta:
            print(consulta)

    def __str__(self):

        return f"Data: {self.data}, Hora: {self.hora}, Medico: {self.medico}, Paciente: {self.paciente}"
    
    def cadastrar_paciente():
        nome_paciente = input("Digite o nome do paciente: ")

        cpf_paciente= input("Digite o cpf do paciente: ")

        idade_paciente= input("Digite a idade do paciente: ")

        queixa_paciente= input("Digite a queixa do paciente: ")

        sexo_paciente= input("Digite o sexo: ")

    def cadastrar_medico():
        crm_medico= input("Digite o crm do médico: ")

        nome_medico=input("Digite o nome do médico: ")

        especialidade_medico= input("Digite a especialidade do médico: ")

        telefone_medico= input("Digite o telefone do médico: ")

    def agendar_consulta():
        data_consulta= input("Digite a data da consulta: ")

        hora_consulta=  input("Digite a hora da consulta: ")

        medico_consulta= input("Digite o nome do médico: ")

        paciente_consulta= input("Digite o nome do paciente: ")


    
def main():
    while True:
        print("********MENU*********")
        print("1.Cadastrar Paciente")
        print("2.Cadastrar Medico")
        print("3.Agendar Consulta")
        print("4.Sair")


