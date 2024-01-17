import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='!nteligenci@',
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
    resultado = cursor.fetchall()  # ler o banco de dados


#------------------------------------------------------------------------------------------
def read():
    comando = f'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)


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

escolha = input('Digite ( 1 ) para ver a lista\n Digite ( 2 ) para adicionar itens a lista\n Digite ( 3 ) para editar itens da lista\nDigite ( 4 ) para excluir itens da lista\n')
if escolha =='1':
    read()
elif escolha == '2':
    create()
elif escolha == '3':
    update()
elif escolha == '4':
    delete()
else:
    print("Nenhuma das opções que voce digitou é válido\n certifique que digitou corretamente o número que corresponda o comando.")

cursor.close()
conexao.close()
#------------------------------------------------------------------------------------------