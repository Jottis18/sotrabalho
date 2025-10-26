#!/bin/bash

# Script de setup para o projeto SchedulerAI PRO
# Este script configura o ambiente de desenvolvimento local

echo "🚀 Configurando SchedulerAI PRO..."

# Verifica se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado. Por favor, instale Python 3.8+ primeiro."
    exit 1
fi

# Verifica se Node.js está instalado
if ! command -v node &> /dev/null; then
    echo "❌ Node.js não encontrado. Por favor, instale Node.js 16+ primeiro."
    exit 1
fi

echo "✅ Python e Node.js encontrados"

# Setup do Backend
echo "📦 Configurando backend..."
cd backend

# Cria ambiente virtual se não existir
if [ ! -d "venv" ]; then
    echo "Criando ambiente virtual Python..."
    python3 -m venv venv
fi

# Ativa ambiente virtual
echo "Ativando ambiente virtual..."
source venv/bin/activate

# Instala dependências
echo "Instalando dependências Python..."
pip install -r requirements.txt

echo "✅ Backend configurado!"

# Setup do Frontend
echo "📦 Configurando frontend..."
cd ../frontend

# Instala dependências
echo "Instalando dependências Node.js..."
npm install

echo "✅ Frontend configurado!"

# Volta para o diretório raiz
cd ..

echo ""
echo "🎉 Setup concluído!"
echo ""
echo "Para executar o projeto:"
echo ""
echo "1. Backend (em um terminal):"
echo "   cd backend"
echo "   source venv/bin/activate"
echo "   python api_server.py"
echo ""
echo "2. Frontend (em outro terminal):"
echo "   cd frontend"
echo "   npm start"
echo ""
echo "3. Acesse http://localhost:3000 no navegador"
echo ""
echo "Para deploy:"
echo "- Backend: Railway (pasta backend/)"
echo "- Frontend: Vercel (pasta frontend/)"
echo ""
