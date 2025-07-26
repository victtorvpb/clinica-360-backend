# 💰 Deploy BARATO em VPS ($5/mês)

Deploy em VPS de $5/mês com Docker.

## 🎯 Escolha do Provedor

### 🥇 Vultr - $5/mês (Recomendado)
- **1GB RAM**, 25GB SSD, 1TB transfer
- **São Paulo**: Datacenter no Brasil
- **Ubuntu 22.04 + Docker** preinstalado

### 🥈 DigitalOcean - $6/mês  
- **1GB RAM**, 25GB SSD, 1TB transfer
- **1-Click Docker Droplet**
- **São Francisco**: Mais próximo

### 🥉 Linode - $5/mês
- **1GB RAM**, 25GB SSD, 1TB transfer
- **Performance superior**
- **São Paulo**: Datacenter disponível

## 🚀 Setup no Vultr (Exemplo)

### Passo 1: Criar VPS
```bash
1. Vultr.com → Create Instance
2. Choose Instance: Regular Performance
3. Server Location: São Paulo, Brazil  
4. Server Image: Ubuntu 22.04 LTS
5. Server Size: $5/mo (1GB RAM)
6. Add SSH Key (recomendado)
```

### Passo 2: Conectar ao Servidor
```bash
# Conectar via SSH
ssh root@SEU_IP_VPS

# Atualizar sistema
apt update && apt upgrade -y

# Instalar Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Instalar Docker Compose
apt install docker-compose -y
```

### Passo 3: Configurar Firewall
```bash
# UFW Firewall
ufw allow 22    # SSH
ufw allow 80    # HTTP
ufw allow 443   # HTTPS
ufw allow 8000  # API (temporário)
ufw enable
```

### Passo 4: Deploy da Aplicação
```bash
# Clonar repositório
git clone https://github.com/seu-usuario/clinica-360-backend.git
cd clinica-360-backend

# Configurar .env
cp env.example .env
nano .env
```

```env
# Configurações para VPS
POSTGRES_SERVER=postgres
POSTGRES_USER=clinica_user
POSTGRES_PASSWORD=sua_senha_forte_aqui
POSTGRES_DB=clinica_360
POSTGRES_PORT=5432

SECRET_KEY=sua-chave-secreta-super-forte-para-producao
ENVIRONMENT=production
DEBUG=false
BACKEND_CORS_ORIGINS=https://seu-dominio.com
```

### Passo 5: Subir Aplicação
```bash
# Build e subir containers
docker-compose up -d

# Verificar logs
docker-compose logs -f api

# Testar
curl http://localhost:8000/health
```

## 🌐 Configurar Domínio (Opcional)

### Opção 1: Cloudflare (Gratuito)
```bash
1. Comprar domínio (.com.br ~R$40/ano)
2. Cloudflare DNS (gratuito)
3. Apontar A record para IP do VPS
4. SSL automático via Cloudflare
```

### Opção 2: Nginx + Let's Encrypt
```bash
# Instalar Nginx
apt install nginx -y

# Configurar reverse proxy
nano /etc/nginx/sites-available/clinica360
```

```nginx
server {
    listen 80;
    server_name seu-dominio.com;
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

```bash
# Ativar site
ln -s /etc/nginx/sites-available/clinica360 /etc/nginx/sites-enabled/
nginx -t && systemctl reload nginx

# SSL grátis com Certbot
apt install certbot python3-certbot-nginx -y
certbot --nginx -d seu-dominio.com
```

## 🔄 Automação de Deploy

### Script de Deploy
```bash
# deploy.sh
#!/bin/bash
cd /root/clinica-360-backend
git pull origin main
docker-compose down
docker-compose build api
docker-compose up -d
echo "✅ Deploy concluído!"
```

### GitHub Actions para VPS
```yaml
# .github/workflows/deploy-vps.yml
name: Deploy to VPS
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to server
        uses: appleboy/ssh-action@v0.1.5
        with:
          host: ${{ secrets.VPS_HOST }}
          username: root
          key: ${{ secrets.VPS_SSH_KEY }}
          script: |
            cd clinica-360-backend
            git pull origin main
            docker-compose down
            docker-compose up -d --build
```

## 💾 Backup Automático

### Script de Backup PostgreSQL
```bash
# backup.sh
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
docker exec postgres pg_dump -U clinica_user clinica_360 > backup_$DATE.sql
aws s3 cp backup_$DATE.sql s3://meu-bucket/backups/
rm backup_$DATE.sql

# Adicionar ao crontab
crontab -e
# Backup diário às 3h
0 3 * * * /root/backup.sh
```

## 📊 Monitoramento

### htop + Docker Stats
```bash
# Instalar ferramentas
apt install htop -y

# Monitorar recursos
htop
docker stats

# Logs em tempo real
docker-compose logs -f
```

### Uptime Monitor
```bash
# UptimeRobot.com (gratuito)
1. Add Monitor: http://SEU_IP:8000/health
2. Alert via email se cair
3. Dashboard público opcional
```

## 💡 Otimizações

### Otimizar Docker
```bash
# Cleanup automático
docker system prune -af --volumes

# Limitar logs
nano docker-compose.yml
```

```yaml
services:
  api:
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

### Swap para VPS pequena
```bash
# Adicionar 1GB swap
fallocate -l 1G /swapfile
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile
echo '/swapfile none swap sw 0 0' >> /etc/fstab
```

## 💰 Resumo de Custos

### VPS: ~$5/mês
- **Vultr**: $5/mês
- **Domínio**: R$40/ano (~$8/ano)
- **Total**: ~$60/ano ($5/mês)

### Alternativa ainda mais barata:
- **Oracle Cloud Free Tier**: $0 (para sempre)
- **Domínio**: Apenas se quiser
- **Total**: $0 🎉

## 🎯 Vale a pena?

### ✅ **Prós VPS:**
- **Controle total**
- **Performance previsível**
- **Sem limitações**
- **Aprendizado DevOps**

### ❌ **Contras VPS:**
- **Manutenção manual**
- **Backup responsabilidade sua**
- **Monitoramento manual**
- **SSL/Domain extra**

### 🤔 **Comparação:**
- **Render gratuito**: $0 mas limites
- **Railway**: $5 mas sem trabalho
- **VPS**: $5 mas precisa configurar

**Para aprender**: VPS é ótimo!
**Para produção**: Railway é mais fácil 
