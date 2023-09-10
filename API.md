# Documentação da API
> **Dica** para facilitar os testes com a API utilizei a ferramente **Insomnia**.
O objetivo desse desafio era consumir a API do TMDb e armazenar os filmes populares.
Após isso é preciso criar uma task usando o celery para agendar essa busca por novos
filmes populares a cada 2 horas.
### OBS
No README, já foi informado mas sempre é bom reforçar, o projeto está utilizando a porta 8001!
# Rotas da API
## Mostrar uma lista dos 20 filmes mais populares, ordenados por popularidade.
* Rota: `/movies/`
* Método: `GET`
Resposta
```
{
		"id": 615656,
		"adult": false,
		"title": "Meg 2: The Trench",
		"overview": "An exploratory dive into the deepest depths of the ocean of a daring research team spirals into chaos when a malevolent mining operation threatens their mission and forces them into a high-stakes battle for survival.",
		"release_date": "2023-08-02",
		"vote_average": "7.0",
		"popularity": "4372.097"
	},
	{
		"id": 346698,
		"adult": false,
		"title": "Barbie",
		"overview": "Barbie and Ken are having the time of their lives in the colorful and seemingly perfect world of Barbie Land. However, when they get a chance to go to the real world, they soon discover the joys and perils of living among humans.",
		"release_date": "2023-07-19",
		"vote_average": "7.4",
		"popularity": "3486.508"
	}
```
## Apresentar detalhes de um filme específico baseado no seu ID
* Rota: `/movies/{id}/`
* Método: `GET`
Parâmetros da URL
  - `{id}` (obrigatório): O Id do filme 
Resposta
```
{
	"id": 569094,
	"adult": false,
	"title": "Spider-Man: Across the Spider-Verse",
	"overview": "After reuniting with Gwen Stacy, Brooklyn’s full-time, friendly neighborhood Spider-Man is catapulted across the Multiverse...,
	"release_date": "2023-05-31",
	"vote_average": "8.4",
	"popularity": "976.720"
}
```
## Criar um novo objeto Movie dados os necessários parâmetros
* Rota: `/movies/`
* Método: `POST`
Parâmetros do Corpo (JSON)
```
{
    "id": 3,
    "adult": false,
    "title": "Teste Filme",
    "overview": "Descrição do filme Teste",
    "release_date": "2011-11-11",
    "vote_average": "1.1",
    "popularity": "111.111"
}
```
Resposta
```
{
    "id": 3,
    "adult": false,
    "title": "Teste Filme",
    "overview": "Descrição do filme Teste",
    "release_date": "2011-11-11",
    "vote_average": "1.1",
    "popularity": "111.111"
}
```
### Fazer update do objeto Movie
* Rota: `/movies/update/{id}/`
* Método: `PUT`
Parâmetros da URL
 - `{id}` (obrigatório): O Id do filme
Parâmetros do Corpo (JSON)
```
{
    "adult": false,
    "title": "Teste Filme Put",
    "overview": "Descrição do filme Teste",
    "release_date": "2011-11-11",
    "vote_average": "1.1",
    "popularity": "111.111"
}
```
Resposta
```
{
    "id": 3,
    "adult": false,
    "title": "Teste Filme Put",
    "overview": "Descrição do filme Teste",
    "release_date": "2011-11-11",
    "vote_average": "1.1",
    "popularity": "111.111"
}
```
### Fazer update parcial do objeto Movie
* Rota: `/movies/update/{id}/`
*  Método: `PATCH`
*  Parâmetros da URL
 - `{id}` (obrigatório): O Id do filme
Parâmetros do Corpo (JSON)
```
{
    "title": "Teste Filme Patch 1",
}
```
Resposta
```
{
    "id": 3,
    "adult": false,
    "title": "Teste Filme Patch 1",
    "overview": "Descrição do filme Teste",
    "release_date": "2011-11-11",
    "vote_average": "1.1",
    "popularity": "111.111"
}
```
