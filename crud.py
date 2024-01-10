import mysql.connector

conexao = mysql.connector.connect( #estou usando um servidor local então para funcionar é preciso que preencha com os dados do seu proprio servidor.
    host='localhost',
    user='root',
    password='102030',
    database='crud',
)
cursor = conexao.cursor()

#crud

nome_produto = "patrimonio"
valor = 1
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() # edita no banco de dados
resultado = cursor.fetchall() # ler o banco de dados



cursor.close()
conexao.close()


 # CREATE
# nome_produto = "computador"
#valor = 3
#comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
#cursor.execute(comando)
#conexao.commit() # edita no banco de dador
#resultado = cursor.fetchall() # ler o banco de dados

 # READ
#omando = f'SELECT * FROM vendas'
#cursor.execute(comando)
#resultado = cursor.fetchall()
#print(resultado)


 # UPDATE
#nome_produto = "computador"
#valor = 2
#comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit() #edita o banco de dados

 # DELETE
#nome_produto = "computador"
#comando =f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit()