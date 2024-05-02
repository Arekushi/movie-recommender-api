<h1 align="center">
    Movie Recommender API
</h1>

<p align="center">
    <a href="#" target="blank">
        <img
            src="./assets/movie-icon.svg"
            width="200"
            title="Project Icon"
            alt="Project Icon"
        />
    </a>
</p>

<p align="center">
    🚧 Mais detalhamento em breve.
    <br>
    English version of this README.md <a href="https://github.com/Arekushi/movie-recommender-api/blob/master/README.en.md">here</a>
</p>


## Sobre o Projeto
🚧 Mais detalhamento em breve.


## Construído com
- [Python 3.10.14][python]
- [Prisma v5.13.0/Prisma Client Python v0.13.1][prisma]
- [Strawberry v0.227.3][strawberry]


## Primeiros passos
Se quiser o projeto para desenvolver, alguns pré-requisitos são necessários.


### Pré-requisitos (Windows)
* Python
    1. Você pode baixar aqui: [Python][python]
    2. Aqui tem um tutorial passo-a-passo. [(Tutorial)][python_tutorial]
        1. Tutorial com Miniconda. [(Tutorial)][miniconda_tutorial]
* Poetry
    1. Você pode instalar aqui: [Poetry][poetry]


### Variáveis .env
> Você precisa criar um arquivo `.env` dentro da pasta raíz.
```python
DATABASE_URL="mongodb+srv://..."
HOST_URL="127.0.0.1"
HOST_PORT="8080"
RELOAD="1"
```


### Instalação
1. Clone o repositório.
    ```sh
    git clone https://github.com/Arekushi/movie-recommender-api.git
    ```
2. Instale os pacotes com o `Poetry`
    ```sh
    poetry install
    ```
3. Execute no terminal:
    ```sh
    prisma py generate
    ```
4. Para finalizar, execute:
    ```sh
    python main.py
    ```
5. Prontinho, o projeto já está executando 🎉

## Reconhecimentos
Aqui está um [link][acknowledgments] onde você pode ver todo o material que usamos para construir o projeto. 😉

## Professores orientadores
| [<div><img width=115 src="https://avatars.githubusercontent.com/u/31980070?v=4"><br><sub>Luan Fernandes</sub></div>][luan] <div title="Guide">📚</div> |
| :---: |

## Contribuidores
| [<div><img width=115 src="https://avatars.githubusercontent.com/u/54884313?v=4"><br><sub>Alexandre Ferreira de Lima</sub></div>][arekushi] <div title="Code">💻</div> | [<div><img width=115 src="https://avatars.githubusercontent.com/u/4665684?v=4"><br><sub>Shyrles Monteiro</sub></div>][shyrles] <div title="Code">💻</div> | [<div><img width=115 src="https://avatars.githubusercontent.com/u/91470759?v=4"><br><sub>Ariane Cristina Costa Dias</sub></div>][ariane] <div title="Code">💻</div> | [<div><img width=115 src="https://avatars.githubusercontent.com/u/90654164?v=4"><br><sub>Diego Silva Neves</sub></div>][diego] <div title="Code">💻</div> | [<div><img width=115 src="https://avatars.githubusercontent.com/u/91035018?v=4"><br><sub>Ana Carolina Ferreira de Camargo</sub></div>][ana] <div title="Code">💻</div> | [<div><img width=115 src="https://avatars.githubusercontent.com/u/86978502?v=4"><br><sub>Mychelle Roberto Veloso</sub></div>][myche] <div title="Code">💻</div> |
| :---: | :---: | :---: | :---: | :---: | :---: |


<!-- [Build With] -->
[python]: https://www.python.org/downloads/
[python_tutorial]: https://www.digitalocean.com/community/tutorials/install-python-windows-10
[miniconda_tutorial]: https://katiekodes.com/setup-python-windows-miniconda/
[poetry]: https://python-poetry.org/docs/#installation
[prisma]: https://github.com/RobertCraigie/prisma-client-py
[strawberry]: https://strawberry.rocks/docs

<!-- [Some links] -->
[acknowledgments]: https://arekushi.notion.site/Acknowledgments-826db5a25cbf4f629640641cbd3ab917?pvs=4

<!-- [Constributors] -->
[arekushi]: https://github.com/Arekushi
[shyrles]: https://github.com/Shyrles
[ariane]: https://github.com/arianeccdias
[diego]: https://github.com/nevesbattousai
[ana]: https://github.com/Anakaita
[myche]: https://github.com/mychveloso
[luan]: https://github.com/souluanf
