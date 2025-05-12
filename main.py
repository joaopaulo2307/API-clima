from clima_app import buscar_clima
from db import inicializar_db, salvar_dados, exibir_historico
from visualizacao import gerar_grafico

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