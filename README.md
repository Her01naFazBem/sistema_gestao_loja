# sistema_gestao_loja
1. Classe 
Produto
 Atributos:
 nome (string)
 preco (float)
estoque (int)
 peso_kg (float, peso unitário do produto)
 Métodos:
 atualizar_preco(novo_preco) → Valida se 
novo_preco > 0 e atualiza.
 aplicar_desconto(percentual) → Aplica desconto ao preço (ex: 10% → preço * 0.9).
 verificar_estoque_baixo() → Retorna 
True se estoque < 5.
 Métodos Especiais/Sobrecarga:
 __eq__(self, other) → Compara produtos pelo nome e preço.
 __str__(self) → Retorna 
[estoque]" .
 "Produto: [nome] | Preço: R$ [preco] | Estoque:
 2. Classe 
Cliente
 Atributos:
 nome (string)
 email (string)
 pontos_fidelidade (int, inicial 0)
 Métodos:
 adicionar_pontos(pontos) → Adiciona pontos de fidelidade (apenas valores positivos).
 resgatar_pontos(pontos) → Remove pontos (não permite negativo).
 verificar_vip() → Retorna 
Métodos Especiais/Sobrecarga:
 True se pontos >= 1000.
 __eq__(self, other) → Compara clientes pelo e-mail.
 __iadd__(self, pontos) → Sobrecarga de 
+= para adicionar pontos.
 __str__(self) → Retorna 
"Cliente: [nome] | Pontos: [pontos_fidelidade]" .
 3. Classe 
Pedido
 Atributos:
cliente (instância de 
Cliente )
 produto (instância de 
Produto )
 quantidade (int)
 status (string: "pendente", "processando", "entregue")
 Métodos:
 calcular_total() → Retorna 
preco * peso_total .
 calcular_peso_total() → Retorna 
peso_kg * quantidade .
 atualizar_status(novo_status) → Valida transições (ex: não permite voltar de
 "entregue" para "pendente").
 cancelar_pedido() → Só permite cancelar se status for "pendente".
 Métodos Especiais/Sobrecarga:
 __add__(self, other) → Combina pedidos do mesmo cliente, somando quantidades
 se o produto for igual.
 __lt__(self, other) → Compara pelo peso total do pedido.
 __call__(self) → Retorna uma string com resumo do pedido (ex: 
"Pedido: 2x Camiseta").