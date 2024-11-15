import numpy as np

def newton_raphson(f, g, x0, E=0.00001, N=100):
    """
    Método de Newton-Raphson para encontrar raízes de funções.

    Parâmetros:
    f  - Função da qual queremos encontrar a raiz.
    g  - Derivada da função f.
    x0 - Estimativa inicial da raiz.
    E  - Tolerância para critério de parada (default: 0.00001).
    N  - Número máximo de iterações (default: 100).

    Retorna:
    Aproximação da raiz da função f ou None se falhar.
    """
    for n in range(1, N + 1):
        try:
            fx = f(x0)
            gx = g(x0)
            if gx == 0:
                print(f"Iteração {n}: Derivada zero. Newton-Raphson falhou.")
                return None

            x_novo = x0 - fx / gx
        except ZeroDivisionError:
            print(f"Iteração {n}: Divisão por zero. Newton-Raphson falhou.")
            return None
        except Exception as e:
            print(f"Erro na iteração {n}: {e}")
            return None

        print(f"Iteração {n}: x = {x_novo:.15f}, f(x) = {fx:.15f}")

        if abs(x_novo - x0) < E:  # Critério de parada
            return x_novo

        x0 = x_novo

    print("Número máximo de iterações atingido.")
    return None

# Função 1: f(x) = (x^2)/2 - tan(x)
def f1(x):
    return (x**2) / 2 - np.tan(x)

# Derivada da função 1: g(x) = x - sec(x)^2
def g1(x):
    return x - (1 / np.cos(x))**2

# Função 2: f(x) = x^5 - 9x^3 + x + 3
def f2(x):
    return x**5 - 9 * x**3 + x + 3

# Derivada da função 2: g(x) = 5x^4 - 27x^2 + 1
def g2(x):
    return 5 * x**4 - 27 * x**2 + 1

# Testando o método de Newton-Raphson com ambas as funções
print("Raiz da função f(x) = (x^2)/2 - tan(x):")
x0_f1 = -2 # Estimativa inicial para f1
raiz1 = newton_raphson(f1, g1, x0_f1)
if raiz1 is not None:
    print(f'Raiz aproximada: x = {raiz1:.15f}\n')

print("Raiz da função f(x) = x^5 - 9x^3 + x + 3:")
x0_f2 = 0.5  # Estimativa inicial para f2
raiz2 = newton_raphson(f2, g2, x0_f2)
if raiz2 is not None:
    print(f'Raiz aproximada: x = {raiz2:.15f}\n')
