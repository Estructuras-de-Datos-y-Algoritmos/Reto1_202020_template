
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
from time import process_time 



def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Mejores peliculas de un director")#requerimiento 1
    print("3- Crear ranking de peliculas")#requerimiento 2
    print("4- Conocer un director") #requerimiento 3
    print("5- Conocer un actor")#requerimiento 4
    print('6- Entender un genero')#requerimiento 5
    print("7- Ranking del Genero")#requerimiento 6
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
#REQUERIMIENTO 1 #opcion 2 del menu

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
        return((count,round((sum/count),2)))
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



#Funciones para requerimiento 2

def comparar_vote_count (movie1, movie2):
    return ( float(movie1[1]["vote_count"]) > float(movie2[1]["vote_count"]))

def comparar_vote_average (movie1, movie2):
    return ( float(movie1[1]["vote_average"]) > float(movie2[1]["vote_average"]))


def lista_ordenada_vote_count(list):
    lt.tad_merge(list,comparar_vote_count)
    return list


def obtener_peliculas_mas_votadas (list, number):
    movies = lista_ordenada_vote_count(list)
    peliculas_mas_votadas_ascendente= lt.newList("ARRAY_LIST")
    peliculas_mas_votadas_descendente= lt.newList("ARRAY_LIST")
    for cont in range (1, number+1):
        tuple1=("Id: ",lt.getElement (movies, cont)[0]["id"],"Title: ",lt.getElement (movies, cont)[1]["original_title"],"Vote_Count: ",lt.getElement (movies, cont)[1]["vote_count"]  )
        lt.addFirst (peliculas_mas_votadas_ascendente, tuple1)
        lt.addLast (peliculas_mas_votadas_descendente, tuple1)
    return (peliculas_mas_votadas_descendente["elements"],peliculas_mas_votadas_ascendente["elements"])

def obtener_peliculas_menos_votadas (list, number):
    movies = lista_ordenada_vote_count(list)
    peliculas_menos_votadas_ascendente= lt.newList("ARRAY_LIST")
    peliculas_menos_votadas_descendente= lt.newList("ARRAY_LIST")
    si= int(lt.size(movies))
    inf= si - number
    for k in range (inf+1, si+1):
        tuple1=("Id: ",lt.getElement (movies, k)[0]["id"],"Title: ",lt.getElement (movies, k)[1]["original_title"],"Vote_Count: ",lt.getElement (movies, k)[1]["vote_count"]  )
        lt.addLast (peliculas_menos_votadas_descendente, tuple1)
        lt.addFirst (peliculas_menos_votadas_ascendente, tuple1)
        
    return (peliculas_menos_votadas_descendente["elements"],peliculas_menos_votadas_ascendente["elements"])

def lista_ordenada_vote_average(list):
    lt.tad_merge(list,comparar_vote_average)
    return list


def obtener_peliculas_mejor_votadas (list, number):
    movies = lista_ordenada_vote_average(list)
    peliculas_mejores_calificaciones_ascendente= lt.newList("ARRAY_LIST")
    peliculas_mejores_calificaciones_descendente= lt.newList("ARRAY_LIST")
    for cont in range (1, number+1):
        tuple1=("Id: ",lt.getElement (movies, cont)[0]["id"],"Title: ",lt.getElement (movies, cont)[1]["original_title"],"Vote_Average: ",lt.getElement (movies, cont)[1]["vote_average"]  )
        lt.addFirst (peliculas_mejores_calificaciones_ascendente, tuple1)
        lt.addLast (peliculas_mejores_calificaciones_descendente, tuple1)
    return (peliculas_mejores_calificaciones_descendente["elements"],peliculas_mejores_calificaciones_ascendente["elements"])

