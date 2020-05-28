
def main():
    import random 
    m=int(input("Ingrese la cantidad de m => Filas...: "))
    n=int(input("Ingrese la cantidad de n => Columnas...: "))
    a=[]
    mayores = []
    
    for i in range(0, m):
        a.append([999]*n)
    
    def llenar(ma,z,w):
        for i in range(0,z,1):
            for j in range(0,w,1):
                valor = (random.randint(100, 1000))
                ma[i][j] = valor
        return

    def mostrar(ma,z,w):
        for i in range(0,z,1):
            print()
            for j in range(0,w,1):
                print(ma[i][j],'\t',end="")
        return
    
    
    def sumaMatrizPrincipal(ma,z,w):
        total = 0 
        for i in range(0,z,1):
            print()
            for j in range(0,w,1):
                if(j==i):
                    total+=ma[i][j]
        return total
 
    def sumaMatrizSecundaria(ma,z,w):
        total = 0 
        for i in range(w):
            total+=ma[i][w-i-1]
        return total
    
    def promedioFilas(ma, z, w):
        promedio = 0
        for i in range(0,z, 1):
            for j in range(0, w, 1):
                promedio+= ma[i][j]
            print("Promedio de la fila "+str(i), (promedio/w))
        return

    def promedioColumnas(ma, z, w):
        promedio = 0
        for i in range(0,w, 1):
            mayor=0
            for j in range(0, z, 1):
                promedio+= ma[j][i]
                if(ma[j][i] > mayor):
                    mayor = ma[j][i]
            mayores.append(mayor)
            print("Promedio de la columna "+str(i), (promedio/z))
        return

    def promedioMatriz(ma, z, w):
        promedio = 0
        for i in range(0,z, 1):
            for j in range(0, w, 1):
                promedio+= ma[i][j]
        print("Promedio de todos los elementos de la matriz ", (promedio/(z*w)))
        return
        
    def mostrarMayores(mayores):
        i = 0
        for m in mayores:
            print("El elemento mayor de la columna "+str(i)+" es ",m)
            i+=1
    
    c=str(input("Presione enter para ingresar los datos...........: "))
    llenar(a,m,n)
    c=str(input("Presione enter para ver los datos...: "))
    mostrar(a,m,n) 
    print()
    c=str(input("Presione enter para ver la suma de los elementos de la diagonal principal ...: "))
    print("La suma de los elementos es: ", sumaMatrizPrincipal(a,m,n))
    print()
    c=str(input("Presione enter para ver la suma de los elementos de la diagonal secundaria ...: "))
    print("La suma de los elementos es: ", sumaMatrizSecundaria(a,m,n))
    print()
    c=str(input("Presione enter para ver el promedio de los elementos de cada fila ...: "))
    promedioFilas(a,m,n)
    print()
    c=str(input("Presione enter para ver el promedio de los elementos de cada columna ...: "))
    promedioColumnas(a,m,n)
    print()
    c=str(input("Presione enter para ver el promedio de todos los elementos de la matriz ...: "))
    promedioMatriz(a,m,n)
    print()
    c=str(input("Presione enter para ver el vectores con los mayores de cada columna ...: "))
    mostrarMayores(mayores)
    print()
    print ("Terminamos.........................")
main()