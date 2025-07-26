# 🚀 Deploy no Render (100% Gratuito)

Guia completo para deploy da **Clinica 360 Backend** no Render.

## 📋 Pré-requisitos

- ✅ Conta no GitHub
- ✅ Projeto commitado no GitHub  
- ✅ Conta no Render (gratuita)

## 🎯 Por que Render?

### ✅ **Vantagens:**
- **100% gratuito** para sempre
- **PostgreSQL gratuito** incluído
- **SSL automático** 
- **Deploy automático** via GitHub
- **Zero configuração** de infraestrutura
- **750 horas/mês gratuitas** (suficiente)

### ⚠️ **Limitações Plano Gratuito:**
- **Sleep após 15min** de inatividade
- **512MB RAM** máximo
- **Restart em ~30s** quando acordar
- **Dados persistem** (PostgreSQL mantido)

## 🚀 Passo a Passo

### Passo 1: Preparar Repositório
```bash
# Commit final do projeto
git add .
git commit -m "Configure for Render deployment"
git push origin main

# Verificar se todos os arquivos estão commitados:
# ✅ Dockerfile
# ✅ entrypoint.sh  
# ✅ requirements.txt
# ✅ render.yaml (opcional)
# ✅ alembic/
# ✅ app/
```

### Passo 2: Criar Conta no Render
```bash
1. Ir para render.com
2. "Get Started for Free"
3. Conectar com GitHub
4. Autorizar acesso aos repos
```

### Passo 3: Criar PostgreSQL Database
```bash
1. Dashboard → "New +"
2. Escolher "PostgreSQL"
3. Configurar:
   - Name: clinica-360-postgres
   - Database: clinica_360
   - User: clinica_user
   - Region: Oregon (padrão)
   - Plan: Free ($0/month)
4. "Create Database"
5. ⏳ Aguardar criação (~2-3 min)
```

### Passo 4: Obter Dados do PostgreSQL
```bash
# Após criação, copiar:
📋 Database URL (Internal): postgres://user:pass@host:port/db
📋 Host: dpg-xxxxx-a.oregon-postgres.render.com
📋 Port: 5432
📋 Database: clinica_360
📋 Username: clinica_user  
📋 Password: [gerado automaticamente]
```

### Passo 5: Criar Web Service
```bash
1. Dashboard → "New +"
2. Escolher "Web Service"
3. Conectar repositório:
   - "Connect account" (GitHub)
   - Escolher "clinica-360-backend"
   - "Connect"
4. Configurar Basic Settings:
   - Name: clinica-360-api
   - Region: Oregon
   - Branch: main  
   - Runtime: Docker
   - Build Command: [deixar vazio]
   - Start Command: /entrypoint.sh
```

### Passo 6: Configurar Environment Variables
```bash
# Em "Environment Variables", adicionar:

ENVIRONMENT=production
DEBUG=false
SECRET_KEY=[gerar uma chave forte aleatória]

# Database - usar dados do Passo 4:
POSTGRES_SERVER=dpg-xxxxx-a.oregon-postgres.render.com  
POSTGRES_PORT=5432
POSTGRES_USER=clinica_user
POSTGRES_PASSWORD=[password do passo 4]
POSTGRES_DB=clinica_360

# OU usar DATABASE_URL diretamente:
DATABASE_URL=[Internal Database URL do passo 4]

# CORS para produção:
BACKEND_CORS_ORIGINS=https://sua-app.vercel.app,https://clinica360.com
```

### Passo 7: Deploy
```bash
1. "Create Web Service"
2. ⏳ Aguardar build (~5-10 min)
3. Acompanhar logs em tempo real
4. ✅ Deploy concluído!
```

### Passo 8: Verificar URLs
```bash
# Após deploy:
🌐 API URL: https://clinica-360-api.onrender.com
📚 Swagger: https://clinica-360-api.onrender.com/docs
🔍 ReDoc: https://clinica-360-api.onrender.com/redoc
❤️ Health: https://clinica-360-api.onrender.com/health

# PostgreSQL (apenas interno):
🗄️ postgres://clinica_user:password@dpg-xxxxx:5432/clinica_360
```

## 🔍 Verificação do Deploy

### Testar API
```bash
# Health check
curl https://clinica-360-api.onrender.com/health

# Swagger UI
open https://clinica-360-api.onrender.com/docs

# Listar endpoints
curl https://clinica-360-api.onrender.com/api/v1/
```

### Verificar Logs
```bash
1. Render Dashboard
2. clinica-360-api service  
3. "Logs" tab
4. Verificar:
   ✅ PostgreSQL connection successful
   ✅ Alembic migrations completed
   ✅ FastAPI started on port 10000
```

