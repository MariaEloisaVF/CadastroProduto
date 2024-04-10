#Codigo em python para realizar o cadastro de produtos

def exibir_menu():
	#função de menu principal para escolha de opções
  print('''Escolha uma opção:

	1. Cadastrar
	2. Listar 
	3. Procurar 
	4. Remover
	5. Encerrar
	''')


def cadastrar(produtos):
	#função para receber os dados do produto
  codigo = int(input('Código: '))
  nome = input('Nome: ')
  valor = float(input('Valor: R$ '))
  produtos.append((codigo, nome, valor))


def listar(produtos):
	#função para listar os produtos cadastrados utilizando de um FOR para percorrer a lista
  for produto in produtos:
    codigo, nome, valor = produto
    print(f'Nome: {nome}, Valor: {valor}, Código: {codigo}')

def buscar(produtos):
	#função para buscar um produto pelo código usando de um FOR para percorrer a lista e um IF para verificar se o código digitado é igual ao código do produto
  codigo_desejado = int(input('Código: '))
  encontrado = False
  for produto in produtos:
    codigo, nome, valor = produto
    if codigo == codigo_desejado:
      print(f'Nome: {nome}, Valor: {valor}, Código: {codigo}')
      encontrado = True
  if not encontrado:
    print(f'Produto com código {codigo_desejado} não encontrado')


def remover(produtos):
	#função para remover um produto pelo código usando de um FOR para percorrer a lista e buscar o elemento com o código desejado e o remove da lista
  codigo = int(input('Código: '))
  produtos = [produto for produto in produtos if produto[0] != codigo]
  print('Produto Removido')


def encerrar(produtos):
	#função para encerrar o programa
  print('Programa Encerrado')
  quit()


def main():
  produtos = [] #lista para armazenar os produtos

  while True:
		#neste comando de repetição o programa irá continuar rodando até que o usuário digite uma opção válida ou sair do programa
    exibir_menu()
    opcao = int(input('Opção--> '))
    if opcao == 1:
      cadastrar(produtos)
    elif opcao == 2:
      listar(produtos)
    elif opcao == 3:
      buscar(produtos)
    elif opcao == 4:
      remover(produtos)
    elif opcao == 5:
      encerrar(produtos)
    else:
      print('Opção Inválida')

if __name__ == "__main__":
  main()
