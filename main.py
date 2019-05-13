from render import game
from storage import storage_file as s

def main():
    file = s()
    registro = file.get_palavra()
    jogo = game(registro[1].lower(), registro[2].lower())
    
    print(jogo)

    while (jogo.existe_jogadas_disponiveis()):

        jogada_ok: bool = False
        while (not jogada_ok and jogo.existe_jogadas_disponiveis()):
            letra = input('Vamos jogar. Informe uma letra:\n')
            result  = jogo.jogar_letra(letra)
            jogada_ok = result[0]
            print(result[1])
            print(jogo)
    
    print('Fim de jogo')


if __name__ == "__main__":
    main()