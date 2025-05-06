# Gestão de Bandas e Músicas

Este projeto é uma aplicação web simples desenvolvida com **Flask** (Python) que permite gerir bandas e as suas músicas. Inclui funcionalidades para adicionar, editar e apagar bandas e músicas de forma prática, sem necessidade de base de dados (armazenamento mockado em memória).

## Funcionalidades

- Autenticação simples de utilizador (login/logout)
- Adicionar novas bandas
- Editar nome das bandas
- Apagar bandas
- Adicionar músicas a uma banda
- Editar e apagar músicas

## Tecnologias Utilizadas

- **Flask**: Framework web em Python
- **HTML/CSS**: Front-end simples com formulários organizados

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute a aplicação:
   ```bash
   flask run
   ```

## Estrutura

- `app.py`: Lógica principal da aplicação Flask
- `templates/`: Contém os ficheiros HTML
- `requirements.txt`: Dependências do projeto

## Notas

- Os dados são mantidos em memória, ou seja, perdem-se quando a aplicação reinicia.
- Para persistência real, pode-se adicionar uma base de dados no futuro.

---

Feito em Flask. Saiba mais em [https://gptonline.ai/pt/](https://gptonline.ai/pt/)
