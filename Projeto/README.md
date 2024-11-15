# Trabalho de Modelagem Computacional

## Newton Raphson 

O código em Python implementa o método de Newton-Raphson, permitindo encontrar raízes de funções matemáticas. Ele recebe como parâmetros a função, sua derivada e um valor inicial `x0`, retornando a raiz aproximada com erro máximo de `0,00001` e limite de 100 iterações. O cálculo itera até atingir a precisão desejada ou o limite de iterações, garantindo flexibilidade e eficiência no processo.

### Obtenção dos Pontos

Para determinar os valores iniciais `x0`, utilizamos o software GeoGebra, analisando os gráficos das funções e identificando pontos próximos às raízes.

#### Gráfico de f(x) = (x²)/2 - tan(x)
Escolhemos o valor de `x0 = −2`, pois está próximo de uma raiz visível no gráfico e dentro do intervalo onde a função é contínua, evitando as descontinuidades de `tan(x)`.

#### Gráfico de f(x) = x⁵ - 9x³ + x + 3
Escolhemos o valor de `x0 = 0.7`, pois é onde o ponto está próximo de uma raiz real, como observada acima no comportamento da função.

### Resultados

Os valores iniciais escolhidos, combinados com o método de Newton-Raphson, permitem aproximar as raízes das funções, com as justificativas baseadas na análise gráfica.

---

## Bissecção 

O código em Python implementa o Método da Bissecção, uma técnica numérica para encontrar raízes de funções contínuas em um intervalo `[a, b]`. O método divide o intervalo ao meio iterativamente, selecionando a sub-região onde ocorre uma mudança de sinal da função, até atingir a precisão desejada ou o número máximo de 100 iterações. Ele garante a convergência para uma raiz se o intervalo inicial contiver uma mudança de sinal.

### Obtenção dos Intervalos

Para aplicar o Método da Bissecção, utilizamos o software GeoGebra para analisar os gráficos das funções e identificar intervalos `[a, b]` em que ocorre uma mudança de sinal, garantindo que `f(a) . f(b) < 0`.

#### Gráfico de f(x) = (x²)/2 - tan(x)
Selecionamos o intervalo `[−2.2, 1]`, pois os valores da função nesse intervalo apresentam uma mudança de sinal, indicando a presença de uma raiz. Este intervalo foi escolhido com base na análise gráfica e no comportamento contínuo da função longe das descontinuidades de `tan(x)`.

#### Gráfico de f(x) = x⁵ - 9x³ + x + 3
Escolhemos o intervalo `[−3, 0.7]`, onde o gráfico da função mostra uma mudança de sinal clara, confirmando que há pelo menos uma raiz neste intervalo. A escolha também foi feita com base no comportamento observado no gráfico.

### Resultados

Os intervalos escolhidos são suportados por imagens dos gráficos que evidenciam as mudanças de sinal, assegurando a aplicabilidade do Método da Bissecção.
