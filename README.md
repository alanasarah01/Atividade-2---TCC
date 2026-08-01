# Atividade-2---TCC — Identificação de Amplificador de Potência via Mínimos Quadrados

Exercício de identificação de sistemas não lineares: ajuste de um modelo polinomial com memória (estilo NARX) aos dados reais de entrada/saída de um amplificador de potência (PA).

## Stack utilizada
- Linguagem: Python (numpy, scipy, matplotlib)
- Dados: arquivo .mat (IN_OUT_PA.mat)

## Fonte dos dados
Arquivo IN_OUT_PA.mat com sinais medidos de entrada (in) e saída (out) do amplificador de potência.

## Arquitetura
Carregamento do .mat com scipy.io.loadmat -> extração dos vetores de entrada (u) e saída (y) -> montagem da matriz de regressão XX considerando ordem do polinômio (P) e memória (M) -> resolução por mínimos quadrados -> comparação entre saída medida e saída estimada pelo modelo.

## Principais decisões
Ordem do polinômio (P=2) e memória (M=2) escolhidas para representar a não linearidade e os efeitos de memória do sistema, equilibrando complexidade do modelo e qualidade do ajuste.

## Como rodar o projeto
1. Ajuste o caminho do arquivo IN_OUT_PA.mat em TCC_2.py (ou use o TCC_2.ipynb).
2. Execute o script: python TCC_2.py
3. O relatório com o desenvolvimento completo está em "Atividade Mínimos Quadrados - ATV 2 - Alana Rocha.pdf".

## Resultados
Modelo polinomial com memória ajustado aos dados reais do amplificador, com gráfico comparando a saída medida e a saída estimada.

## Aprendizados
Identificação de sistemas dinâmicos não lineares aplicada a um caso real de engenharia (amplificadores de potência), estendendo o método dos mínimos quadrados trabalhado na Atividade 1 para um problema com múltiplas variáveis de regressão.
