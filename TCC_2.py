import numpy as np
import matplotlib.pyplot as plt
# Carregar o arquivo .mat
data = scipy.io.loadmat('/Users/alanasarahfreitasdarocha/Documents/UFPR 8 periodo/Atividade 2 - TCC/IN_OUT_PA.mat')

# Exibir os cabeçalhos
print(data.keys())
u = data['in'].flatten()  # Entrada, flatten é usado para transformar em uma unica dimensão 
y = data['out'].flatten()  # Saída

print(u[:5]) # printando 5 primeiros valores
print(y[:5])
# Definir a ordem do polinômio (P) e o número de atrasos (M)
P = 2  # Ordem do polinômio
M = 2  # Memória 

# Número de dados
N = len(u) #99
print(N)
# Inicializar a matriz de regressão XX
XX = []

# Construir a matriz de regressão XX utilizando loop
for n in range(M, N):  # Evitar os primeiros M valores, pois nao teremos memoria    
    linha = []
    for m in range(M):  # Para memória
        for p in range(1, P + 1):  # Para cada potência
            linha.append(u[n - m] ** p)
    XX.append(linha)

# Converter a lista para um array NumPy
XX = np.array(XX)

# Ajustar o vetor de saída correspondente
y_adjusted = y[M:]

# Ver as primeiras linhas da matriz XX e do vetor Y
print("Primeiras linhas de XX:", XX[:5])
print("Primeiras linhas de Y:", y_adjusted[:5])