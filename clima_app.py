
import requests
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# CONFIGURAÇÕES
API_KEY = '059893380e306cd99bdbb8cbd5625e9c'  # Substitua pela sua chave da OpenWeatherMap
DB_NAME = 'clima.db'

# ----- Funções de acesso à API -----
def buscar_clima(cidade):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        clima = {
            'cidade': cidade,
            'temperatura': dados['main']['temp'],
            'umidade': dados['main']['humidity'],
            'descricao': dados['weather'][0]['description'],
            'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        return clima
    else:
        print("Erro ao buscar dados do clima.")
        return None

# ----- Funções de banco de dados -----
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

# ----- Visualização -----
def exibir_historico(cidade):
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM clima WHERE cidade = ? ORDER BY data DESC", conn, params=(cidade,))
    conn.close()
    print(df)
    return df

def gerar_grafico(df):
    if df.empty:
        print("Nenhum dado para exibir no gráfico.")
        return
    df['data'] = pd.to_datetime(df['data'])
    plt.figure(figsize=(10, 5))
    plt.plot(df['data'], df['temperatura'], marker='o', label='Temperatura (°C)')
    plt.title(f"Histórico de Temperatura - {df['cidade'].iloc[0]}")
    plt.xlabel("Data")
    plt.ylabel("Temperatura (°C)")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.show()

# ----- Execução principal -----
def main():
    inicializar_db()
    while True:
        print("\n1. Buscar clima\n2. Exibir histórico\n3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cidade = input("Digite o nome da cidade: ")
            clima = buscar_clima(cidade)
            if clima:
                print(clima)
                salvar_dados(clima)
        elif opcao == '2':
            cidade = input("Digite o nome da cidade: ")
            df = exibir_historico(cidade)
            gerar_grafico(df)
        elif opcao == '3':
            break
        else:
            print("Opção inválida.")

if __name__ == '__main__':
    main()
