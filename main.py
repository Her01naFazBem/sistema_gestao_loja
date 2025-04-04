class Produto:
    
    def __init__(self, nome, preco, estoque, peso_kg):
        self.nome: str = nome
        self.preco: float = preco
        self.estoque: int = estoque
        self.peso_kg: float = peso_kg

    def novo_preco (self, novo_preco):
        if novo_preco > 0 :
            self.preco = novo_preco
    
    def aplicar_desconto (self, percentual):
        percentual1 = percentual / 100

        self.preco *= (1 - percentual1)


    def verificar_estoque (self) :
        if self.estoque < 5 :
            return True
        
    def __eq__(self, value):
        if self.nome == value.nome and self.preco == value.preco :
            return True
    
    def __str__(self):
        return f"Produto: {self.nome} | Preço: R$ {self.preco} | Estoque: {self.estoque}"

class Cliente :
    def __init__(self, nome, email, pontos_fidelidade):
        self.nome: str = nome
        self.email: str = email
        self.pontos_fidelidade: int = pontos_fidelidade
    
    def adicionar_pontos (self, pontos):
        if pontos > 0 :
            self.pontos_fidelidade += pontos

    def resgatar_pontos (self, pontos):
        if pontos > 0:
            self.pontos_fidelidade -= pontos
    
    def verificar_vip (self):
        if self.pontos_fidelidade >= 1000:
            return True
        
    def __eq__(self, value):
        if self.email == value.email:
            return True
        
    def __iadd__ (self, value):
        self.pontos_fidelidade += value
        return self
    
    def __str__(self):
        return f"Cliente: {self.nome} | Pontos: {self.pontos_fidelidade}"
    
class Pedido :
    def __init__(self, cliente: Cliente, produto: Produto, quantidade, status):
        if status.lower() not in ["pendente", "processando", "entregue"]:
            raise ValueError("Status inválido")
        
        self.cliente = cliente
        self.produto = produto
        self.quantidade: int = quantidade
        self.status: str = status.lower()


    def calcular_total(self):
        return self.quantidade * self.produto.preco


    def calcular_peso_total (self):
        return self.quantidade * self.produto.preco

    
    def atualizar_status (self, novo_status):
        if novo_status.lower() in ["pendente", "processando", "entregue"]:
            if self.status is novo_status :
                raise ValueError("Status igual ao atual")
            elif self.status is "Entregue"and novo_status is "Pendente" :
                raise ValueError("O pedido não pode voltar a ser pendente depois de ser entregue!")
    
    def cancelar_pedido(self):
        if self.status is "pendente" :
            if self.status is "pendente":
                self.status = "cancelado"
            else:
                raise ValueError("Somente pedidos pendentes podem ser cancelados")
            
    def __add__ (self, other):
        if isinstance(other, Pedido):
            self.quantidade += other.quantidade
        return self
    
    def __lt__ (self, other):
        return self.produto.peso_kg < other.produto.peso_kg

        
    def __call__ (self):
        return f"Pedido: {self.quantidade}X {self.produto}"
    

# Criando um produto
p1 = Produto("Notebook", 3500.00, 10, 2.5)
print(p1)

# Aplicando desconto de 10%
p1.aplicar_desconto(10)
print(f"Preço com desconto: R$ {p1.preco:.2f}")  # Esperado: 350.00 (problema aqui! veja observação abaixo)

# Atualizando o preço
p1.novo_preco(2999.90)
print(f"Novo preço atualizado: R$ {p1.preco:.2f}")  # Esperado: 2999.90

# Verificando estoque
print("Estoque baixo?", p1.verificar_estoque())  # Esperado: False

# Criando um cliente
c1 = Cliente("Maria", "maria@email.com", 950)
print(c1)

# Adicionando pontos
c1.adicionar_pontos(100)
print(f"Pontos após adição: {c1.pontos_fidelidade}")  # Esperado: 1050
print("Cliente VIP?", c1.verificar_vip())  # Esperado: True

# Resgatando pontos
c1.resgatar_pontos(50)
print(f"Pontos após resgate: {c1.pontos_fidelidade}")  # Esperado: 1000

# Criando pedido
pedido1 = Pedido(c1, p1, 2, "pendente")

# Total e peso
print("Total do pedido:", pedido1.calcular_total())  # ERRO! Veja observação abaixo
print("Peso total:", pedido1.calcular_peso_total())  # Esperado: 5.0

# Chamando o pedido
print(pedido1())  # Deve mostrar algo como "Pedido: 2X Produto: Notebook | Preço: ..."

# Atualizar status (deve falhar se tentar atualizar para o mesmo status)
try:
    pedido1.atualizar_status("pendente")
except ValueError as e:
    print("Erro ao atualizar status:", e)

# Cancelar pedido
pedido1.cancelar_pedido()
print("Status do pedido após cancelamento:", pedido1.status)  # Esperado: cancelado
