# Search News

### Sobre

Projeto que permite a pesquisa de notícias, de diferentes gêneros, em fontes como G1, Omelete e Tecmundo. Foi utilizada a técnica de webscraping em Python 3, além do framework Django 2.

### Tecnologias

- Python 3
- Django 2
- Webscraping
- Utilização de bibliotecas como _request_ e _Beautiful Soup_

### Instalação do projeto

- Realizar o clone do projeto

        git clone https://github.com/USER/search-news.git

- Instalar as dependências

        pip install -r requirements.txt

- Criar um arquivo ".env" semelhante ao ".env-example", alterando para as credenciais adequadas.

        Exemplo: cp .env_example .env

- Executar migrations pendentes

        python manage.py migrate

- Executar o projeto

        python manage.py runserver