def obtener_peliculas_peor_votadas (list, number):
    movies = lista_ordenada_vote_average(list)
    peliculas_peor_calificadas_ascendente= lt.newList("ARRAY_LIST")
    peliculas_peor_calificadas_descendente= lt.newList("ARRAY_LIST")
    si= int(lt.size(movies))
    inf= si - number
    for k in range (inf+1, si+1):
        tuple1=("Id: ",lt.getElement (movies, k)[0]["id"],"Title: ",lt.getElement (movies, k)[1]["original_title"],"Vote_Average: ",lt.getElement (movies, k)[1]["vote_average"]  )
        lt.addLast (peliculas_peor_calificadas_descendente, tuple1)
        lt.addFirst (peliculas_peor_calificadas_ascendente, tuple1)
    return (peliculas_peor_calificadas_descendente["elements"],peliculas_peor_calificadas_ascendente["elements"])

#Requerimiento 6. Crear Ranking del género
#1. Buscamos todas las películas de un genero

def promedios_genero(lista,genero_buscado):
    #pasamos el str buscado a minusculas, y eliminamos cualquier caracter que pueda generar errores en la búsqueda
    genero_buscado=(((genero_buscado.lower()).replace(" ","")).replace("-",""))
    promedio_votos=0
    promedio_puntaje=0
    peliculas_de_un_genero= lt.newList()
    recorrido = 0

    while recorrido <= int(lt.size(lista)):
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
    
    return (peliculas_de_un_genero, round(promedio_votos,2), round(promedio_puntaje,2),size)
    
# Ordenar la lista por puntuación
def ordenar_peliculas_genero_vote_average(lista,genero_buscado):
    lista_genero= promedios_genero(lista,genero_buscado)[0]
    lt.tad_merge(lista_genero,comparar_vote_average)
    return lista_genero

def ranking_las_mejor_votadas_del_genero(lista,genero_buscado,number):
    lista_ordenada_vote_average_genero= ordenar_peliculas_genero_vote_average(lista,genero_buscado)
    mejor_votadas_del_genero_ascendente=lt.newList("ARRAY_LIST")
    mejor_votadas_del_genero_descendente=lt.newList("ARRAY_LIST")
    for k in range(1, number+1):
        element=lt.getElement(lista_ordenada_vote_average_genero,k)
        tuple1=("Titulo:",element[1]["original_title"], "Vote Average: ",element[1]["vote_average"], "Genero: ",element[1]["genres"])
        lt.addFirst(mejor_votadas_del_genero_ascendente,tuple1)
        lt.addLast(mejor_votadas_del_genero_descendente,tuple1)
    return (mejor_votadas_del_genero_ascendente["elements"],mejor_votadas_del_genero_descendente["elements"])

def ranking_las_peor_votadas_del_genero(lista,genero_buscado,number):
    lista_ordenada_vote_average_genero= ordenar_peliculas_genero_vote_average(lista,genero_buscado)
    peor_votadas_del_genero_ascendente=lt.newList("ARRAY_LIST")
    peor_votadas_del_genero_descendente=lt.newList("ARRAY_LIST")
    si= int(lt.size(lista_ordenada_vote_average_genero))
    inf= si-number
    for k in range(inf+1, si+1):
        element=lt.getElement(lista_ordenada_vote_average_genero,k)
        tuple1=("Titulo:",element[1]["original_title"], "Vote Average: ",element[1]["vote_average"], "Genero: ",element[1]["genres"])
        lt.addFirst(peor_votadas_del_genero_descendente,tuple1)
        lt.addLast(peor_votadas_del_genero_ascendente,tuple1)
    return (peor_votadas_del_genero_ascendente["elements"],peor_votadas_del_genero_descendente["elements"])

#Ordenar la lista por votacion
def ordenar_peliculas_genero_vote_count(lista,genero_buscado):
    lista_genero= promedios_genero(lista,genero_buscado)[0]
    lt.tad_merge(lista_genero,comparar_vote_count)
    return lista_genero

def ranking_las_mas_votadas_del_genero(lista,genero_buscado,number):
    lista_ordenada_vote_count_genero= ordenar_peliculas_genero_vote_count(lista,genero_buscado)
    mas_votadas_del_genero_ascendente=lt.newList("ARRAY_LIST")
    mas_votadas_del_genero_descendente=lt.newList("ARRAY_LIST")
    for k in range(1, number+1):
        element=lt.getElement(lista_ordenada_vote_count_genero,k)
        tuple1=("Titulo:",element[1]["original_title"], "Vote Count: ",element[1]["vote_count"], "Genero: ",element[1]["genres"])
        lt.addFirst(mas_votadas_del_genero_ascendente,tuple1)
        lt.addLast(mas_votadas_del_genero_descendente,tuple1)
    return (mas_votadas_del_genero_ascendente["elements"],mas_votadas_del_genero_descendente["elements"])

