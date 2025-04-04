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
    


