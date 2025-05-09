# 🔐 Projeto de Autenticação e Segurança com Flask, JWT e Bcrypt

Este projeto demonstra como construir uma API segura usando o microframework **Flask**, com autenticação baseada em **JWT** e criptografia de senhas com **Bcrypt**. A arquitetura segue o padrão **MVC (Model-View-Controller)** e faz uso de **variáveis de ambiente com dotenv** para armazenar informações sensíveis.

---

## 📁 Estrutura de Pastas


## 🧪 Funcionalidades

- ✅ Registro de usuários com senha criptografada
- 🔐 Login seguro e emissão de JWT
- ✅ Validação de token JWT em rotas protegidas
- 📦 Uso de variáveis de ambiente com `.env`
- 🧱 Organização do código com arquitetura **MVC**
- 🔒 Segurança com `bcrypt` e `pyjwt`

---

## 🚀 Como executar o projeto

### 1. Clonar o repositório

```
git clone https://github.com/taleshmm/ProjetoAutenticacaoESeguranca.git
cd ProjetoAutenticacaoESeguranca
```

### 2. Criar e ativar um ambiente virtual

```
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instalar as dependências

```
pip install -r requirements.txt
```

### 4. Criar um arquivo `.env`

```
SECRET_KEY=sua_chave_secreta_aqui
JWT_SECRET=sua_jwt_secret
DATABASE_URL=sqlite:///storage.db
```

### 5. Executar o servidor Flask

```
python run.py
```

---

## 🔐 Segurança

* **JWT** é usado para autenticação sem estado (stateless).
* **Bcrypt** garante senhas armazenadas de forma segura com salt.
* **Variáveis sensíveis** são mantidas fora do código com `.env`.

---

## 📚 Conceitos aprendidos

* Como estruturar uma aplicação Flask com MVC
* Como usar `bcrypt` para proteger senhas
* Como gerar e validar tokens JWT
* Como lidar com erros e exceções na API
* Como organizar variáveis sensíveis com dotenv


