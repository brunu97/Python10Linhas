import random
def obtemPi(pontos: int) -> float:
    pontos_dentro = 0
    for _ in range(pontos): 
        x, y = random.uniform(0, 1), random.uniform(0, 1)
        if ((x*x + y*y) <= 1.0): pontos_dentro += 1
    return (pontos_dentro/pontos) * 4.0
print(obtemPi(2000000))