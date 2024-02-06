import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='@dma9#ti$10',
    database='crud',
)
cursor = conexao.cursor()

#--------estou usando um servidor local então para funcionar é preciso que preencha com os dados do seu proprio servidor.----------------------------------------------------------------------------------
#----------------------------------funções--------------------------------------------------------
def create():
    nome_produto = input('Digite o nome do produto que você deseja adicionar:  ')
    valor = int(input('Digite quantas unidades deste: '))
    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
    cursor.execute(comando)
    conexao.commit()  # edita no banco de dados

#------------------------------------------------------------------------------------------
def read():
    comando = f'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print('-----------------------------------------')
    print('Tipos de itens: ', len(resultado))
    print('--------------LISTA-----------------')
    for row in resultado:
        #print('Total de itens já adicinados na lista : ', row[0])
        print('Nome do produto: ', row[1])
        print('Quantidade: ', row[2])
        print('-----------------------------------------')
    minimo = 5
    for row in resultado:
            if row[2] <= minimo:
                print('Você está quase sem estoque deste produto: ', row[1])

#------------------------------------------------------------------------------------------
def update():
    nome_produto = input('Digite o nome do produto que deseja alterar: ')
    valor = input('Quantidade: ')
    comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados


#------------------------------------------------------------------------------------------
def delete():
    nome_produto = input('Digite o iten que deseja excluir: ')
    comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    conexao.commit()


#---------------------------------crud Programa principal---------------------------------------------------------
def menu_operacoes():
 while True:
    menu = input(' Digite (1) para ver a lista\n Digite (2) para adicionar itens à lista\n Digite (3) para editar itens da lista\n Digite (4) para excluir itens da lista\n Digite (0) para sair\n')
    if menu == '1':
        read()
    elif menu == '2':
        create()
    elif menu == '3':
        update()
    elif menu == '4':
        delete()
    elif menu =='0':
        break
    else:
        print("Nenhuma das opções que você digitou é válida. Certifique-se de digitar corretamente o número correspondente ao comando.")

    cursor.close()
    conexao.close()
menu_operacoes()
#------------------------------------------------------------------------------------------