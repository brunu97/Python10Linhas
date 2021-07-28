campo, jogador = [["1","2","3"], ["4", "5", "6"], ["7", "8", "9"]], "X"
while True: 
    print("\n" + '\n'.join(map('|'.join, campo)))
    if len([s for s in sum(campo, []) if s.isdigit()]) == 0: print("Emapte"); break # Verifica se não há mais jogadas possives, marca como empate
    if any([True if i == [j, j, j] else False  for i in campo for j in ["X", "O"]]): print("Ganhou " + "X" if jogador == "O" else "O"); break # Horizontal 
    if any(True if [campo[i][i] for i in range(len(campo))] == [j, j, j] else False for j in ["X", "O"]) or any(True if [n[-i-1] for i, n in enumerate(campo)] == [j, j, j] else False for j in ["X", "O"]): print("Ganhou " + "X" if jogador == "O" else "O"); break # Diagonal 
    if any(True if [x, y, z] == [j, j, j] else False for x, y, z in zip(*campo) for j in ["X", "O"]): print("Ganhou " + "X" if jogador == "O" else "O"); break # Vertical
    l = sum(campo, []); V = int(input(jogador + " >")) - 1 
    if l[V] in ["X", "O"]: continue; 
    l[V] = jogador; jogador = "X" if jogador == "O" else "O"; campo = [l[i:i+3] for i in range(0, len(l), 3)] 