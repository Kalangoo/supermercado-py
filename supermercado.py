IDs = ["01","02","03","04","05","06","07","08","09","10"]
Itens = ["BANANA","MAÇÃ","BERGAMOTA","UVA","PÃO","LEITE","MEL","SALAME","QUEIJO","PRESUNTO"]
Precos = [5.00,3.00,4.00,5.00,2.50,7.00,6.90,10.00,9.50,8.50]
Sacola = []

while True:
    print("""
==================== MENU ====================
        
   Olá, seja bem vindo ao mercadinho Seu Zé

           1- Começar uma compra --
        
           2- Ir para o carrinho --

           3- Sair
""")
    
    while True:                
        try:         
            Escolha_Menu = int(input("Escreva 1, 2 ou 3 para escolher uma das opções: "))

            if Escolha_Menu in [1, 2, 3]:
                break
            else:
                print("Opção inválida, por favor tente novamente")
        except ValueError:
            print("Opção inválida, por favor tente novamente")

    if Escolha_Menu == 1:  # MENU do cliente
        while True:
            print("""
============== LISTA DE PRODUTOS =============
            
          Olá, cliente, o que deseja?
           
   Digite o ID do produto que deseja comprar
""")
            for item , preco , ID in zip(Itens , Precos , IDs) :
                print(f"             {ID} - {item}: R${preco:.2f}")
            print("\n             00 - VOLTAR\n")
            
            while True:
                try:
                    produto_id = int(input("Escolha o ID do produto: "))
                    
                    if produto_id == 0:
                        break
                    elif produto_id <= 10 and produto_id >= 1:
                        quantidade = int(input("Escolha a quantidade do produto: "))
                        produto = {"id": produto_id, "nome": Itens[produto_id-1], "preco": Precos[produto_id-1], "quantidade": quantidade}
                        Sacola.append(produto)
                        print(f"\nVocê adicionou {quantidade} {Itens[produto_id-1]} a sua sacola\n")
                    else:
                        print("Opção inválida, por favor tente novamente")
                except ValueError:
                    print("Opção inválida, por favor tente novamente")  
            break

    elif Escolha_Menu == 2:  # MENU do carrinho
        while True:
            print("""
                ============ CARRINHO ===============
            
            Olá colaborador, o que deseja?

            1- Verificar itens da compra

            2- Voltar

            3- Pagar e sair

            """)
            while True :
                try :
                    Escolha_Carrinho = int(input("Escreva 1, 2 ou 3 para escolher uma das opções: "))
                    if Escolha_Carrinho in [1, 2, 3]:
                        break
                    else:
                        print("Opção inválida, por favor tente novamente")
                except ValueError:
                    print("Opção inválida, por favor tente novamente")
            if Escolha_Carrinho == 1:
                print("Você comprou:\n")
                total = 0
                for item in Sacola:
                    print(f"{item['nome']} x {item['quantidade']} = R${item['quantidade']*item['preco']:.2f}")
                    total += item['quantidade']*item['preco']
                print(f"Total: R${total:.2f}")
                while True:
                    try:
                        remov_bool = input("Você deseja remover algo? digite (sim/não) ").lower()
                        if remov_bool in ["sim", "s","ss","sim!"]:
                            remov_nome = input("Digite o nome do item que deseja retirar: ").upper()
                            for produto in Sacola:
                                if produto['nome'] == remov_nome:
                                    quantidade_remov = int(input(f"Quantos {remov_nome} deseja remover? Digite apenas números: "))
                                    if quantidade_remov >= produto['quantidade']:
                                        Sacola.remove(produto)
                                    else:
                                        produto['quantidade'] -= quantidade_remov
                                    break
                            else:
                                print("Item não encontrado na sacola.")
                        elif remov_bool in ["não", "nao", "n","no","nao!","no!","não!"]:
                            break
                        else:
                            print("Opção inválida")
                    except ValueError:
                        print("Opção inválida")     
            elif Escolha_Carrinho == 2:
                break
            elif Escolha_Carrinho == 3:
                print("Finalizando compra...")
                total = sum(item['quantidade']*item['preco'] for item in Sacola)
                print(f"O total de sua compra é R${total:.2f}")
                senha_correta = input("Digite a senha do cartão de débito: ")
                tentativas = 3
                while tentativas > 0:
                    senha = input("Digite a senha novamente para confirmar: ")
                    if senha == senha_correta:
                        print(f"Pagamento de R${total:.2f} efetuado com sucesso!")
                        exit()
                    else:
                        tentativas -= 1
                        if tentativas > 0:
                            print("Senha incorreta! Tentativas restantes:", tentativas)
                        else:
                            print("Cartão bloqueado! Fim do programa.")
                            exit()
    elif Escolha_Menu == 3:
        print("\nAté a próxima, volte sempre!")
        break