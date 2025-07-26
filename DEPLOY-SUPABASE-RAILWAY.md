# 🚀 Deploy: Supabase + Railway

Deploy híbrido da **Clinica 360 Backend**:
- **🐘 PostgreSQL**: Supabase (100% gratuito)
- **🛤️ API**: Railway ($5 crédito/mês)

## 🎯 Por que essa combinação?

### ✅ **Vantagens:**
- **PostgreSQL gratuito** para sempre no Supabase
- **2GB storage** + backups automáticos
- **API fácil** de deployar no Railway
- **Zero configuração** de banco
- **Dashboard visual** para dados
- **APIs automáticas** do Supabase (bonus)

### 💰 **Custos:**
- **Supabase**: $0 (para sempre)
- **Railway**: ~$3-5/mês (só API)
- **Total**: ~$5/mês

## 🐘 Parte 1: Configurar PostgreSQL no Supabase

### Passo 1: Criar Conta no Supabase
```bash
1. Acesse: https://supabase.com
2. "Start your project"
3. Login com GitHub
4. Autorizar acesso
```

### Passo 2: Criar Projeto
```bash
1. "New project"
2. Configurar:
   - Organization: Sua org (ou criar nova)
   - Name: clinica-360-db
   - Database Password: [senha forte - anote!]
   - Region: South America (São Paulo)
   - Plan: Free ($0)
3. "Create new project"
4. ⏳ Aguardar criação (~2 min)
```

### Passo 3: Obter Dados de Conexão
```bash
# No dashboard do Supabase:
1. Settings → Database
2. Connection parameters:

📋 Copie estas informações:
Host: db.xxx.supabase.co
Database: postgres
Port: 5432
User: postgres
Password: [a senha que você definiu]

📋 Connection String:
postgresql://postgres:[password]@db.xxx.supabase.co:5432/postgres
```

### Passo 4: Testar Conexão Local (Opcional)
```bash
# Testar se o banco está acessível
psql "postgresql://postgres:sua_senha@db.xxx.supabase.co:5432/postgres"

# Se funcionar, você verá:
postgres=> \q
```

## 🛤️ Parte 2: Deploy da API no Railway

### Passo 1: Preparar Projeto
```bash
# Commit todas as mudanças
git add .
git commit -m "Configure for Supabase + Railway deployment"
git push origin main
```

### Passo 2: Criar Conta no Railway
```bash
1. Acesse: https://railway.app
2. "Login" → GitHub
3. Autorizar acesso aos repos
4. Verificar email se necessário
```

### Passo 3: Criar Projeto no Railway
```bash
1. Dashboard → "New Project"
2. "Deploy from GitHub repo"
3. Escolher "clinica-360-backend"
4. "Deploy Now"
5. ⏳ Aguardar build inicial (~5 min)
```

### Passo 4: Configurar Environment Variables
```bash
# No Railway Dashboard → Settings → Variables
# Adicionar estas variáveis:

ENVIRONMENT=production
DEBUG=false
SECRET_KEY=sua-chave-secreta-super-forte-aqui

# Database Supabase (usar dados do Passo 3)
DATABASE_URL=postgresql://postgres:sua_senha@db.xxx.supabase.co:5432/postgres

# CORS para frontend
BACKEND_CORS_ORIGINS=https://clinica-360.vercel.app,https://localhost:3000

# Opcional: configuração manual
POSTGRES_SERVER=db.xxx.supabase.co
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha_supabase
POSTGRES_DB=postgres
```

### Passo 5: Verificar Deploy
```bash
# Após configurar as variáveis:
1. Railway automaticamente faz redeploy
2. Verificar logs em tempo real
3. ✅ Deploy concluído!

# URLs do Railway:
🌐 API: https://clinica-360-backend-production.up.railway.app
📚 Swagger: https://[sua-url].railway.app/docs
❤️ Health: https://[sua-url].railway.app/health
```

## 🔍 Verificação Completa

### Testar Conexão com Banco
```bash
# No Railway logs, procurar por:
✅ "PostgreSQL is ready!"
✅ "Migrations completed!"
✅ "Starting FastAPI application..."

# Se der erro de conexão:
❌ Verificar DATABASE_URL
❌ Verificar senha do Supabase
❌ Verificar se IP está liberado
```

### Testar API
```bash
# Health check
curl https://sua-url.railway.app/health

# Swagger UI
open https://sua-url.railway.app/docs

# Testar endpoint
curl https://sua-url.railway.app/api/v1/
```

### Verificar Dados no Supabase
```bash
# No Supabase Dashboard:
1. Table Editor
2. Verificar se tabelas foram criadas:
   ✅ users
   ✅ patients  
   ✅ doctors
   ✅ appointments
   ✅ alembic_version
```

## 🗄️ Gerenciar Dados no Supabase

