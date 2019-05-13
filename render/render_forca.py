class render_forca:

    def __init__(self):
        self.__erro__ = 0
        self.__status__ = [
             '''
            +-----+
            |     |
                  |
                  |
                  |
                  |
            ============
            ''',
            '''
            +-----+
            |     |
            0     |
                  |
                  |
                  |
            ============
            ''',
            '''
            +-----+
            |     |
            0     |
            |     |
                  |
                  |
            ============
            ''',
            '''
            +-----+
            |     |
            0     |
           /|     |
                  |
                  |
            ============
            ''',
            '''
            +-----+
            |     |
            0     |
           /|\    |
                  |
                  |
            ============
            ''',
            '''
            +-----+
            |     |
            0     |
           /|\    |
           /      |
                  |
            ============
            ''',
            '''
            +-----+
            |     |
            0     |
           /|\    |
           / \    |
                  |
            ============
            '''
        ]

    def novo_erro(self):
      if self.__erro__ + 1 > 7:
            raise Exception('Erro está no máximo para o jogo')

      self.__erro__ += 1
      self.__str__()

    def fim_de_jogo(self):
      return self.__erro__ == 6

    def __str__(self):
      return self.__status__[self.__erro__]