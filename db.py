import sqlite3
import pandas as pd

DB_NAME = 'clima.db'

def inicializar_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clima (
                    id INTEGER PRIMARY KEY,
                    cidade TEXT,
                    temperatura REAL,
                    umidade INTEGER,
                    descricao TEXT,
                    data TEXT
                )''')
    conn.commit()
    conn.close()

def salvar_dados(clima):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''INSERT INTO clima (cidade, temperatura, umidade, descricao, data)
                 VALUES (?, ?, ?, ?, ?)''',
              (clima['cidade'], clima['temperatura'], clima['umidade'], clima['descricao'], clima['data']))
    conn.commit()
    conn.close()

def exibir_historico(cidade):
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM clima WHERE cidade = ? ORDER BY data DESC", conn, params=(cidade,))
    conn.close()
    print(df)
    return df