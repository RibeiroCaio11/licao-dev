class Pessoa:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.__cpf = cpf
        self.idade = idade

    def get_cpf(self):
        return self.__cpf

class Paciente(Pessoa):
    def __init__(self, nome, cpf, idade, queixa, sexo):
        super().__init__(nome, cpf, idade)
        self.queixa = queixa
        self.sexo = sexo
    
    def adicionar_info(self):
        self.nome = input("Digite o nome do paciente: ")
        self._Pessoa__cpf = input("Digite o cpf do paciente: ")
        self.idade = input("Digite a idade do paciente: ")
        self.queixa = input("Digite a queixa do paciente: ")
        self.sexo = input("Digite o sexo: ")

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Queixa: {self.queixa}, Sexo: {self.sexo}"
    

class Medico(Pessoa):
    def __init__(self, crm, cpf, nome, especialidade, telefone, idade):
        super().__init__(nome, cpf, idade)
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
    def __init__(self, data, hora, medico, paciente):
        self.data = data
        self.hora = hora
        self.medico = medico
        self.paciente = paciente

    def adicionar_consulta(self):
        self.data = input("Digite a data da consulta: ")
        self.hora = input("Digite a hora da consulta: ")
        self.medico = input("Digite o nome do médico: ")
        self.paciente = input("Digite o nome do paciente: ")

    def __str__(self):
        return f"Data: {self.data}, Hora: {self.hora}, Medico: {self.medico}, Paciente: {self.paciente}"
    

class Hospital:
    def __init__(self, nome):
        self.nome = nome
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
        consulta = Consulta("", "", "", "")
        consulta.adicionar_consulta()
        self.consultas.append(consulta)

    def visualizar_consultas(self):
        for consulta in self.consultas:
            print(consulta)
    
def main():
    hospital = Hospital("centro")
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
    

#front
from tkinter import *
from tkinter import ttk,messagebox

root = Tk()

