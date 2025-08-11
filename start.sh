#!/bin/bash

# Script de startup para Render
# Executa migrations e inicia a aplicação

echo "🚀 Iniciando Clinica 360 API..."

# Aguarda o banco estar disponível
echo "⏳ Aguardando banco de dados..."
sleep 5

# Executa migrations
echo "📦 Executando migrations..."
alembic upgrade head

# Verifica se as migrations foram executadas com sucesso
if [ $? -eq 0 ]; then
    echo "✅ Migrations executadas com sucesso!"
else
    echo "❌ Erro ao executar migrations"
    exit 1
fi

# Inicia a aplicação
echo "🌐 Iniciando servidor..."
uvicorn app.main:app --host 0.0.0.0 --port $PORT
