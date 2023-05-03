from random import randint
from time import time
from algorithmHandler import getAlgorithm
DATA = [randint(0,30),randint(0,30),randint(0,30),randint(0,30),randint(0,30),randint(0,30)]

algorithmName=input("What is the name of the algorithm that you want to run? ")
algorithm = getAlgorithm(algorithmName)
start_time = time()
end_time = time() - start_time

print(f"The program took {end_time}")