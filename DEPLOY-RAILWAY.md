# 🚀 Deploy Clinica 360 Backend no Railway

Guia passo-a-passo para fazer deploy da API FastAPI no Railway.

## 📋 Pré-requisitos

- ✅ Projeto no GitHub (pode ser privado)
- ✅ Conta no Railway (grátis)
- ✅ Dockerfile funcionando (já temos!)

## 🛤️ Passo 1: Preparar o Projeto

O projeto já está preparado com:
- ✅ `Dockerfile` otimizado para Railway
- ✅ `railway.json` com configurações
- ✅ `entrypoint.sh` com suporte a `DATABASE_URL`
- ✅ Migrações automáticas

## 🌐 Passo 2: Criar Conta e Projeto no Railway

### 1. Acesse https://railway.app
### 2. Faça login com GitHub
### 3. Clique em "New Project"
### 4. Selecione "Deploy from GitHub repo"
### 5. Escolha seu repositório (clinica-360-backend)

## 🐘 Passo 3: Adicionar PostgreSQL

### 1. No dashboard do projeto, clique em "+"
### 2. Selecione "Database" → "Add PostgreSQL"
### 3. Railway criará automaticamente:
   - Base de dados PostgreSQL
   - Variável `DATABASE_URL` 
   - Conexão automática entre API e banco

## ⚙️ Passo 4: Configurar Variáveis de Ambiente

No Railway dashboard → sua API service → Variables:

```env
# Automáticas (Railway fornece):
DATABASE_URL=postgresql://...  # ✅ Auto-generated

# Adicionar manualmente:
SECRET_KEY=your-super-secret-key-for-production-change-this
ENVIRONMENT=production
DEBUG=false
BACKEND_CORS_ORIGINS=https://your-frontend-url.com,https://clinica360.vercel.app
```

## 🚀 Passo 5: Deploy

### Automático:
- Railway detecta `Dockerfile`
- Build automático
- Deploy em ~3-5 minutos

### Manual (se necessário):
```bash
# Instalar Railway CLI
npm install -g @railway/cli

# Login
railway login

# Deploy
railway up
```

## 🔗 Passo 6: Obter URLs

Após deploy:
- **API**: `https://clinica-360-backend-production.up.railway.app`
- **Swagger**: `https://your-url.railway.app/docs`
- **Health**: `https://your-url.railway.app/health`

## ✅ Passo 7: Verificar Deploy

```bash
# Testar API
curl https://your-url.railway.app/health

# Verificar Swagger
# Abrir: https://your-url.railway.app/docs
```

## 🔄 Passo 8: Configurar Deploy Automático

No GitHub → Settings → Webhooks:
- Railway configura automaticamente
- Push para `main` = deploy automático
- PR merge = deploy automático

## 📊 Monitoramento

Railway Dashboard mostra:
- 📈 CPU/Memory usage
- 📋 Logs em tempo real
- 🔄 Deploy history
- 💾 Database metrics

## 🚨 Troubleshooting

### Deploy falhou?
```bash
# Ver logs no Railway dashboard
# Ou via CLI:
railway logs
```

### Banco não conecta?
- Verifique se `DATABASE_URL` está setada
- Logs devem mostrar "✅ PostgreSQL is ready!"

### Migrações não rodaram?
- Verifique logs do entrypoint.sh
- Railway roda automaticamente: `alembic upgrade head`

## 💰 Custos

**Plano Hobby (Gratuito):**
- $5 crédito/mês
- ~500h runtime/mês
- Suficiente para desenvolvimento/teste

**Se precisar mais:**
- Plano Pro: $20/mês
- Railway é bem econômico comparado a outros

## 🔐 Segurança

Para produção, altere:
```env
SECRET_KEY=generate-a-strong-secret-key-here
DEBUG=false
BACKEND_CORS_ORIGINS=https://your-actual-frontend-domain.com
```

## 📱 Conectar Frontend

No seu frontend React (clinica-360):
```typescript
// src/config/api.ts
const API_BASE_URL = process.env.NODE_ENV === 'production' 
  ? 'https://your-railway-url.railway.app'
  : 'http://localhost:8000';
```

## 🎉 Pronto!

Seu backend está no ar! 🚀

Links úteis:
- Railway Dashboard: https://railway.app/dashboard
- Documentação: https://docs.railway.app
- Status: https://status.railway.app 
