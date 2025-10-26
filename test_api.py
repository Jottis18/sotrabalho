#!/usr/bin/env python3
"""
Script de teste para verificar se a API está funcionando corretamente
"""

import requests
import json

# URL do backend no Railway
API_URL = "https://sotrabalho-production.up.railway.app"

def test_health():
    """Testa o endpoint de health check"""
    try:
        response = requests.get(f"{API_URL}/api/health")
        if response.status_code == 200:
            data = response.json()
            print("✅ Health Check:", data)
            return True
        else:
            print("❌ Health Check falhou:", response.status_code)
            return False
    except Exception as e:
        print("❌ Erro no Health Check:", e)
        return False

def test_algorithms():
    """Testa o endpoint de algoritmos"""
    try:
        response = requests.get(f"{API_URL}/api/algorithms")
        if response.status_code == 200:
            data = response.json()
            print("✅ Algoritmos disponíveis:")
            for alg in data['algorithms']:
                print(f"  - {alg['name']} ({alg['id']})")
            return True
        else:
            print("❌ Algoritmos falharam:", response.status_code)
            return False
    except Exception as e:
        print("❌ Erro nos Algoritmos:", e)
        return False

def test_simulation():
    """Testa uma simulação simples"""
    try:
        test_data = {
            "processes": [
                {"creationTime": 0, "duration": 3, "priority": 1},
                {"creationTime": 1, "duration": 2, "priority": 2}
            ],
            "algorithm": "FCFS",
            "config": {"quantum": 2, "aging": 1}
        }
        
        response = requests.post(
            f"{API_URL}/api/simulate",
            headers={"Content-Type": "application/json"},
            json=test_data
        )
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print("✅ Simulação funcionando:")
                print(f"  - Algoritmo: {data['algorithm']}")
                print(f"  - Tempo médio de turnaround: {data['avgTurnaroundTime']:.2f}")
                print(f"  - Tempo médio de espera: {data['avgWaitingTime']:.2f}")
                print(f"  - Trocas de contexto: {data['contextSwitches']}")
                return True
            else:
                print("❌ Simulação falhou:", data.get('error'))
                return False
        else:
            print("❌ Simulação falhou:", response.status_code)
            return False
    except Exception as e:
        print("❌ Erro na Simulação:", e)
        return False

if __name__ == "__main__":
    print("🧪 Testando API do SchedulerAI PRO...")
    print("=" * 50)
    
    health_ok = test_health()
    print()
    
    algorithms_ok = test_algorithms()
    print()
    
    simulation_ok = test_simulation()
    print()
    
    print("=" * 50)
    if health_ok and algorithms_ok and simulation_ok:
        print("🎉 TODOS OS TESTES PASSARAM!")
        print("✅ Backend está funcionando perfeitamente")
        print("✅ Pronto para conectar com o frontend")
    else:
        print("❌ Alguns testes falharam")
        print("Verifique os logs do Railway")
