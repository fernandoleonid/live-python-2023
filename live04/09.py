import pymysql

conn = pymysql.connect(host='localhost', user='root', password='', database='estoquedb')

cursor = conn.cursor()

# Inserindo dados
sql = 'INSERT INTO produtos (nome, preco, quantidade) VALUES (%s, %s, %s)'
cursor.execute(sql,('Mesa', '100.90', '300'))
conn.commit()

# Atualizar dados
sql = 'UPDATE produtos SET preco=%s, quantidade=%s WHERE nome=%s'
cursor.execute(sql, ('999','777','Mouse'))
conn.commit()


# Mostrando todos dos dados
cursor.execute('SELECT * FROM produtos')

for linha in cursor:
    print(f" => {linha}")

# Fim

cursor.close()
conn.close()