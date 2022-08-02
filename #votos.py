#votos
votos_canditato_X=0
votos_canditato_Y=0
votos_canditato_Z=0
votos_branco=0
nulos=0
final = 'fim'

while(final=='fim'):
    try:
        candidato = int(input("""Escolha seu candidato digitando o número correspondente:
                - candidato_X => 889
                - candidato_Y => 847
                - candidato_Z => 515
                - branco => 0  \n"""))
    except:
        print("Seu voto foi nulo")
        candidato = 123

    if (candidato == 889):
        votos_canditato_X = votos_canditato_X + 1
        print('Você votou no candidato X')
    elif (candidato == 847):
        votos_canditato_Y = votos_canditato_Y + 1
        print('Você votou no candidato Y')
    elif (candidato == 515):
        votos_canditato_Z = votos_canditato_Z + 1
        print('Você votou no candidato Z')
    elif (candidato == 0):
        votos_branco = votos_branco + 1
        print('Você votou em branco')
    else:
        nulos = nulos + 1

    final = input("""Fim da votação.
         Digite: 
         1 - Novo Voto
         2 - Resultados \n""")

    if (final == "2"):
        if votos_canditato_X > votos_canditato_Y and votos_canditato_X > votos_canditato_Z:
            print(f"Vencedor: Candidato X com {votos_canditato_X} votos\n"
                  f"Candidato Y: {votos_canditato_Y} votos\n"
                  f"Candidato Z: {votos_canditato_Z} votos\n")
        elif votos_canditato_Y > votos_canditato_X and votos_canditato_Y > votos_canditato_Z:
            print(f"Vencedor: Candidato Y com {votos_canditato_Y} votos\n"
                  f"Candidato X: {votos_canditato_X} votos\n"
                  f"Candidato Z: {votos_canditato_Z} votos\n")
        elif votos_canditato_Z > votos_canditato_X and votos_canditato_Z > votos_canditato_Y:
            print(f"Vencedor: Candidato Z com {votos_canditato_Z} votos\n"
                  f"Candidato X: {votos_canditato_X} votos\n"
                  f"Candidato Y: {votos_canditato_Y} votos\n")
        else:
         print(f"Total de votos nulos: {nulos} \n Total de votos em branco: {votos_branco}")
