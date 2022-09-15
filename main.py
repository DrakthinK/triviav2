
""" 223 horizontal , 219 vertical ascii """
from glob import glob
from optparse import Values
import os 
import sys 
import time
import random
BLUE, RED, WHITE, CYAN, DEFAULT, YELLOW, MAGENTA, GREEN, END, BOLD = '\033[34m', '\033[31m', '\33[37m', '\033[36m', '\033[0m', '\033[33m', '\033[35m', '\033[32m', '\033[0m', '\033[1m'
points=0
preguntasCompletados=[]
opcionesRestantes=[1,2,3,4]
competitor=''
def banner():
    print ('\n') 
    print(f' {BLUE}------------------------------------------------------------------------')
    print (f'{BLUE}|███████╗ ██╗ ██╗       ╔███████╗   █████████╗   ██║  ██╗   ████████╗   |')
    print (f'{BLUE}|██╔════╝ ██║ ██║      ██╔═════██╗  ██║      █║  ██║  ██║        ██╔╝   |')		
    print (f'{BLUE}|███████╗ ██║ ██║      ██║     ██║  █████████║   ██║  ██║      ███╔╝    |')
    print (f'{BLUE}| ╚═══██║ ██║ ██║      ██║███████║  ██║      █║  ██║  ██║    ██╔══╝     |')
    print (f'{BLUE}|███████║ ██║ ███████╗ ██║     ██║  █████████║   ██████╔╝    ████████║  |')
    print (f'{BLUE}|╚══════╝ ╚═╝ ╚══════╝ ╚═╝     ╚═╝  ╚════════╝   ╚═════╝     ╚═══════╝  |')
    print (f'{RED}|     	                     "PROGRAMA DE PRE SELECCION MTPE"           |')
    print (f'{RED}|                                       BY: PIERO PEZO MARIN            |')
    print (f'{RED}|                                   correo: pierbryanunu@gmail.com      |')
    print(f'{BLUE} ------------------------------------------------------------------------')
    print ('\n\n')

def menu(preguntasCompletados):
    global opcionesRestantes
    ALLPREGUNTAS={1:'Caracteristicas de Python',2:'Definicion Hardware',3:'Definicion Software',4:'Salir'}
    
    if len(preguntasCompletados)==0:
        print ('------------------------------------------------------------------------------------- ')	
        print ('||                                        OPCIONES                                   ||')
        print ('||-----------------------------------------------------------------------------------||')
        print ('||                                                                                   ||')
        print ('||          [01] Caracteristicas de Python                                           ||')
        print ('||                                                                                   ||')
        print ('||          [02] Definicion Hardware                                                 ||')
        print ('||                                                                                   ||')
        print ('||          [03] Definicion Software                                                 ||')
        print ('||                                                                                   ||')
        print ('||          [04] Salir                                                               ||')
        print (' ------------------------------------------------------------------------------------- ')
    else:
        os.system('clear')
        print ('------------------------------------------------------------------------------------- ')	
        print ('||                                        OPCIONES                                   ||')
        print ('||-----------------------------------------------------------------------------------||')
        print ('||                                                                                   ||')
        for key,pregunta in ALLPREGUNTAS.items():
            if key not in preguntasCompletados:
                print ('||          ['+str(key)+']'+ALLPREGUNTAS[key]+'                           ')         
        print (' ------------------------------------------------------------------------------------- ')
