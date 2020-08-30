import pytest
import config as cf
from Sorting import selectionsort as sort
from DataStructures import listiterator as it
from ADT import list as lt
import csv

#list_type = 'ARRAY_LIST'
list_type = 'SINGLE_LINKED'

lst_books = lt.newList(list_type)
booksfile = "Data/SmallMoviesDetailsCleaned.csv"


def setUp():
    print('Cargando Películas')
    loadCSVFile(booksfile, lst_books)
    print(lst_books['size'])


def tearDown():
       pass
def loadCSVFile (file,lst, sep=";"):
    print("Cargando archivo ....")
    dialect = csv.excel()
    dialect.delimiter=sep
    contador=0
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
                contador+=1
                if contador==5:
                    break
    print(lst_books)
    except:
        print("Hubo un error con la carga del archivo")

def printList(lst):
    iterator = it.newIterator(lst)
    while it.hasNext(iterator):
        element = it.next(iterator)
        print(element['\ufeffid'])

def less(element1, element2):
    if int(element1['\ufeffid']) < int(element2['\ufeffid']):
        return True
    return False

def test_sort():
    """
    Lista con elementos en orden aleatorio
    """
    print("sorting ....")
    sort.selectionSort(lst_books, less)

def test_loading_CSV_y_ordenamiento():
    """
    Prueba que se pueda leer el archivo y que despues de relizar el sort, el orden este correcto
    """
    setUp()
    sort.selectionSort(lst_books,less)
    while not (lt.isEmpty(lst_books)):
        x = int(lt.removeLast(lst_books)['\ufeffid'])
        if not (lt.isEmpty(lst_books)):
            y = int(lt.lastElement(lst_books)['id'])
        else:
            break
        assert x > y

