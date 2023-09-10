# miio-desafio-tecnico
Projeto feito para o desafio técnico da miio de criar uma API RESTful de filmes

## Como configurar e executar esse projeto
## Via Docker
### 1 - Realizando o docker-compose para criar as imagens e containers
Para realizar isso basta executar esse comando abaixo.
```
docker-compose up -d --build       
```
Após executar esse comando o projeto será dockerizado.
### 2 - Acessando o container
```
docker exec -it miio-django /bin/sh
```
Ao executar esse comando você estará acessando o container.
Dessa forma poderá realizar os comandos do django que utilizam manage.py.
### 3 - Executando o script para povoar o banco inicialmente.
Ao entrar no container, é necessário executar um script para consumir a API do TMDb.
Dessa forma o banco terá alguns filmes.
Siga os comandos abaixo para realizar corretamente.
```
python manage.py shell
```
Com isso estará acessando o shell do projeto.
Após isso basta executar o script.
```
exec(open("init_script.py").read())
```
Pronto. O banco agora possui dados da API do TMDb
### 4 - Criando um superuser
Primeiramente, execute um 'ls' para saber se está no mesmo diretorio onde está o 'manage.py'.
Caso esteja, realize o seguinte comando.
```
python manage.py createsuperuser
```
Ao executar este comando, crie o seu usuário.
Após criar o usuário, agora é possivel acessar a parte do admin do projeto
### OBS
  - Ao realizar o docker-compose, já está setado para executar as migrations.
  - Pode ser utilizado tanto localhost:portas ou 127.0.0.1:portas
  - O projeto está utilizando a porta 8001.
  - Na porta 5050, poderá acessar o pgAdmin referente ao banco do container:
    - usuario: postgres@hotmail.com
    - senha: postgres
  - Após se conectar é necessario adicionar o server referente ao banco:
    - host name/adress: db
    - port: 5432
    - username: postgres
    - password: postgres
  - Pronto. Agora poderá visualizar o banco que está sendo utilizado pelo pgAdmin.
  - A documentação da API está na API.md.
