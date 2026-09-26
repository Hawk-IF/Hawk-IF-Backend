# Hawk-IF-Backend
Backend do [Hawk IFRN](https://github.com/Hawk-IF/) criado com 
python e utilizando fastapi

## Sumario
- [Docs](#documentação-e-readme)
- [Rodando o Projeto](#como-rodar)

## Documentação e readme
O sistema tem seu proprio [repositorio de documentação](https://github.com/Hawk-IF/Hawk-IF-Docs)
o repositorio do backend apenas tem alguns arquivos minimos como o 
readme, para dar suporte rapido sem a necessidade de abrir outro repositorio
ou buscar dentro de pastas e arquivos gigantes


## Como Rodar
O sistema tem alguns requisitos minimos para rodar:

### Requisitos
- python (versão no arquivo [.python-version](.python-version))
- uv ou pip para gerenciar as dependencias do python
- postgresql
- git e github

### Clonando o repositorio
para clonar o repositorio basta rodar:

```bash
git clone https://github.com/Hawk-IF/Hawk-IF-Backend ./backend
```

### Baixando das dependencias do python:
com o uv use:

```bash
uv sync
```