def options():
    global points
    global preguntasCompletados
    global competitor
    global opcionesRestantes
    menu(preguntasCompletados)
    OPTIONES=[1,2,3,4]
    if competitor=='':      
        competitor =input("Hola,¿Cual es tu nombre? ").replace(' ','').upper()
    print("!Bienvenido ",competitor,'.El juego consiste en responder la pregunta correcta.!')
    pointslocal=0;
    print("[+]Cada pregunta contestada correctamente, te ortogara puntos alatoriamente,y se mostrara al final del juego")
    print(f"{GREEN}[+]Solo tienes  2 intentos para responder cada pregunta,Debido a que tengo 3 opciones por pregunta :)")
    opprincipal="-".join([str(i) for i in opcionesRestantes])
    option = input(f"Opcion [{opprincipal}]>>")
    if option=='':
       print(f"{GREEN}[+] No es una Opcion valida,escriba un numero de las opciones")
       input("clear para continuar...")
       os.system('clear')
    elif int(option)  in preguntasCompletados:
        print(f"{GREEN}[+] No es una Opcion valida,respuesta completada ")
        input("pulsa enter para continuar...")
    elif option == '1' :
        INTENTOS=2
        print(f"{GREEN}[+]Comencemos!, esta pregunta se trata sobre el lenguaje de programacion Python")
        input("pulsa enter para ver las opciones...") 
        while True:
            os.system('clear')
            print ('============================================PREGUNTA1==================================')
            print('[+]¿Cuales de las opciones tienen por caracteristicas el leguaje de programacion python?||')
            print ('[01] compilado ,Estaticamente Tipado,Debilmente Tipado                                   ||')
            print ('[02] Debilmente Tipado,Dinamicamente Tipado,interpretado                               ||')
            print ('[03] Interpretado,Dinamicamente Tipado,Fuertemente Tipado                              ||')
            print ('[04] Salir                                                                             ||')
            print ('============================================PREGUNTA1==================================')
            op = input("Su respuesta es:>>$ ")
            os.system('clear')
            print("[+] verificando..... ")
            time.sleep(0.4)
            INTENTOS-=1 
            if  op=='1' or op=='2':
                print(f"{GREEN}[+] Lo sentimos respuesta incorrecta :/ pipipi!")
                print(f"{GREEN}[+] {competitor} te quedan {INTENTOS} intentos :) ")
                input("pulsa enter para continuar...")
            elif  op=='3':
                pointslocal=random.randint(1,10)
                points+=pointslocal
                print(f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
                print(f"░░░░░░░░░░░░░░░░░░¡Felicidades .La Respuesta es correcta...! :)░░░░░░░░░░░░░░░░░░░░░░")
                print(f"░░░░░░░░░░░░░░░░░░¡{competitor} lo lograstes! al intento {2-INTENTOS}!....░░░░░░░░░░░")
                print(f"░░░░░░░░░░░░░░░░░░¡{competitor} Acumulastes {points} puntos ,pregunta completada...░░░░░░░░░░░")
                print(f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
                preguntasCompletados.append(1)
                opcionesRestantes.remove(1)
                break
            elif op=='4':
                info(2-(INTENTOS+1),points,competitor)
                break;
            elif op not in OPTIONES:
                INTENTOS=2
                print(f"{GREEN}[+] No es una Opcion valida ")
                input("pulsa enter para continuar...")
            if INTENTOS==0:
                print(f"{GREEN}[+] Lo sentimos se acabo el numero de intentos :) Perdistes")
                info(2,points,competitor)
                res=input(f"{GREEN}[+] Desea seguir intentando la pregunta 1?:s/n").lower()
                if res=='s':
                    INTENTOS=2
                    pointslocal=0
                else:
                    info(2-INTENTOS,points,competitor)
                    break
    elif option == '2':
        INTENTOS=2
        print(f"{GREEN}[+]Comencemos!, esta pregunta se trata sobre Hardware")
        input("pulsa enter para ver las opciones...") 
        while True:
            os.system('clear')
            print ('============================================PREGUNTA2==================================')
            print('[+]¿Cual de las siguientes alternativos es la definicion de Hardware?                    ||')
            print ('[01] El Hadware es la parte física del computador, la parte tangible                   ||')
            print ('[02] Es la Unidad Central de Procesamiento                                             ||')
            print ('[03] El Hardware es la parte física del computador, la parte intangible                ||')
            print ('[04] Salir                                                                             ||')
            print ('============================================PREGUNTA2==================================')
            op = input("Su respuesta es:>>$ ")
            os.system('clear')
            print("[+] verificando..... ")
            time.sleep(0.4)
            INTENTOS-=1 
            if  op=='2' or op=='3':
                print(f"{GREEN}[+] Lo sentimos  respuesta incorrecta :/ pipipi!")
                print(f"{GREEN}[+] {competitor} te quedan {INTENTOS} intentos :) ")
                input("pulsa enter para continuar...")
            elif  op=='1':
                pointslocal=random.randint(1,10)
                points+=pointslocal
                print(f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
                print(f"░░░░░░░░░░░░░░░░░░¡Felicidades .La Respuesta es correcta...! :)░░░░░░░░░░░░░░░░░░░░░░")
                print(f"░░░░░░░░░░░░░░░░░░¡{competitor} lo lograstes! al intento {2-INTENTOS}!....░░░░░░░░░░░")
                print(f"░░░░░░░░░░░░░░░░░░¡{competitor} Acumulastes {points} puntos ,pregunta completada...░░░░░░░░░░░")
                print(f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
                preguntasCompletados.append(2)
                opcionesRestantes.remove(2)
                break
            elif op=='4':
                info(2-(INTENTOS+1),points,competitor)
                break;
            elif op not in OPTIONES:
                INTENTOS=2
                print(f"{GREEN}[+] No es una Opcion valida ")
                input("pulsa enter para continuar...")
            if INTENTOS==0:
                print(f"{GREEN}[+] Lo sentimos se acabo el numero de intentos :) Perdistes")
                info(2,points,competitor)
                res=input(f"{GREEN}[+] Desea seguir intentando la pregunta 1?:s/n").lower()
                if res=='s':
                    INTENTOS=2
                    pointslocal=0
                else:
                    info(2-INTENTOS,points,competitor)
                    break
    elif option == '3':
        INTENTOS=2
        print(f"{GREEN}[+]Comencemos!, esta pregunta se trata sobre Software")
        input("pulsa enter para ver las opciones...") 
        while True:
            os.system('clear')
            print ('============================================PREGUNTA3==================================')
            print('[+]¿Cual de las siguientes alternativos corresponde a una definicion de Software?       ||')
            print ('[01] Es la parte tangible y logico del ordenador                                       ||')
            print ('[02] Se define como la parte cuantitativa del ordenador                                ||')
            print ('[03] Software es el equipamiento lógico e intangible de un ordenador                   ||')
            print ('[04] Salir                                                                             ||')
            print ('============================================PREGUNTA3==================================')
            op = input("Su respuesta es:>>$ ")
            os.system('clear')
            print("[+] verificando..... ")
            time.sleep(0.4)
            INTENTOS-=1 
            if  op=='1' or op=='2':
                print(f"{GREEN}[+] Lo sentimos  respuesta incorrecta :/ pipipi!")
                print(f"{GREEN}[+] {competitor} te quedan {INTENTOS} intentos :) ")
                input("pulsa enter para continuar...")
            elif  op=='3':
                pointslocal=random.randint(1,10)
                points+=pointslocal
                print(f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
                print(f"░░░░░░░░░░░░░░░░░░¡Felicidades .La Respuesta es correcta...! :)░░░░░░░░░░░░░░░░░░░░░░")
                print(f"░░░░░░░░░░░░░░░░░░¡{competitor} lo lograstes! al intento {2-INTENTOS}!....░░░░░░░░░░░")
                print(f"░░░░░░░░░░░░░░░░░░¡{competitor} Acumulastes {points} puntos ,pregunta completada...░░░░░░░░░░░")
                print(f"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
                preguntasCompletados.append(3)
                opcionesRestantes.remove(3)
                break
            elif op=='4':
                info(2-(INTENTOS+1),points,competitor)
                break;
            elif op not in OPTIONES:
                INTENTOS=2
                print(f"{GREEN}[+] No es una Opcion valida ")
                input("pulsa enter para continuar...")
            if INTENTOS==0:
                print(f"{GREEN}[+] Lo sentimos se acabo el numero de intentos :) Perdistes")
                info(2,points,competitor)
                res=input(f"{GREEN}[+] Desea seguir intentando la pregunta 1?:s/n").lower()
                if res=='s':
                    INTENTOS=2
                    pointslocal=0
                else:
                    info(2-INTENTOS,points,competitor)
                    break
    elif option=='4':
        info(0,points,competitor)
        raise KeyboardInterrupt
    elif option not in opcionesRestantes:
         print(f"{GREEN}[+] No es una Opcion valida ")
         input("pulsa enter para continuar...")
         
    input("pulsa enter elegir la siguiente pregunta...")
    options()  
        
def info(intentos,points,competitor):
    print(f"{GREEN}[+] Gracias por participar\n")
    time.sleep(0.2)
    print("[AUTOR]: PIERO PEZO --> \n\n")
    for numero_carga in range(5,0,-1):
        time.sleep(0.2)
    if intentos==0:
        print (f"=========================================Information================================")
        print (f"||                                                                                 ||")
        print (f"||        [PARTICIPANTE]:{competitor}        [N° P.RESPONDIDAS] :{preguntasCompletados} [N° PUNTOS] :{points}  ||")
        print (f"||                                                                                 ||")
        print (f"====================================================================================")
    else:
        print (f"=========================================Information================================")
        print (f"||                                                                                 ||")
        print (f"||          [PARTICIPANTE]:{competitor}        [N° INTENTOS] :{intentos} [N° PUNTOS] :{points}  ||")
        print (f"||                                                                                 ||")
        print (f"====================================================================================")
    banner()

def main():
    banner()
    options()
    
if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print ('\nprograma  finalizado.....')
    else:
        input("pulsa enter para continuar...")
        os.system('clear')
        print ('finish..')      