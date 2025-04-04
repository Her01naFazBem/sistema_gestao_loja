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

        self.preco = self.preco * percentual1

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
    def __init__(self, cliente : Cliente, produto : Produto, quantidade, status):
        if status.lower() not in ["pendente", "processando", "Entregue"] :
            raise ValueError ("Status inválido")
        
        self.cliente = cliente
        self.produto = produto
        self.quantidade : int = quantidade
        self.status : str = status

    def calcular_total (self):
        return self.preco * self.quantidade * self.produto.preco

    def calcular_peso_total (self):
        return self.quantidade * self.produto.peso_kg
    
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