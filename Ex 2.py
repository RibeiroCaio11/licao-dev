
class Pessoa:
    def __init__(self,nome,cpf,idade):
        self.nome = nome
        self.__cpf = cpf
        self.idade = idade

    def get_cpf(self):
        return self.__cpf

class Paciente(Pessoa):
    def __init__(self,nome,cpf,idade,queixa,sexo):
        super().__init__(nome,cpf,idade)
        self.queixa = queixa
        self.sexo = sexo
    
    def adicionar_info(self):
        self.nome = input("Digite o nome do paciente: ")
        self._Pessoa__cpf= input("Digite o cpf do paciente: ")
        self.idade= input("Digite a idade do paciente: ")
        self.queixa= input("Digite a queixa do paciente: ")
        self.sexo= input("Digite o sexo: ")

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Queixa: {self.queixa}, Sexo: {self.sexo}"
    

class Medico(Pessoa):
    def __init__ (self,crm,cpf,nome,especialidade,telefone,idade):
        super().__init__(nome,cpf,idade)
        self.__crm = crm
        self.especialidade = especialidade
        self.telefone = telefone

    def get_crm(self):  
        return self.__crm
        
    def cadastrar_medico(self):
        self.nome = input("Digite o nome do médico: ")
        self._Pessoa__cpf = input("Digite o cpf do médico: ")
        self.idade = input("Digite a idade do médico: ")
        self.__crm = input("Digite o crm do médico: ")
        self.especialidade = input("Digite a especialidade do médico: ")
        self.telefone = input("Digite o telefone do médico: ")

    def __str__(self):
        return f"Nome: {self.nome}, Especialidade: {self.especialidade}, Telefone: {self.telefone}"

class Consulta:
    def __init__(self,data,hora,medico,paciente):
        self.data = data
        self.hora = hora
        self.medico = medico
        self.paciente = paciente

    def adicionar_consulta(self):

        self.data= input("Digite a data da consulta: ")
        self.hora=  input("Digite a hora da consulta: ")
        self.medico= input("Digite o nome do médico: ")
        self.paciente= input("Digite o nome do paciente: ")

    def __str__(self):

        return f"Data: {self.data}, Hora: {self.hora}, Medico: {self.medico}, Paciente: {self.paciente}"
    

class Hospital:
    def __init__(self,nome):
        self.nome=nome
        self.pacientes = []
        self.medicos = []
        self.consultas = []
    

    def cadastrar_paciente(self):
        paciente = Paciente("", "", "", "", "")
        paciente.adicionar_info()
        self.pacientes.append(paciente)
  
    def adicionar_medico(self):
        medico = Medico("", "", "", "", "", "")
        medico.cadastrar_medico()
        self.medicos.append(medico)
        
    def agendar_consulta(self):
        consulta = Consulta("","","","")
        consulta.adicionar_consulta()
        self.consultas.append(consulta)

    def visualizar_consultas(self):
        for consulta in self.consultas:
            print(consulta)
    
def main():
    hospital=Hospital("centro")
    while True:
        print("********MENU*********")
        print("1.Cadastrar Paciente")
        print("2.Cadastrar Medico")
        print("3.Agendar Consulta")
        print("4.Visualizar Consultas")
        print("5.Sair")

        escolha = int(input("Digite uma opção:"))

        if escolha == 1:
            hospital.cadastrar_paciente()
        
        elif escolha == 2:
            hospital.adicionar_medico()
        
        elif escolha == 3:
            hospital.agendar_consulta()

        elif escolha == 4:
            hospital.visualizar_consultas()
        
        elif escolha == 5:
            break
    

main()