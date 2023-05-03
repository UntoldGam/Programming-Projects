from os import listdir, path
from path import isdir, isfile, join

algorithms={}
DIR = "algorithms/"
def getAlgorithm(name):
  return algorithms[name]


def storeAlgorithms():
  for mainFolder in listdir(dir_path):
    # check if current path is a file
    print(mainFolder)
    if isdir(join(dir_path, mainFolder)):
        for subFolder in listdir(mainFolder):
           print(subFolder)
  return False