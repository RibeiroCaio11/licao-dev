class Conta:
    def __init__(self,saldo:float,numero:int,agencia:str,cliente,historico):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico

    def exibir_saldo(self,):
        return f"saldo da conta é:{self.saldo}"

    def nova_conta(self,cliente,numero:int):
       return  Conta(0.0, numero, self.agencia, cliente, Historico())
        
        

    def sacar(self,valor:float):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.adicionar_transacao(f"Saque de {valor}")
            return f"saldo:{self.saldo}"
        else:
            return f"Saldo insuficiente"
        
    def depositar(self,valor:float):
        self.saldo += valor
        self.historico.adicionar_transacao(f"Depósito de {valor}")


class ContaCorrente(Conta):
    def __init__(self,saldo:float,numero:int,agencia:str,cliente,historico,limite:float,limite_saques:int):
        super().__init__(saldo,numero,agencia,cliente,historico)
        self.limite = limite
        self.limite_saques = limite_saques
        
    
class Transacao:
    def __init__(self,valor:float):
        self.valor = valor
        
    def registrar(self,conta):
        pass

class Deposito(Transacao):
    def registrar(self, conta):
        conta.depositar(self.valor)
        conta.historico.adicionar_transacao(f"Depósito de {self.valor}")

class Saque(Transacao):
    def registrar(self, conta):
        if conta.sacar(self.valor):  
            conta.historico.adicionar_transacao(f"Saque de {self.valor}")

class Historico:
     
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao: str):
            self.transacoes.append(transacao)

    def exibir_transacoes(self):
        for transacao in self.transacoes:
            print(transacao)
           
class Cliente:
    def __init__(self,nome,cpf,email,endereco,):
        self.cpf = cpf
        self.nome=nome
        self.email=email
        self.endereco = endereco
        self.contas = []
        

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self,conta,transacao):
        if isinstance(transacao, Transacao):
            transacao.registrar(conta)     

class PessoaFisica(Cliente):
    def __init__(self,email,cpf,nome,data_nascimento,endereco):
        self.data_nascimento = data_nascimento
        super().__init__(nome,cpf,email,endereco)
        
historico = Historico()

cliente = PessoaFisica("Alfredo", "123.456.789-00", "alfredo@example.com", "São Paulo", "15/12/1996")
conta1 = ContaCorrente(1500.0, 132, "001", cliente, historico, 500.0, 3)
cliente.adicionar_conta(conta1)

deposito = Deposito(200.0)
saque = Saque(150.0)

cliente.realizar_transacao(conta1, deposito)
cliente.realizar_transacao(conta1, saque)

nova_conta = ContaCorrente(0.0, 789, "001", cliente, historico, 500.0, 3)
cliente.adicionar_conta(nova_conta)

print(f"Nova conta: {nova_conta.numero}")
historico.exibir_transacoes()