import random
import os

class storage_file:

   def __init__ (self):

       basepath = os.path.abspath(os.path.dirname(__file__))
       path = os.path.join(basepath, './palavras.txt')

       with open(path, 'r') as file:
           self.__palavras__ = file.readlines()
           file.close()

   def get_palavra(self):
        posicao = random.randrange(0, len(self.__palavras__))
        palavra = self.__palavras__[posicao]
        return palavra.split(';')
