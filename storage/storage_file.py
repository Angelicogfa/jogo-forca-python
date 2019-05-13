import random

class storage_file:

   def __init__ (self):
       with open('C:\\Users\\guilherme.angelico\\Documents\\Estudos\\python\\jogo_forca\\storage\\palavras.txt', 'r') as file:
           self.__palavras__ = file.readlines()
           file.close()

   def get_palavra(self):
        posicao = random.randrange(0, len(self.__palavras__))
        palavra = self.__palavras__[posicao]
        print('Palavra storage: {}'.format(palavra))
        return palavra.split(';')