class Application:

    def __init__(self):
        self.root = root
        self.tela()
        self.frame_principal()
        self.entrada_paciente()
        self.criar_lista()
        self.hospital = Hospital("centro")
        self.lista()
        root.mainloop()

    def frame_principal(self):
        self.frame_principal = Frame(self.root)
        self.frame_principal.place(relx=0.014, rely=0.02, relwidth=0.97, relheight=0.96)

    def tela(self):    
        self.root.title("Clinica Saúde")
        self.root.geometry("700x500")
        self.root.resizable(False, False)
        self.root.configure(background="#1e3743")
    
    def entrada_paciente(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()
        
        Label(self.frame_principal, text="Cadastro de Paciente", font=("Arial", 14, "bold")).place(relx=0.35, rely=0.01)
        Label(self.frame_principal, text="Nome:").place(relx=0.3, rely=0.2)
        self.nome_paciente = Entry(self.frame_principal, width=30)
        self.nome_paciente.place(relx=0.38, rely=0.2)

        Label(self.frame_principal, text="CPF:").place(relx=0.3, rely=0.28)
        self.cpf_paciente = Entry(self.frame_principal, width=30)
        self.cpf_paciente.place(relx=0.38, rely=0.28)

        Label(self.frame_principal, text="Idade:").place(relx=0.3, rely=0.36)
        self.idade_paciente = Entry(self.frame_principal, width=30)
        self.idade_paciente.place(relx=0.38, rely=0.36)

        Label(self.frame_principal, text="Queixa:").place(relx=0.3, rely=0.44)
        self.queixa_paciente = Entry(self.frame_principal, width=30)
        self.queixa_paciente.place(relx=0.38, rely=0.44)
        
        self.var1 = IntVar()
        Checkbutton(self.frame_principal, text='Masculino', variable=self.var1).place(relx=0.45, rely=0.5)
        self.var2 = IntVar()
        Checkbutton(self.frame_principal, text='Feminino', variable=self.var2).place(relx=0.3, rely=0.5)
        Button(self.root, text='Sair', width=10, command=root.destroy).place(relx=0.8, rely=0.9)
        Button(self.frame_principal, text="Confirmar", command=self.confirmar_paciente).place(relx=0.4, rely=0.58)
        
    def entrada_medico(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()
        
        Label(self.frame_principal, text="Cadastro de Médico", font=("Arial", 14, "bold")).place(relx=0.35, rely=0.01)
        Label(self.frame_principal, text="Nome:").place(relx=0.3, rely=0.2)
        self.nome_medico = Entry(self.frame_principal, width=30)
        self.nome_medico.place(relx=0.38, rely=0.2)
        Label(self.frame_principal, text="CPF:").place(relx=0.3, rely=0.28)
        self.cpf_medico = Entry(self.frame_principal, width=30)
        self.cpf_medico.place(relx=0.38, rely=0.28)

        Label(self.frame_principal, text="Idade:").place(relx=0.3, rely=0.36)
        self.idade_medico = Entry(self.frame_principal, width=30)
        self.idade_medico.place(relx=0.38, rely=0.36)

        Label(self.frame_principal, text="CRM:").place(relx=0.3, rely=0.44)
        self.crm_medico = Entry(self.frame_principal, width=30)
        self.crm_medico.place(relx=0.38, rely=0.44)

        Label(self.frame_principal, text="Especialidade:").place(relx=0.25, rely=0.52)
        self.especialidade_medico = Entry(self.frame_principal, width=30)
        self.especialidade_medico.place(relx=0.38, rely=0.52)

        Label(self.frame_principal, text="Telefone:").place(relx=0.3, rely=0.6)
        self.telefone_medico = Entry(self.frame_principal, width=30)
        self.telefone_medico.place(relx=0.38, rely=0.6)
        
        self.var1 = IntVar()
        Checkbutton(self.frame_principal, text='Masculino', variable=self.var1).place(relx=0.45, rely=0.68)
        self.var2 = IntVar()
        Checkbutton(self.frame_principal, text='Feminino', variable=self.var2).place(relx=0.3, rely=0.68)
        Button(self.root, text='Sair', width=10, command=root.destroy).place(relx=0.8, rely=0.9)
        Button(self.frame_principal, text="Confirmar", command=self.confirmar_medico).place(relx=0.4, rely=0.76)

    def info_consultas(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

        Label(self.frame_principal, text="Agendamento de Consulta", font=("Arial", 14, "bold")).place(relx=0.35, rely=0.01)
        Label(self.frame_principal, text="Data:").place(relx=0.3, rely=0.2)
        self.data_consulta = Entry(self.frame_principal, width=30)
        self.data_consulta.place(relx=0.38, rely=0.2)

        Label(self.frame_principal, text="Horário:").place(relx=0.3, rely=0.28)
        self.horario_consulta = Entry(self.frame_principal, width=30)
        self.horario_consulta.place(relx=0.38, rely=0.28)
        
        Label(self.frame_principal, text="Paciente:").place(relx=0.3, rely=0.36)
        self.paciente_consulta = Entry(self.frame_principal, width=30)
        self.paciente_consulta.place(relx=0.38, rely=0.36)

        Label(self.frame_principal, text="Médico:").place(relx=0.3, rely=0.44)
        self.medico_consulta = Entry(self.frame_principal, width=30)
        self.medico_consulta.place(relx=0.38, rely=0.44)

        Button(self.root, text='Sair', width=10, command=root.destroy).place(relx=0.8, rely=0.9)
        Button(self.frame_principal, text="Confirmar", command=self.confirmar_consulta).place(relx=0.4, rely=0.52)

    def visualizar(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

        Label(self.frame_principal, text="Visualizção de Consultas", font=("Arial", 14, "bold")).place(relx=0.35, rely=0.01)
        lista = ttk.Treeview(self.frame_principal, height=2, columns=("col1", "col2", "col3"))
        lista.heading("#0", text="Data:")
        lista.heading("#1", text="Horário:")
        lista.heading("#2", text="Paciente:")
        lista.heading("#3", text="Médico:")
        lista.column("#0", width=120)
        lista.column("#1", width=120)
        lista.column("#2", width=120)
        lista.column("#3", width=120)
        lista.place(relx=0.1, rely=0.2)
        Button(self.root, text='Sair', width=10, command=root.destroy).place(relx=0.8, rely=0.9)
        for consulta in self.hospital.consultas:
            lista.insert("", "end", text=consulta.data, values=(consulta.hora, consulta.paciente, consulta.medico))
        
    def criar_lista(self, event=None):
        # Create a label
        self.label = Label(self.root, text="Selecione: ")
        self.label.place(relx=0.3, rely=0.09)

        # Create a Combobox widget
        self.combo_box = ttk.Combobox(self.root, values=["Paciente", "Médico", "Agendar", "Visualizar"])
        self.combo_box.place(relx=0.4, rely=0.09)

        # Set default value
        self.combo_box.set("Paciente")

        # Bind event to selection
        self.combo_box.bind("<<ComboboxSelected>>", self.lista)

    def lista(self, event=None):
        selecionado = self.combo_box.get()

        if selecionado == "Paciente":
            self.entrada_paciente()
        elif selecionado == "Médico":
            self.entrada_medico() 
        elif selecionado == "Agendar":
            self.info_consultas()
        elif selecionado == "Visualizar":
            self.visualizar()

    def sair(self):
        button = Tk.Button(self.root, text='Stop', width=25, command=root.destroy)

    def confirmar_paciente(self):
        nome = self.nome_paciente.get()
        cpf = self.cpf_paciente.get()
        idade = self.idade_paciente.get()
        queixa = self.queixa_paciente.get()
        sexo = 'Masculino' if self.var1.get() else 'Feminino'
        
        paciente = Paciente(nome, cpf, idade, queixa, sexo)
        self.hospital.pacientes.append(paciente)
        print("Paciente cadastrado com sucesso!")
        print(paciente)      
    
    def confirmar_medico(self):
        nome = self.nome_medico.get()
        cpf = self.cpf_medico.get()
        idade = self.idade_medico.get()
        crm = self.crm_medico.get()
        especialidade = self.especialidade_medico.get()
        telefone = self.telefone_medico.get()
        
        medico = Medico(crm, cpf, nome, especialidade, telefone, idade)
        self.hospital.medicos.append(medico)
        print("Médico cadastrado com sucesso!")
        print(medico)

    def confirmar_consulta(self):
        data = self.data_consulta.get()
        hora = self.horario_consulta.get()
        paciente = self.paciente_consulta.get()
        medico = self.medico_consulta.get()

        
        paciente_encontrado = None
        for p in self.hospital.pacientes:
            if p.nome == paciente:
                paciente_encontrado = p
                break
        if not paciente_encontrado:
            messagebox.showerror("Erro", "Paciente não cadastrado!")
            return

       
        medico_encontrado = None
        for m in self.hospital.medicos:
            if m.nome == medico:
                medico_encontrado = m
                break
        if not medico_encontrado:
            messagebox.showerror("Erro", "Médico não cadastrado!")
            return
        
        consulta = Consulta(data, hora, medico, paciente)
        self.hospital.consultas.append(consulta)
        print("Consulta agendada com sucesso!")
        print(consulta)

Application()