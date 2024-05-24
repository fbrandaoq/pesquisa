# lista de nomes
nomes = ['Alex','Eduardo','Maria','Mariana','João','José','Joana','Fernanda','Fulano','Cicrano','Beltrano','Connor','Corona','Cecilia','Alexandre']

# usuário informa o nome que deseja pesquisar
nome = input('Digite o nome a ser pesquisado: ').capitalize() # a função capitalize() permite que você digite a primeira letra em minusculo mas retorna como está cadastrado

# verifica se o nome está na lista ou não
try:
#if nome in nomes:
    # retorna o indice do nome pesquisado
    indice = nomes.index(nome)
    print(f'Nome encontrado: {nome} no indice {indice}.')
except:
    print(f'{nome} não encontrado na lista')