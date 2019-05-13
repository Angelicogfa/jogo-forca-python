from render.render_forca import render_forca
import os

class game:
    def __init__(self, palavra: str, dica: str = None):
        self.__palavra__ = palavra.lower()
        self.__dica__ = dica.lower()
        self.__letras__ = []
        self.__erros__ = []
        self.__acertos__ = []
        self.__render__ = render_forca()

    def jogar_letra(self, letra: str) -> (bool, str):
        if letra in self.__letras__:
            return (False, 'Letra já informada. Informe outra')
        elif letra in self.__palavra__:
            self.__letras__.append(letra)
            self.__acertos__.append(letra)
            return (True, 'Informe uma nova letra')
        else:
            try:
                self.__letras__.append(letra)
                self.__erros__.append(letra)
                self.__render__.novo_erro()
                return (False, 'Não foi dessa vez. Informe uma nova letra')
            except:
                return (False, "Fim de jogo. Tente novamente :(")

    def existe_jogadas_disponiveis(self):
        return not (self.__render__.fim_de_jogo() or len(self.__palavra__) == len(self.__acertos__))

    def __formatar_campo__(self) -> []:
        caracteres = []

        for caracter in self.__palavra__:
            if caracter in self.__acertos__:
                caracteres.append(' {} '.format(caracter))
            else:
                caracteres.append(' __ ')
        
        return caracteres
    
    def ganhou_jogo(self) -> bool:
        ganhou = True
        
        for letra in self.__palavra__:
            if letra not in self.__acertos__:
                ganhou = False
                break
        
        return ganhou

    def __str__(self):
        os.system('cls')       
        texto = '''
        ========== Jogo da Forca ==========

        {forca}

        Palavra: {palavra_sorteada}
        Dica: {dica_palavra}

        *** Letras Acertadas ***  
        Acertos: {letras_acertadas}

        *** Letras erradas ***
        Erros: {letras_erradas}      
        '''.format(forca=self.__render__,
                   palavra_sorteada=self.__formatar_campo__(),
                   dica_palavra=self.__dica__,
                   letras_acertadas=self.__acertos__,
                   letras_erradas=self.__erros__)
        
        return texto