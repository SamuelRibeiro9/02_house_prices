# House Prices

Primeiro projeto de machine learning desenvolvido a partir dos estudos de modelos de regressão linear.
Além disso, foi criado uma interface no streamlit para um usuário que deseja prever valores de um imóvel na região da Califórnia.

![FIGURA](imagens/house_prices.png)


## Organização do projeto

```
├── .gitignore          <- Arquivos e diretórios a serem ignorados pelo Git
├── environment.yml     <- O arquivo de requisitos para reproduzir o ambiente de análise
├── LICENSE             <- Licença de código aberto se uma for escolhida
├── README.md           <- README informações pertinentes sobre o projeto.
|
├── dados               <- Arquivos de dados para o projeto.
|
├── modelos             <- Modelos treinados e serializados, previsões de modelos ou resumos de modelos.
|
├── notebooks          <- Cadernos Jupyter. A convenção de nomenclatura é um número (para ordenação),
│                         as iniciais do criador e uma descrição curta separada por `-`, por exemplo
│                         `01-fb-exploracao-inicial-de-dados`.
│
|   └──src               <- Código-fonte para uso neste projeto.
|      │
|      ├── __init__.py   <- Torna um módulo Python
|      ├── config.py     <- Configurações básicas do projeto
|      ├── auxiliares.py <- Funções auxiliares para organização do código.
|      ├── models.py     <- Modelos que foram utilizados no projeto.
|      └── graficos.py   <- Scripts para criar visualizações exploratórias e orientadas a resultados
|
├── referencias          <- Dicionários de dados.
|
├── imagens         
│      |
|      ├── house_prices.png <- Imagem ilustrativa para o projeto.
```

## Configuração do ambiente

1. Faça o clone do repositório que será criado a partir deste modelo.

    ```bash
    git clone https://github.com/SamuelRibeiro9/02_house_prices.git
    ```

2. Crie um ambiente virtual para o seu projeto utilizando o gerenciador de ambientes de sua preferência.

    a. Caso esteja utilizando o `conda`, exporte as dependências do ambiente para o arquivo `environment.yml`:

      ```bash
      conda env create -f environment.yml --name house_prices
      ```

    b. Caso esteja utilizando outro gerenciador de ambientes, exporte as dependências
    para o arquivo `requirements.txt` ou outro formato de sua preferência. Adicione o
    arquivo ao controle de versão, removendo o arquivo `enviroment.yml`.

## Mais informações sobre a base de dados

[Clique aqui](referencias/01_dicionario_de_dados.md) para ver o dicionário de dados.
