def codifica(mensagem: str, senha: str) -> str: return "".join([chr(((ord(mensagem[i]) + ord(senha[i])) % 26) + ord('A')) for i in range(len(mensagem))])
def descodifica(mensagem: str, senha: str) -> str: return "".join([chr(((ord(mensagem[i]) - ord(senha[i]) + 26) % 26) + ord('A')) for i in range(len(mensagem))])

resultado = codifica("TESTE", "CHAVE")
print(f"Codificado {resultado}")
print(descodifica(resultado, "CHAVE"))