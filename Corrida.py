import random
carro1, carro2 = ".-.", ".-."
while True:
    carro1, carro2 = (" " * random.randint(0, 2)) + carro1, (" " * random.randint(0, 2)) + carro2
    print("Carro 1" + carro1 +  "\n" + "Carro 2" + carro2 + "\n" + "-"*45 + "|")
    if len(carro1) >= 40 and len(carro2) >= 40:
        print("Empate!"); break
    if len(carro1) >= 40 or len(carro2) >= 40:
        print("Ganhou carro 1") if len(carro1) >= 40 else print("Ganhou carro 2")
        break