def ranking_las_menos_votadas_del_genero(lista,genero_buscado,number):
    lista_ordenada_vote_count_genero= ordenar_peliculas_genero_vote_count(lista,genero_buscado)
    menos_votadas_del_genero_ascendente=lt.newList("ARRAY_LIST")
    menos_votadas_del_genero_descendente=lt.newList("ARRAY_LIST")
    si= int(lt.size(lista_ordenada_vote_count_genero))
    inf= si-number
    for k in range(inf+1, si+1):
        element=lt.getElement(lista_ordenada_vote_count_genero,k)
        tuple1=("Titulo:",element[1]["original_title"], "Vote Count: ",element[1]["vote_count"], "Genero: ",element[1]["genres"])
        lt.addFirst(menos_votadas_del_genero_descendente,tuple1)
        lt.addLast(menos_votadas_del_genero_ascendente,tuple1)
    return (menos_votadas_del_genero_ascendente["elements"],menos_votadas_del_genero_descendente["elements"])

# Ordenar la lista por votacion
    


#sort.mergesort(peliculas_del_genero_vote_count,comparar_vote_count)
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
                
                dir= input('Ingrese el nombre del Director: ')
                peliculas= good_movies(lst_movies_array_list,dir)
                print("De el director "+ dir + " se encontraron " + str(peliculas[0]) + " peliculas buenas. El promedio de la puntuación de estas películas es: " + str(peliculas[1]))

            elif int(inputs[0])==3: #opcion 3
                    print("1 -Ver películas más votadas en orden descendente")
                    print("2- Ver películas más votadas en orden ascendente")
                    print("3- Ver películas menos votadas en orden descendente")
                    print("4- Ver películas menos votadas en orden ascendente")
                    print("5- Ver películas mejor votadas en orden descendente")
                    print("6- Ver películas mejor votadas en orden ascendente")
                    print("7- Ver películas peor votadas en orden descendente")
                    print("8- Ver películas peor votadas en orden ascendente")
                    print("9- Volver a menú principal")

                    inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
                    if len(inputs)>0:
                        if int(inputs[0])==1: 
                            number=int(input("Ingrese el número de peliculas que desea ver en el ranking: \n"))
                            print("Las películas más votadas en orden descendente son:\n " + str(obtener_peliculas_mas_votadas(lst_movies_single_linked,number)[0] )  )
                        elif int(inputs[0])==2:
                            number=int(input("Ingrese el número de peliculas que desea ver en el ranking: \n"))
                            print("Las películas más votadas en orden ascendente son:\n " + str(obtener_peliculas_mas_votadas(lst_movies_single_linked,number)[1] )  )
                        elif int(inputs[0])==3:
                            number=int(input("Ingrese el número de peliculas que desea ver en el ranking: \n"))
                            print("Las películas menos votadas en orden descendente son:\n " + str(obtener_peliculas_menos_votadas(lst_movies_single_linked,number)[0] ))
                        elif int(inputs[0])==4: 
                            number=int(input("Ingrese el número de peliculas que desea ver en el ranking: \n"))
                            print("Las películas menos votadas en orden ascendente son:\n " + str(obtener_peliculas_menos_votadas(lst_movies_single_linked,number)[1] )  )
                        elif int(inputs[0])==5:
                            number=int(input("Ingrese el número de peliculas que desea ver en el ranking: \n"))
                            print("Las películas mejor calificadas en orden descendente son:\n " + str(obtener_peliculas_mejor_votadas(lst_movies_single_linked,number)[0] ))
                        elif int(inputs[0])==6:
                            number=int(input("Ingrese el número de peliculas que desea ver en el ranking: \n"))
                            print("Las películas mejor calificadas en orden ascendente son:\n " + str(obtener_peliculas_mejor_votadas(lst_movies_single_linked,number)[1] )  )
                        elif int(inputs[0])==7:
                            number=int(input("Ingrese el número de peliculas que desea ver en el ranking: \n"))
                            print("Las películas peor calificadas en orden descendente son:\n " + str(obtener_peliculas_peor_votadas(lst_movies_single_linked,number)[0] ))
                        elif int(inputs[0])==8:
                            number=int(input("Ingrese el número de peliculas que desea ver en el ranking: \n"))
                            print("Las películas peor calificadas en orden ascendente son:\n " + str(obtener_peliculas_peor_votadas(lst_movies_single_linked,number)[1] )  )
                        elif int(inputs[0])==9:       
                            printMenu() #imprimir el menu de opciones en consola
                            inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada

                

            elif int(inputs[0])==4: #opcion 4
                dir= input('Ingrese el nombre del Director: ')

                peliculas_de_un_director(lst_movies_single_linked,dir)

            elif int(inputs[0])==5: #opcion 5
                pass


            elif int(inputs[0])==6: #opcion 6
                genero_buscado= input("Ingrese el género que desea consultar: ")
                datos_genero=promedios_genero(lst_movies_single_linked,genero_buscado)
                print("Se encontraron " + str(datos_genero[3]) +" peliculas del género " + genero_buscado + ". Este género tiene un promedio de votación de " + str(datos_genero[1]) + " y un promedio de puntuacion de " + str(datos_genero[2]))


            elif int(inputs[0])==7: #opcion 7
                genre= input(' Ingrese el genero para el cual desea crear el ranking: ')
                print(" Lista de rankings ofrecidos de este género: \n 1. Lista de las peliculas mejor calificadas. \n 2. Lista de peliculas peor calificadas.")
                print(" 3. Lista de peliculas más votadas. \n 4. Lista de peliculas menos votadas")
                ranking_deseado=int(input("Ingrese el ranking que desea consultar: "))
                number= int(input("Ingrese el número de peliculas que desea ver en el ranking: "))
                if ranking_deseado == 1:
                    las_mejor_votadas_del_genero= ranking_las_mejor_votadas_del_genero(lst_movies_single_linked ,genre,number)
                    print("Las peliculas mejor votadas del genero " + genre + " ordenadas de manera ascendente son: "+ str(las_mejor_votadas_del_genero[0]))
                    print("Las peliculas mejor votadas del genero " + genre + " ordenadas de manera descendente son: "+ str(las_mejor_votadas_del_genero[1]))

                elif ranking_deseado ==2:
                    las_peor_votadas_del_genero= ranking_las_peor_votadas_del_genero(lst_movies_single_linked ,genero_buscado,number)
                    print("Las peliculas peor votadas del genero " + genre + " ordenadas de manera ascendente son: "+ str(las_peor_votadas_del_genero[0]))
                    print("Las peliculas peor votadas del genero " + genre + " ordenadas de manera descendente son: "+ str(las_peor_votadas_del_genero[1]))


                elif ranking_deseado == 3:
                    las_mas_votadas_del_genero= ranking_las_mas_votadas_del_genero(lst_movies_single_linked ,genero_buscado,number)
                    print("Las peliculas mas votadas del genero " + genre + " ordenadas de manera ascendente son: "+ str(las_mas_votadas_del_genero[0]))
                    print("Las peliculas mas votadas del genero " + genre + " ordenadas de manera descendente son: "+ str(las_mas_votadas_del_genero[1]))
                elif ranking_deseado ==4:
                    las_menos_votadas_del_genero= ranking_las_menos_votadas_del_genero(lst_movies_single_linked ,genero_buscado,number)
                    print("Las peliculas menos votadas del genero " + genre + " ordenadas de manera ascendente son: "+ str(las_menos_votadas_del_genero[0]))
                    print("Las peliculas menos votadas del genero " + genre + " ordenadas de manera descendente son: "+ str(las_menos_votadas_del_genero[1]))
                    

            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()