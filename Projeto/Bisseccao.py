import math

# Definindo as funções matemáticas
def f1(x):
    return x**2 / 2 - math.tan(x)

def f2(x):
    return x**5 - 9 * x**3 + x + 3

# Implementação do método da bisseção
def bisection_method(func, a, b, tolerance, max_iterations):
    print(f"Avaliando os extremos do intervalo: f({a}) = {func(a):.5f}, f({b}) = {func(b):.5f}")

    # Verifica se o método é aplicável no intervalo dado
    if func(a) * func(b) >= 0:
        print(f"Não é possível aplicar o método no intervalo ({a}, {b}) devido à falta de sinais opostos.")
        return None

    iteration = 0
    while (b - a) / 2 > tolerance and iteration < max_iterations:
        c = (a + b) / 2  # Calcula o ponto médio
        if func(c) == 0:  # Encontrou a raiz exata
            print(f"Raiz exata encontrada em x = {c:.5f}")
            return c, iteration
        elif func(a) * func(c) < 0:  # A raiz está na metade esquerda
            b = c
        else:  # A raiz está na metade direita
            a = c
        iteration += 1

    return c, iteration  # Retorna a raiz aproximada e o número de iterações

# Função para ajustar automaticamente o intervalo, caso inválido
def find_valid_interval(func, a, b, step=0.1, max_steps=50):
    for _ in range(max_steps):
        if func(a) * func(b) < 0:  # Verifica se o intervalo é válido
            return a, b
        a -= step
        b += step
    return None, None  # Retorna None se nenhum intervalo válido for encontrado

# Configurações do problema
tolerance = 10**-5  # Precisão desejada
max_iterations = 100  # Limite máximo de iterações

# Intervalos iniciais para as funções
intervals = [
    (f1, -2.2, 1),
    (f2, -3, 0.7)
]

# Processando cada função
results = []
for i, (func, a, b) in enumerate(intervals):
    print(f"\nAnalisando a função f{i+1} no intervalo inicial ({a}, {b}):")

    # Verifica se o intervalo inicial é válido
    if func(a) * func(b) >= 0:
        print(f"O intervalo fornecido ({a}, {b}) não é válido. Buscando um novo intervalo...")
        a, b = find_valid_interval(func, a, b)
        if a is None or b is None:
            print("Não foi possível encontrar um intervalo válido após múltiplas tentativas.")
            results.append((None, None))
            continue
        print(f"Novo intervalo válido encontrado: ({a}, {b})")

    # Calcula a raiz usando o método da bisseção
    root, iterations = bisection_method(func, a, b, tolerance, max_iterations)
    results.append((root, iterations))

# Apresentando os resultados
print("\nResultados Finais:")
for i, (root, iterations) in enumerate(results):
    print(f"Função f{i+1}:")
    if root is not None:
        print(f"  - Raiz aproximada: x = {root:.5f}")
        print(f"  - Iterações necessárias: {iterations}")
    else:
        print("  - Nenhuma raiz foi encontrada dentro dos limites fornecidos.")
    print("-" * 30)
