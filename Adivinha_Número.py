import random as rnd
def adivinha(resposta: str) -> str: 
    try: return (v:= rnd.randrange(0, 100), "Certo!!!" if int(resposta) is v else "Errado! A resposta correta é " + str(v))[1] 
    except: return "Tentativa inválida!"
print(adivinha(input("Adivinha entre 0 a 100: ")))