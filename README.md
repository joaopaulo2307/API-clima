# 🌤️ Análise Climática de Cidades com Python

Este projeto realiza a coleta, análise e visualização de dados climáticos de diferentes cidades utilizando **Python**. Os dados são obtidos de uma API pública de clima (como a [OpenWeatherMap](https://openweathermap.org/api)) com a biblioteca `requests`. A manipulação é feita com `pandas`, e os gráficos são gerados com `matplotlib`.

## 🚀 Tecnologias Utilizadas

- **Python 3.8+**
- **Requests** – para consumo da API de clima
- **Pandas** – para análise e manipulação dos dados
- **Matplotlib** – para geração de gráficos

## 📦 Instalação

Clone este repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/projeto-clima.git
cd projeto-clima
pip install -r requirements.txt
```

## 🔑 Configuração da API

Este projeto utiliza uma API de clima. Você deve obter uma chave de API e configurar no projeto.

1. Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
API_KEY=sua_chave_da_api_aqui
```

2. Certifique-se de que a chave é mantida em segurança e não incluída em commits públicos.

## 📈 Funcionalidades

- Consulta de condições climáticas atuais em tempo real
- Análise de temperatura, umidade e outras métricas por cidade
- Visualização em gráfico das variações climáticas
- Exportação dos dados processados para `.csv`

## 📌 Requisitos

- Python 3.8 ou superior
- Chave de API válida (por exemplo, da OpenWeatherMap)
- Conexão com a internet para acessar os dados climáticos
