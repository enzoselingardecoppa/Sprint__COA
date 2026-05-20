# processamento.py - Simulação de processamento de dados de sensores
import time

def processar_dados():
    soma = 0
    # Simula a leitura e processamento de 1000 registros de um eletroposto
    for i in range(1, 1001):
        soma += i
    return soma

inicio = time.time()
resultado = processar_dados()
fim = time.time()

print(f"Resultado: {resultado}")
print(f"O Python executou milhares de ciclos de CPU devido ao interpretador.")