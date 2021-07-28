tabela_morse = { 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.', ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-', '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.', " ": "/" }
def morse_codifica(mensagem: str) -> str: return " ".join([tabela_morse[i] for i in mensagem.upper() if i in tabela_morse])
def morse_descodifica(mensagem: str) -> str:
    tabela_traduzida = {v: k for k, v in tabela_morse.items()}
    return "".join([tabela_traduzida[i] for i in mensagem.split(" ") if i in tabela_traduzida]) 

print(morse_codifica("Uma frase fixe"))
print(morse_descodifica(".. ... - --- / . / ..- -- .- / ..-. .-. .- ... . / .-.. --- -. --. .- / -- ..- .. - --- / .-.. --- -. --. .- / .--. .- .-. .- / - . ... - .- .-. / --- / --.- ..- . / .- -.-. --- -. - . -. -.-. ."))
print(morse_descodifica(morse_codifica("mensagem curta de teste")))