## 🔄 Deploy Automático

### GitHub Actions (Opcional)
```yaml
# .github/workflows/deploy.yml
name: Deploy to Render
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy Hook
        run: |
          curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

```bash
# Configurar Deploy Hook:
1. Render Dashboard → Service Settings
2. "Build & Deploy" → "Deploy Hook"  
3. Copiar URL
4. GitHub → Settings → Secrets → Add RENDER_DEPLOY_HOOK
```

## 😴 Problema do Sleep

### Como Funciona:
- **15 min inativo** → API hiberna
- **Primeira request** → ~30s para acordar
- **Requests seguintes** → Normal

### Soluções:

#### 1. UptimeRobot (Recomendado)
```bash
1. uptimerobot.com → Free Account
2. Add Monitor:
   - Type: HTTP(s)
   - URL: https://clinica-360-api.onrender.com/health
   - Interval: 5 minutes
3. ✅ API acordada 24/7
```

#### 2. GitHub Actions Ping
```yaml
# .github/workflows/keepalive.yml
name: Keep API Alive
on:
  schedule:
    - cron: '*/10 * * * *'  # Every 10 minutes

jobs:
  ping:
    runs-on: ubuntu-latest
    steps:
      - name: Ping API
        run: curl https://clinica-360-api.onrender.com/health
```

#### 3. Frontend Ping
```javascript
// No frontend, ping a cada 10 min
setInterval(() => {
  fetch('https://clinica-360-api.onrender.com/health')
}, 10 * 60 * 1000);
```

## 💾 Backup do PostgreSQL

### Export Manual
```bash
# Render Dashboard → PostgreSQL → Connect
# Usar External Connection ou usar pg_dump via script
```

### Script de Backup
```bash
# backup.sh
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
EXTERNAL_URL="postgres://user:pass@external-host:5432/db"

pg_dump $EXTERNAL_URL > backup_$DATE.sql
echo "Backup criado: backup_$DATE.sql"
```

## 🔧 Troubleshooting

### Build Errors
```bash
# Erro comum: Dockerfile não encontrado
✅ Verificar se Dockerfile está na raiz do repo
✅ Runtime deve ser "Docker" no Render

# Erro: Requirements não satisfeitos  
✅ Verificar requirements.txt
✅ Verificar Python version no Dockerfile
```

### Runtime Errors
```bash
# Database connection failed
✅ Verificar DATABASE_URL
✅ Verificar se PostgreSQL foi criado
✅ Verificar environment variables

# Port binding error
✅ Usar PORT=${PORT:-10000} no entrypoint.sh
✅ Render usa porta dinâmica via $PORT
```

### Performance Issues
```bash
# API lenta (plano gratuito)
✅ Otimizar queries SQL
✅ Implementar cache Redis (Redis Cloud free)
✅ Considerar upgrade para $7/mês se necessário
```

## 💰 Custos

### Free Tier:
- **Web Service**: $0 (750h/mês)
- **PostgreSQL**: $0 (90 dias, depois $7/mês)
- **Total primeiros 90 dias**: $0 🎉
- **Após 90 dias**: $7/mês apenas PostgreSQL

### Alternativas Banco Gratuito:
```bash
# Se PostgreSQL do Render expirar:
1. Supabase PostgreSQL (2 projetos grátis)
2. ElephantSQL (20MB grátis)  
3. Railway PostgreSQL ($5 crédito/mês)
4. Aiven (30 dias grátis)
```

## 🔗 Conectar Frontend

### URLs para usar no Frontend:
```javascript
// Em produção (Vercel/Netlify)
const API_URL = 'https://clinica-360-api.onrender.com/api/v1'

// Em desenvolvimento  
const API_URL = 'http://localhost:8000/api/v1'

// Configurar CORS no backend
BACKEND_CORS_ORIGINS=https://clinica-360.vercel.app,https://localhost:3000
```

## ✅ Checklist Final

### Deploy Concluído:
- [ ] PostgreSQL criado
- [ ] Web Service configurado  
- [ ] Environment variables setadas
- [ ] Deploy realizado com sucesso
- [ ] API funcionando (/health retorna 200)
- [ ] Swagger acessível (/docs)
- [ ] UptimeRobot configurado
- [ ] Frontend conectado

### Next Steps:
- [ ] Configurar domínio custom (se houver)
- [ ] Implementar monitoramento
- [ ] Configurar backups  
- [ ] Planejar upgrade se necessário

## 🎉 Parabéns!

Sua **Clinica 360 API** está rodando **100% gratuito** no Render! 🚀

**URLs importantes:**
- 📱 **API**: https://clinica-360-api.onrender.com  
- 📚 **Docs**: https://clinica-360-api.onrender.com/docs 
