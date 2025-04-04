class Produto:
    
    def __init__(self, nome, preco, estoque, peso_kg):
        self.nome = nome
        self.preco =preco
        self.estoque = estoque
        self.peso_kg = peso_kg

    def novo_preco (self, novo_preco):
        if novo_preco > 0 :
            self.preco = novo_preco
    
    def aplicar_desconto (self, percentual):
        percentual1 = percentual / 100

        self.preco = self.preco * percentual1

    def verificar_estoque (self) :
        if self.estoque < 5 :
            return True
        else :
            return False
        
    def __eq__(self, value):
        if self.nome == value.nome and self.preco == value.preco :
            return True
        else :
            return False
    
    def __str__(self):
        return f"Produto: {self.nome} | Preço: R$ {self.preco} | Estoque: {self.estoque}"
    

p1 = Produto("Arroz", 5, 100, 1)
p2 = Produto("Feijão", 5, 100, 1)

print(p1.verificar_estoque())
print(p1.__str__())

p1.novo_preco(10)
print(p1.__str__())

p1.aplicar_desconto(10)
print(p1.__str__())