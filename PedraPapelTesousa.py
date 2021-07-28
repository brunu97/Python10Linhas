import random
tabela = {1: "Pedra", 2: "Papel", 3: "Tesoura"}
def Resultado(jogador: int) -> list[int, str]: 
    n = random.randint(1, 3); return [n, ["Empate", "Humano Ganhou", "PC Ganhou"][(jogador - n) % 3]]
while True:
    print("\n1 - Pedra, 2 - Papel, 3 - Tesoura")
    n = Resultado(int(input(">")))
    print("Resultado: " + str(n[1]) + " - PC Jogou " + str(tabela[n[0]]))