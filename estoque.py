class ItemEstoque:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome 
        self.quantidade = quantidade
        self.preco = preco

lista_itens = []
soma = 0
#função adicionar
def adicionar_itens():
    
    nome = str(input("Nome do item:"))
    quantidade = int(input("Quantidade:"))
    preco = float(input("Preço: "))
    item = ItemEstoque(nome, quantidade, preco)
    lista_itens.append(item)

#função mostrar
def mostrar_estoque():
    if len(lista_itens) == 0:
        print("Estoque vazio")

while True:

    print("1- Adicionar itens\n"
        "2- Ver itens disponivel no estoque\n"
        "3- Stop")

    escolha = int(input("Escolha um numero: "))

    if escolha == 1:
        adicionar_itens()

        
    elif escolha == 2:
        mostrar_estoque()
        for item in lista_itens:
            print(f"Nome: {item.nome}\n"
                  f"Quantidade: {item.quantidade}\n"
                  f"Preço: {item.preco}\n")
            
            soma = item.quantidade * item.preco
            print(f"O valor do estoque é: {soma}")
        
           
    else: 
        if escolha == 3:      
            break
        
