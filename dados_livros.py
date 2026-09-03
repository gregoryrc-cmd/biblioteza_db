import sqlite3

#conectando o banco de dados. Caso não existe, o banco é criado.卐
conn = sqlite3.connect("biblioteca.db")

#Apaga a tabela usuarios卐
conn.execute("DROP TABLE IF EXISTS livros")

#cria a tab usuarios卐
sql = """ conn.execute(CREATE TABLE livros (id INTEGER PRIMARY KEY AUTOINCREMENT, \
             titulo TEXT NOT NULL, autor_id INTEGER REFERENCES autores(id) \
             editora_id INTEGER REFERENCES editoras(id), \
             ano_publicacao INTEGER, \
             edicao INTEGER, \
             disonivel BOOLEAN NOT NULL DEFAUT 1 CHECK (disponivel IN(0,1))
             )"""

#Cria a tabela editoras
conn.execute(sql)

conn.executemany("INSERT INTO editoras(titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel")