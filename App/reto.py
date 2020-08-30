"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from Sorting import mergesort as sort
from time import process_time 



def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Ranking de peliculas")
    print("3- Conocer un director")
    print("4- Conocer un actor")
    print("5- Entender un genero")
    print("0- Salir")




def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1


def loadCSVFile (lst,file, sep=";"):
    dialect = csv.excel()
    dialect.delimiter=sep
    try: 
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")

def get_two_csv(file1,file2,list_type):
    list1=   lt.newList(list_type)
    list2=  lt.newList(list_type)
    lst_movies = lt.newList(list_type)
    loadCSVFile(list1,file1)
    loadCSVFile(list2,file2)
    for i in range(0,lt.size(list1)):
        tuples= (lt.getElement(list1,i),lt.getElement(list2,i))
        lt.addLast(lst_movies,tuples)


    return lst_movies

#ESTA ES LA FUNCIÓN PARA LA BÚSQUEDAD DEL DIRECTOR Y DE SUS PELÍCULAS BUENAS
#REQUERIMIENTO 1

def good_movies(lista,busqueda):
#La x mas votadas
    count=0
    sum=0
    recorrido=0
    di=0
    vot=1
    try:
        while recorrido <= lt.size(lista) :
            if lt.getElement(lista,recorrido)[di]["director_name"] == busqueda:
                vote= float(lt.getElement(lista,recorrido)[vot]['vote_average'])
                if vote >= 6:
                    count+=1
                    sum+= vote
            recorrido+=1
        return((count,sum/count))
    except:
        print("El director no fue encontrado")
    

#REQUERIMIENTO 3
def peliculas_de_un_director(list,director_name):
    size= lt.size(list)
    dirigidas= []
    numero= 0
    calificacion= 0
    for i in range(0,size):
        elem= lt.getElement(list,i)
        if elem[0]['director_name'] == director_name :
            dirigidas.append(elem[1]['original_title'])
            calificacion+= float(elem[1]['vote_average'])
            numero+=1
    if len(dirigidas) >= 1 :
        print('El director '+ director_name + ' ha dirigido ' + str(numero) + ' peliculas, y la calificacion promedio de las mismas es '+ str(round((calificacion/numero),2))+ '.' )
        print('A continuacion se listan los nombres de las peliculas')
        print(dirigidas)
    else: 
        print('El director no esta en la lista, Intente nuevamente')

###
# la referenciacion [0] pertenece al casting de las peliculas y [1] a los detalles de las mismas.
#Funciones para requerimiento 2
###
def comparar_vote_count (movie1, movie2):
    return ( float(movie1[1]["vote_count"]) > float(movie2[1]["vote_count"]))

def comparar_vote_average (movie1, movie2):
    return ( float(movie1[1]["vote_average"]) > float(movie2[1]["vote_average"]))


def lista_ordenada_vote_count(list):
    sort.mergesort (list,comparar_vote_count)

def lista_ordenada_vote_average(list):    
    sort.mergesort(list,comparar_vote_average)

def requerimiento_2(option,masomenos, list, number,ascendente):
    var= 'vote_count'
    if option == 0 : ## vote average
        lista_ordenada_vote_average(list)
        var= 'vote_average'
    elif option == 1 : ## count
        lista_ordenada_vote_count(list)
    movies= list
    ascendente_vote= lt.newList()
    descendente_vote= lt.newList()
    lista_final= []
    if masomenos == 1 :  #### Las mas votadas ya sea ascendente o descendente.

        if ascendente == 1 :
            for k in range (1, number+1):
                tuple1=("Id: ",lt.getElement (movies, k)[0]["id"],"Title: ",lt.getElement (movies, k)[1]["original_title"],var,lt.getElement (movies, k)[1][var]  )
                lt.addFirst (ascendente_vote, tuple1)
            size= lt.size(ascendente_vote)
            for i in range(0,(size+1)):
                element= lt.getElement(ascendente_vote,i)
                if element not in lista_final :
                    lista_final.append(element)
            return lista_final
        elif ascendente == 0 :
            for k in range (1, number+1):
                tuple1=("Id: ",lt.getElement (movies, k)[0]["id"],"Title: ",lt.getElement (movies, k)[1]["original_title"],var,lt.getElement (movies, k)[1][var]  )
                lt.addLast(descendente_vote, tuple1)
            size= lt.size(descendente_vote)
            for i in range(0,(size+1)):
                element= lt.getElement(descendente_vote,i)
                if element not in lista_final :
                    lista_final.append(element)
            return lista_final
        else:
            print('Tipo de ordenamiento no valido')
    elif masomenos == 0 : ####Menos votadas ya sea ascendente o descendente.
        si= lt.size(movies)
        inf= si - number
        if ascendente == 1 :
            for k in range (inf,si):
                tuple1=("Id: ",lt.getElement (movies, k)[0]["id"],"Title: ",lt.getElement (movies, k)[1]["original_title"],var,lt.getElement (movies, k)[1][var]  )
                lt.addFirst (ascendente_vote, tuple1)
            size= lt.size(ascendente_vote)
            for i in range(0,(size+1)):
                element= lt.getElement(ascendente_vote,i)
                if element not in lista_final :
                    lista_final.append(element)
            return lista_final
        elif ascendente == 0 :
            for k in range (inf, si):
                tuple1=("Id: ",lt.getElement (movies, k)[0]["id"],"Title: ",lt.getElement (movies, k)[1]["original_title"],var,lt.getElement (movies, k)[1][var]  )
                lt.addLast(descendente_vote, tuple1)
            size= lt.size(descendente_vote)
            for i in range(0,(size+1)):
                element= lt.getElement(descendente_vote,i)
                if element not in lista_final :
                    lista_final.append(element)
            return lista_final
        else:
            print('Tipo de ordenamiento no valido')
    else :
        print('Syntax Error')


#Requerimiento 6. Crear Ranking del género

def promedios_genero(lista,genero_buscado):
    #pasamos el str buscado a minusculas, y eliminamos cualquier caracter que pueda generar errores en la búsqueda
    genero_buscado=(((genero_buscado.lower()).replace(" ","")).replace("-","")).replace("y","")
    promedio_votos=0
    promedio_puntaje=0
    peliculas_de_un_genero= lt.newList()
    peliculas_del_genero_vote_avarenge=lt.newList()
    peliculas_del_genero_vote_count=lt.newList()
    
    recorrido = 0

    while recorrido <= lt.size(lista):
        elemento=lt.getElement(lista,recorrido)
        genero_comparado= ((str(elemento[1]["genres"]).replace("|","")).lower()).replace(" ","")
        if  genero_comparado == genero_buscado:
            lt.addLast(peliculas_de_un_genero, elemento)
            promedio_puntaje+=float(elemento[1]["vote_average"])
            promedio_votos+=float(elemento[1]["vote_count"])
             
        recorrido+=1

    size=int(lt.size(peliculas_de_un_genero))
    promedio_votos=promedio_votos/size
    promedio_puntaje=promedio_puntaje/size
    
    
    sort.mergesort(peliculas_del_genero_vote_count,comparar_vote_count)
    return (peliculas_de_un_genero, promedio_votos, promedio_puntaje,size)
    
    


def ranking_genero_average(number,lista,genero_buscado):
    peliculas_de_un_genero=promedios_genero(lista,genero_buscado)
    lista_ordenada_vote_average = lt.newList
    
    lista_mejores_calificadas_ascendente=lt.newList()
    lista_mejores_calificadas_descendente=lt.newList()
    recorrido=0
    while recorrido <= int(lt.size(lista_ordenada_vote_average)):
        elemento=lt.getElement(lista_ordenada_vote_average,recorrido)[1]
        tupla1= ("Titulo: ",elemento["original_title"], "Vote_Average: ", elemento["vote_average"], "Genero: ", elemento["genres"])
        lt.addFirst(lista_mejores_calificadas_ascendente, tupla1)
        lt.addLast(lista_mejores_calificadas_descendente,tupla1)
    return(lista_mejores_calificadas_ascendente, lista_mejores_calificadas_descendente)


#MENU
def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """


    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:

            if int(inputs[0])==1: #opcion 1
                list_type1 = 'ARRAY_LIST'
                list_type2 = 'SINGLE_LINKED'
                file1 = 'Data/theMoviesdb/MoviesCastingRaw-small.csv'
                file2 = 'Data/theMoviesdb/SmallMoviesDetailsCleaned.csv'
                lst_movies_array_list= get_two_csv(file1,file2,list_type1)
                lst_movies_single_linked= get_two_csv(file1,file2,list_type2)
                print("Datos cargados, " + str(lt.size(lst_movies_single_linked)) + " elementos cargados")

            elif int(inputs[0])==2: #opcion 2
                pass
                num1= int(input('Ingrese el numero de peliculas para el ranking de segun la cantidad de votos : '))
                masomenos1= int(input('Ingrese 1 si desea obtener las mas votadas, o ingrese 0 si desea las menos votadas : '))
                ascen1= int(input('Si quiere obtener las peliculas del ranking vote count en orden ascendente ingrese 1, para descendente ingrese 0 : '))
                num2= int(input('Ingrese el numero de peliculas para el ranking de segun el promedio de los votos : '))
                masomenos2= int(input('Ingrese 1 si desea las peliculas con mejor promedio, o ingrese 0 si desea las de peor promedio : '))
                ascen2= int(input('Si quiere obtener las peliculas del ranking vote average en orden ascendente ingrese 1, para descendente ingrese 0 : '))
                with_count= requerimiento_2(1,masomenos1,lst_movies_single_linked,num1,ascen1)
                with_average= requerimiento_2(0,masomenos2,lst_movies_single_linked,num2,ascen2)
                print('El ranking de vote count solicitado es :')
                print(with_count)
                print('El ranking de vote average solicitado es :')
                print(with_average)

            elif int(inputs[0])==3: #opcion 3
                pass
                dir= input('Ingrese el nombre del Director: ')

                peliculas_de_un_director(lst_movies_array_list,dir)
                

            elif int(inputs[0])==4: #opcion 4
                pass

            elif int(inputs[0])==5: #opcion 5
              """  genero_buscado= input("Ingrese el género que desea consultar: ")
                lista_promedios_genero=promedios_genero(lst_movies_single_linked,genero_buscado)
                
                print("Se encontraron " + str(promedios_genero(lst_movies_single_linked,genero_buscado)[4]) +" peliculas del género " + genero_buscado + ". Este género tiene un promedio de votación de " + str(promedios_genero(lst_movies_single_linked,genero_buscado)[2]) + " y un promedio de puntuacion de " + str(promedios_genero(lst_movies_single_linked,genero_buscado)[3]))

                print(" Lista de rankings ofrecidos de este género: \n 1. Lista de las peliculas mejor calificadas. \n 2. Lista de peliculas peor calificadas.")
                print(" 3. Lista de peliculas más votadas. \n 4. Lista de peliculas menos votadas")
                ranking_deseado=int(input("Ingrese el ranking que desea consultar: "))
                number= int(input("Ingrese el número de peliculas que desea ver en el ranking: "))
                if ranking_deseado == 1:
                    mejores_calificadas=ranking_genero_average(number,lst_movies_single_linked,genero_buscado)
                   # print("Las peliculas del genero " + genero_buscado + "ordenadas de manera ascendente son: "+ str(mejores_calificadas[0]))
                    #print("Las peliculas del genero " + genero_buscado + "ordenadas de manera descendente son: "+ str(mejores_calificadas[1]))



                #elif ranking_deseado ==2:
                #elif ranking_deseado == 3:
               # elif ranking_deseado ==4:
                    """

            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()