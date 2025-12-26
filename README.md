# Simple Flask Authentication API

Uma API REST simples de autenticação desenvolvida com Flask, que permite registro, login, logout e gerenciamento de usuários.

## 📋 Sobre o Projeto

Esta é uma API de autenticação básica que implementa funcionalidades de:
- Registro de novos usuários
- Login e logout
- Visualização de perfil de usuário
- Atualização de senha
- Exclusão de usuários

## 🛠️ Tecnologias Utilizadas

- **Flask** 3.1.2 - Framework web Python
- **Flask-Login** 0.6.3 - Gerenciamento de sessões de usuário
- **Flask-SQLAlchemy** 3.1.1 - ORM para banco de dados
- **SQLAlchemy** 2.0.45 - Biblioteca ORM
- **SQLite** - Banco de dados relacional
- **Werkzeug** 3.1.4 - Utilitários WSGI

## 📡 Endpoints da API

### 1. Registro de Usuário
**POST** `/register`

Cria um novo usuário no sistema.

**Body:**
```json
{
    "username": "nome_usuario",
    "password": "senha123"
}
```

**Resposta de Sucesso (200):**
```json
{
    "message": "Usuário nome_usuario criado com sucesso"
}
```

**Resposta de Erro (400):**
```json
{
    "message": "Já existe um usuário com esse username"
}
```
ou
```json
{
    "message": "O username e senha são obrigatórios"
}
```

---

### 2. Login
**POST** `/login`

Autentica um usuário no sistema.

**Body:**
```json
{
    "username": "nome_usuario",
    "password": "senha123"
}
```

**Resposta de Sucesso (200):**
```json
{
    "message": "Login Realizado com sucesso"
}
```

**Resposta de Erro (400):**
```json
{
    "message": "Credenciais Inválidas"
}
```

---

### 3. Logout
**GET** `/logout`

Encerra a sessão do usuário autenticado.

**Headers:**
- Requer autenticação (sessão ativa)

**Resposta de Sucesso (200):**
```json
{
    "message": "Logout realizado com sucesso"
}
```

---

### 4. Obter Perfil do Usuário
**GET** `/users/<user_id>`

Retorna informações do perfil de um usuário específico.

**Headers:**
- Requer autenticação (sessão ativa)

**Parâmetros:**
- `user_id` (int) - ID do usuário

**Resposta de Sucesso (200):**
```json
{
    "user": {
        "username": "nome_usuario"
    }
}
```

**Resposta de Erro (404):**
```json
{
    "message": "Usuário não encontrado"
}
```

---

### 5. Atualizar Senha do Usuário
**PUT** `/users/<user_id>`

Atualiza a senha de um usuário específico.

**Headers:**
- Requer autenticação (sessão ativa)

**Parâmetros:**
- `user_id` (int) - ID do usuário

**Body:**
```json
{
    "password": "nova_senha"
}
```

**Resposta de Sucesso (200):**
```json
{
    "message": "A senha do usuário nome_usuario foi editado com sucesso"
}
```

**Resposta de Erro (400):**
```json
{
    "message": "Senha é obrigatória"
}
```

**Resposta de Erro (404):**
```json
{
    "message": "Usuário não encontrado"
}
```

---

### 6. Excluir Usuário
**DELETE** `/users/<user_id>`

Remove um usuário do sistema.

**Headers:**
- Requer autenticação (sessão ativa)

**Parâmetros:**
- `user_id` (int) - ID do usuário

**Resposta de Sucesso (200):**
```json
{
    "message": "O usuário foi excluido com sucesso"
}
```

**Resposta de Erro (401):**
```json
{
    "message": "Não permitido"
}
```
*Nota: Não é permitido excluir o próprio usuário*

**Resposta de Erro (404):**
```json
{
    "message": "Usuário não encontrado"
}
```

## 📁 Estrutura do Projeto

```
estudos/
├── app.py                 # Aplicação principal Flask
├── database.py           # Configuração do SQLAlchemy
├── models/
│   └── User.py           # Modelo de usuário
├── instance/
│   └── database.db       # Banco de dados SQLite
├── requirements.txt      # Dependências do projeto
├── api.http              # Exemplos de requisições HTTP
└── README.md             # Este arquivo
```
