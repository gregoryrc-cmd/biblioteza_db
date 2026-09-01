import sqlite3

conn = sqlite3.connect("biblioteca.db")
conn.executemany("INSET INTO usuarios(nome) VALUER(?)", [("Bob",), ("Sam",), ("Frodo",)])
conn.commit()