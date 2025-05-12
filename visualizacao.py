import matplotlib.pyplot as plt
import pandas as pd

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