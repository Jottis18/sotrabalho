# Simulador de Escalonamento de Processos

Um simulador interativo de algoritmos de escalonamento de processos com interface web moderna, desenvolvido para a disciplina de Sistemas Operacionais.

## 🚀 Funcionalidades

- **7 Algoritmos de Escalonamento**:
  - FCFS (First-Come First-Served)
  - SJF (Shortest Job First)
  - SRTF (Shortest Remaining Time First)
  - Priority (Non-Preemptive)
  - Priority (Preemptive)
  - Round Robin
  - Round Robin com Prioridade e Envelhecimento

- **Interface Web Moderna**:
  - Visualização de diagramas de tempo
  - Estatísticas detalhadas (tempo médio de turnaround, tempo de espera, trocas de contexto)
  - Configuração de parâmetros (quantum, aging)
  - Interface responsiva e intuitiva

## 🏗️ Arquitetura

```
projetoSO/
├── backend/           # API Flask + Lógica de Escalonamento
│   ├── api_server.py  # Servidor Flask
│   ├── SchedulerNoGUI.py # Algoritmos de escalonamento
│   ├── config.txt     # Configurações padrão
│   ├── requirements.txt
│   ├── Procfile
│   └── railway.toml
├── frontend/          # React App
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vercel.json
└── README.md
```

## 🛠️ Tecnologias

### Backend
- **Python 3.8+**
- **Flask** - Framework web
- **Flask-CORS** - Cross-origin resource sharing
- **Gunicorn** - Servidor WSGI para produção

### Frontend
- **React 19** - Biblioteca de interface
- **Axios** - Cliente HTTP
- **Recharts** - Gráficos e visualizações
- **Lucide React** - Ícones

## 📦 Instalação e Execução Local

### Pré-requisitos
- Python 3.8+
- Node.js 16+
- npm ou yarn

### Backend

1. Navegue para a pasta backend:
```bash
cd backend
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute o servidor:
```bash
python api_server.py
```

O backend estará disponível em `http://localhost:5000`

### Frontend

1. Navegue para a pasta frontend:
```bash
cd frontend
```

2. Instale as dependências:
```bash
npm install
```

3. Execute o servidor de desenvolvimento:
```bash
npm start
```

O frontend estará disponível em `http://localhost:3000`

## 🌐 Deploy

### Backend - Railway

1. Acesse [Railway](https://railway.app)
2. Conecte sua conta GitHub
3. Crie um novo projeto
4. Selecione o repositório
5. Configure a pasta raiz como `backend`
6. Railway detectará automaticamente o `requirements.txt` e `Procfile`
7. O deploy será feito automaticamente

**Variáveis de ambiente** (opcional):
- `PORT`: Porta do servidor (Railway define automaticamente)

### Frontend - Vercel

1. Acesse [Vercel](https://vercel.com)
2. Conecte sua conta GitHub
3. Importe o repositório
4. Configure:
   - **Framework Preset**: Create React App
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `build`
5. Adicione variável de ambiente:
   - `REACT_APP_API_URL`: URL do seu backend no Railway
6. Faça o deploy

## 🔧 Configuração

### Parâmetros do Sistema

Edite o arquivo `backend/config.txt`:

```
quantum: 2    # Tamanho do quantum para Round Robin
aging: 1      # Taxa de envelhecimento para Round Robin com Aging
```

### Algoritmos Disponíveis

| Algoritmo | ID | Preemptivo | Parâmetros Especiais |
|-----------|----|-----------|-------------------|
| First-Come First-Served | `FCFS` | ❌ | - |
| Shortest Job First | `SJF` | ❌ | - |
| Shortest Remaining Time First | `SRTF` | ✅ | - |
| Priority (Non-Preemptive) | `PriorityNP` | ❌ | - |
| Priority (Preemptive) | `PriorityP` | ✅ | - |
| Round Robin | `RoundRobin` | ✅ | Quantum |
| Round Robin + Priority + Aging | `RoundRobinPriorityAging` | ✅ | Quantum, Aging |

## 📊 API Endpoints

### `POST /api/simulate`
Simula o escalonamento de processos.

**Request Body:**
```json
{
  "processes": [
    {
      "creationTime": 0,
      "duration": 5,
      "priority": 1
    }
  ],
  "algorithm": "FCFS",
  "config": {
    "quantum": 2,
    "aging": 1
  }
}
```

**Response:**
```json
{
  "success": true,
  "algorithm": "FCFS",
  "avgTurnaroundTime": 8.5,
  "avgWaitingTime": 3.5,
  "contextSwitches": 4,
  "diagramData": {
    "processes": [...],
    "maxTime": 10
  }
}
```

### `GET /api/algorithms`
Retorna lista de algoritmos disponíveis.

### `GET /api/health`
Health check da API.

## 🎯 Como Usar

1. **Acesse a aplicação** no navegador
2. **Adicione processos** com:
   - Tempo de criação
   - Duração
   - Prioridade
3. **Selecione o algoritmo** de escalonamento
4. **Configure parâmetros** (se necessário)
5. **Execute a simulação**
6. **Visualize os resultados**:
   - Diagrama de tempo
   - Estatísticas de performance
   - Comparação entre algoritmos

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto é desenvolvido para fins acadêmicos na disciplina de Sistemas Operacionais.

## 👥 Autores

- **Silvana Almeida Silva** - Desenvolvimento completo

## 📚 Referências

- Tanenbaum, A. S. - Sistemas Operacionais Modernos
- Silberschatz, A. - Operating System Concepts
- Documentação Flask: https://flask.palletsprojects.com/
- Documentação React: https://reactjs.org/