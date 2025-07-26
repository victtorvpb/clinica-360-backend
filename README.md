# Clinica 360 Backend

Backend for **Clinica 360** application built with **FastAPI**, **PostgreSQL** and **Docker**.

## 🚀 Technologies

- **FastAPI** - Modern and fast web framework for Python
- **PostgreSQL** - Relational database
- **SQLAlchemy** - ORM for Python
- **Alembic** - Database migrations
- **Docker** - Application containerization
- **Pydantic** - Data validation

## 📁 Project Structure

```
clinica-360-backend/
├── app/
│   ├── api/                 # API endpoints
│   │   └── api_v1/
│   │       ├── endpoints/   # Endpoints organized by module
│   │       └── api.py       # Main router
│   ├── core/               # Core configurations
│   │   └── config.py       # Application settings
│   ├── db/                 # Database configuration
│   │   └── database.py     # SQLAlchemy setup
│   ├── models/             # SQLAlchemy models
│   │   ├── user.py
│   │   ├── patient.py
│   │   ├── doctor.py
│   │   └── appointment.py
│   └── main.py             # Main FastAPI application
├── alembic/                # Database migrations
├── docker-compose.yml      # Docker services
├── Dockerfile              # Application container
├── requirements.txt        # Python dependencies
└── README.md
```

## 🏥 Funcionalidades

### Entidades Principais

- **👤 Usuários**: Sistema de autenticação e autorização
- **🏥 Pacientes**: Cadastro completo com dados pessoais e médicos
- **👨‍⚕️ Médicos**: Gestão de médicos com especialidades e CRM
- **📅 Consultas**: Agendamento e gestão de consultas médicas

### Endpoints da API

- `GET /api/v1/patients` - Listar pacientes
- `POST /api/v1/patients` - Criar paciente
- `GET /api/v1/patients/{id}` - Obter paciente
- `PUT /api/v1/patients/{id}` - Atualizar paciente
- `DELETE /api/v1/patients/{id}` - Deletar paciente

- `GET /api/v1/doctors` - Listar médicos
- `POST /api/v1/doctors` - Criar médico
- E outros endpoints para médicos...

- `GET /api/v1/appointments` - Listar consultas (com filtros)
- `POST /api/v1/appointments` - Agendar consulta
- E outros endpoints para consultas...

## 🛠️ Configuração e Instalação

### Pré-requisitos

- Docker e Docker Compose
- Python 3.11+ (se rodando localmente)

### 1. Setup and Configure

```bash
# Navigate to directory
cd clinica-360-backend

# Quick setup (creates .env and directories)
python scripts/setup.py

# OR manual setup:
# Copy environment file
cp env.example .env

# Edit variables if needed
nano .env
```

### 2. Run with Docker (Recommended)

```bash
# Start PostgreSQL and application
docker-compose up -d

# View logs
docker-compose logs -f api

# OR use Makefile commands:
make up        # Start services
make logs      # View logs
make swagger   # Generate OpenAPI file
```

### 3. Executar Migrações

```bash
# Criar primeira migração (se necessário)
docker-compose exec api alembic revision --autogenerate -m "Initial migration"

# Aplicar migrações
docker-compose exec api alembic upgrade head
```

### 4. Instalação Local (Alternativa)

```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Rodar apenas o PostgreSQL
docker-compose up -d postgres

# Executar migrações
alembic upgrade head

# Iniciar aplicação
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 🌐 Access

- **API**: <http://localhost:8000>
- **Swagger Documentation**: <http://localhost:8000/docs>
- **ReDoc**: <http://localhost:8000/redoc>
- **OpenAPI JSON**: <http://localhost:8000/api/v1/openapi.json>
- **PostgreSQL**: localhost:5432

### Credenciais do Banco (Desenvolvimento)

- **Host**: localhost
- **Porta**: 5432
- **Usuário**: clinica_user
- **Senha**: clinica_password
- **Database**: clinica_360

## 📋 Comandos Úteis

### Docker

```bash
# Subir serviços
docker-compose up -d

# Ver logs
docker-compose logs -f

# Parar serviços
docker-compose down

# Rebuild da aplicação
docker-compose up -d --build api

# Acessar container da API
docker-compose exec api bash
```

### Banco de Dados

```bash
# Criar nova migração
alembic revision --autogenerate -m "Descrição da mudança"

# Aplicar migrações
alembic upgrade head

# Voltar migração
alembic downgrade -1

# Ver histórico
alembic history

# Acessar PostgreSQL diretamente
docker-compose exec postgres psql -U clinica_user -d clinica_360
```

### Desenvolvimento

```bash
# Rodar com reload automático
uvicorn app.main:app --reload

# Formatar código (se usar black)
black app/

# Verificar tipagem (se usar mypy)
mypy app/
```

## 🔧 Configuração de Ambiente

### Variáveis `.env`

```env
# Database
POSTGRES_SERVER=localhost
POSTGRES_USER=clinica_user
POSTGRES_PASSWORD=clinica_password
POSTGRES_DB=clinica_360
POSTGRES_PORT=5432

# Security
SECRET_KEY=your-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=11520

# CORS (para frontend)
BACKEND_CORS_ORIGINS=http://localhost:3000,http://localhost:5173

# Debug
DEBUG=True
```

## 🚀 Deploy

### Opções de Deploy

1. **🆓 Render (100% gratuito)**: Ver `DEPLOY-RENDER.md` 
2. **💰 VPS barato ($5/mês)**: Ver `DEPLOY-VPS.md`
3. **✈️ Fly.io (tier gratuito)**: Via CLI `flyctl`

### Deploy Local para Produção

```bash
# Exemplo para produção
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## 🧪 Próximos Passos

- [ ] Implementar autenticação JWT completa
- [ ] Adicionar validações Pydantic (schemas)
- [ ] Implementar CRUD completo para todas entidades
- [ ] Adicionar testes unitários
- [ ] Configurar CI/CD
- [ ] Adicionar logs estruturados
- [ ] Implementar cache com Redis
- [ ] Adicionar documentação da API

## 🤝 Contribuição

1. Faça fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT.
