# api-rest-embrapa
Api rest para consulta de Dados da Vitivinicultura do site da Embrapa. Esse projeto faz parte da pos-tech FIAP em Machine Learning Engineering

# Descrição

API FastAPI para fazer scraping de dados da página da Embrapa, transformando esses dados em um formato estruturado e disponibilizando-os através de endpoints RESTful.

## Instalação

- `Python 3.7 ou superior`
- `pip instalador`

## Bibliotecas

- `fastapir`
- `uvicorn`
- `httpx`
- `beautifulsoup4`
- `gunicorn`
  
## Funcionalidades

- Scraping de dados da Embrapa
- Exposição de dados através de endpoints RESTful

## Passos para uso

Instale as dependências:
```sh
pip install -r requirements.txt
```

Execute a aplicação:
```sh
uvicorn main:app --reload
```

Acesse a documentação automática da API:
Abra seu navegador e vá para http://127.0.0.1:8000/docs para acessar a documentação interativa gerada pelo FastAPI.

## Endpoints

### GET /dados/{ano}/{tipo}

Retorna os dados para um ano e tipo específicos.

#### Parâmetros

- `ano` (int): O ano para o qual os dados são solicitados.
- `tipo` (str): O tipo de dados solicitado. Valores possíveis:
  - `Producao`
  - `Processamento`
  - `Comercializacao`
  - `Importacao`
  - `Exportacao`

#### Respostas

- **200 OK**: Retorna uma lista de dicionários contendo os dados solicitados.
- **400 Bad Request**: O tipo de dados solicitado é inválido.
- **500 Internal Server Error**: Ocorreu um erro ao buscar os dados.

#### Exemplo de Requisição

```sh
curl -X GET "http://127.0.0.1:8000/dados/2023/Producao" -H "accept: application/json"
```


#### Exemplo de resposta

```
[
    {
        "Produto": "VINHO DE MESA",
        "Quantidade (L.)": "169.762.429"
    },
    {
        "Produto": "Tinto",
        "Quantidade (L.)": "139.320.884"
    },
    {
        "Produto": "Branco",
        "Quantidade (L.)": "27.910.299"
    },
    {
        "Produto": "Rosado",
        "Quantidade (L.)": "2.531.246"
    }
]
```