### Dashboard Visual
```bash
# Supabase oferece interface visual:
1. Table Editor: Ver/editar dados
2. SQL Editor: Executar queries
3. Database: Backups automáticos
4. API Docs: APIs REST/GraphQL automáticas
```

### Backup Manual
```bash
# Via pg_dump
pg_dump "postgresql://postgres:senha@db.xxx.supabase.co:5432/postgres" > backup.sql

# Via Supabase CLI
supabase db dump --db-url "postgresql://..."
```

### Popular com Dados Iniciais
```bash
# Executar script via Railway:
# No Railway Dashboard → Settings → Variables
# Adicionar temporariamente:
RUN_INIT_SCRIPT=true

# Ou executar manualmente:
curl -X POST https://sua-url.railway.app/admin/init-db
```

## 🔄 Deploy Automático

### GitHub Actions
```yaml
# .github/workflows/deploy.yml
name: Deploy to Railway
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Railway
        run: |
          curl -f ${{ secrets.RAILWAY_WEBHOOK_URL }}
```

### Webhook do Railway
```bash
# Configurar no Railway:
1. Settings → Webhooks
2. "Add Webhook"
3. Copiar URL
4. GitHub → Settings → Secrets → RAILWAY_WEBHOOK_URL
```

## 💡 Otimizações

### Connection Pooling
```python
# app/db/database.py
from sqlalchemy import create_engine

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300,  # 5 min
    pool_size=10,
    max_overflow=20
)
```

### Supabase Features Extras
```bash
# APIs automáticas disponíveis:
1. REST API: https://xxx.supabase.co/rest/v1/
2. GraphQL: https://xxx.supabase.co/graphql/v1
3. Auth: Sistema de autenticação
4. Storage: Upload de arquivos
5. Edge Functions: Serverless functions
```

## 🔧 Troubleshooting

### Problemas Comuns

#### 1. Erro de Conexão com Supabase
```bash
❌ "connection refused"
✅ Verificar se PASSWORD está correto
✅ Verificar se HOST está correto
✅ Tentar conexão manual com psql
```

#### 2. Railway Build Falha
```bash
❌ "dockerfile not found"
✅ Verificar se Dockerfile está na raiz
✅ Verificar se requirements.txt está correto
```

#### 3. Migrations Falham
```bash
❌ "relation already exists"
✅ Limpar banco Supabase se necessário
✅ Verificar se alembic.ini está correto
```

#### 4. CORS Errors
```bash
❌ Frontend não consegue acessar API
✅ Verificar BACKEND_CORS_ORIGINS
✅ Adicionar domínio do frontend
```

## 💰 Limites e Custos

### Supabase Free Tier:
- **500MB Database**: Suficiente para MVP
- **2GB Bandwidth**: ~50k requests/mês
- **50MB File Storage**: Para imagens
- **100MB Edge Functions**: Para lógica custom

### Railway Pricing:
- **$5 crédito/mês**: Suficiente para APIs pequenas
- **Pay-per-use**: Sem custos fixos
- **Sleep automático**: Economiza recursos

### Quando Escalar:
```bash
# Supabase Pro ($25/mês): 8GB database
# Railway Team ($20/mês): Mais recursos
# Total: ~$45/mês para produção
```

## 🎉 Vantagens desta Stack

### ✅ **Prós:**
- **Banco confiável** com backups
- **Dashboard visual** para dados
- **APIs extras** do Supabase
- **Deploy simples** no Railway
- **Monitoramento** incluído
- **Escalabilidade** fácil

### ⚠️ **Contras:**
- **Dois serviços** para gerenciar
- **Latência** entre serviços
- **Vendor lock-in** parcial

## 🔗 URLs Importantes

### Supabase:
- **Dashboard**: https://app.supabase.com
- **Docs**: https://supabase.com/docs

### Railway:
- **Dashboard**: https://railway.app/dashboard
- **Docs**: https://docs.railway.app

### Sua API:
- **API URL**: https://[projeto].up.railway.app
- **Swagger**: https://[projeto].up.railway.app/docs

## ✅ Checklist Final

### Supabase Setup:
- [ ] Projeto criado
- [ ] Senha definida
- [ ] Connection string copiada
- [ ] Conexão testada

### Railway Setup:
- [ ] Projeto deployado
- [ ] Environment variables configuradas
- [ ] Build passou
- [ ] API respondendo

### Integração:
- [ ] Migrations executadas
- [ ] Tabelas criadas no Supabase
- [ ] Health check retorna 200
- [ ] Swagger acessível

### Next Steps:
- [ ] Popular dados iniciais
- [ ] Configurar frontend
- [ ] Configurar monitoramento
- [ ] Planejar backup strategy

## 🚀 Parabéns!

Sua **Clinica 360 API** está rodando com:
- **🐘 PostgreSQL no Supabase** (gratuito)
- **🛤️ API no Railway** (~$5/mês)
- **📊 Dashboard visual** para dados
- **🔄 Deploy automático** via Git 
