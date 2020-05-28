import random 

#Creacion de Variables de entrada y de Salida
m=5
n=5
matriz=[]
productos=['Mascarilla', 'Guantes', 'Alcohol', 'Antibacterial', 'Gafas']
sedes=["NULL"]*m
totales = [0]*m
promedios = [0]*m

def inicializarMatriz():
    for i in range(0, m):
        matriz.append([0]*n)

def llenarMatriz(ma,z,w):
    for i in range(0,z,1):
        sedes[i]="Sede"+str(i+1)
        for j in range(0,w,1):
            valor_venta = (random.random())*100000
            ma[i][j] = round (valor_venta,2)
    return

def promedioTienda():
    totalTienda = 0
    for i in promedios:
        totalTienda+=i 
    return totalTienda/5

def mostrar(ma,z,w):
        for p in productos: 
            print('\t',p, " ", end="")
        print()
        for i in range(0,z,1):
            print()
            print(sedes[i]," ",end="") 
            for j in range(0,w,1):
                print(ma[i][j],'\t',end="")
        return


def mostrarTotalVentas(ma,z,w):
    total = 0 
    v = 0
    totalTienda = 0
    for i in range(0,z,1):
        print()
        print(sedes[i]," ",end="")
        for j in range(0,w,1):
            total+=ma[i][j]
            v = total
        print(total)
        promedios[i] = v
        totalTienda+=total
    print("El total de ventas de la tienda es: "+str(totalTienda))
    return

def compararPromedios(ma,z,w):
    total = 0 
    c = 0
    p = promedioTienda()
    for i in range(0,z,1):
        for j in range(0,w,1):
            total+=ma[i][j]
        if(total > p):
            c+=1
    return c


def mostrarMayor(ma,z,w):
    mayor = 0 
    pos = 0
    for i in range(0,z,1):
        print()
        mayor = ma[i][0]
        for j in range(0,w,1):
            if(ma[i][j] > mayor):
                mayor = ma[i][j]
                pos = j
        if(pos==0):
            print("El mayor en la sede "+str(i+1)+" es la mascarilla")
        elif(pos==1):
            print("El mayor en la sede "+str(i+1)+" son los guantes")
        elif(pos==2):
            print("El mayor en la sede "+str(i+1)+" es el alcohol")
        elif(pos==3):
            print("El mayor en la sede "+str(i+1)+" es el antibacterial")
        else:
            print("El mayor en la sede "+str(i+1)+" son las gafas")
    return


def mostrarPromedioProductos(ma,z,w):
    total = 0
    for j in range(0,w,1):
        print()
        print(productos[j]," ",end="")
        for i in range(0,z,1):
            total+=ma[i][j]
        if(j==0):
            print("El promedio ventas de la mascatrilla es: "+ str(total/5))
        elif(j==1):
            print("El promedio ventas de los guantes es: "+ str(total/5))
        elif(j==2):
            print("El promedio ventas del alcohol es: "+ str(total/5))
        elif(j==3):
            print("El promedio ventas del antibacterial: "+ str(total/5))
        else:
            print("El promedio ventas de las gafas es: "+ str(total/5))
        total=0
    return

def mostrarPromedioSedes(ma, z, w):
    total = 0
    for i in range(0,z,1):
        print()
        print(sedes[i]," ",end="")
        for j in range(0,w,1):
            total+=ma[i][j]
        print("El promedio de las sede "+str(i+1)+" es: "+ str(total/5))

def main():
    inicializarMatriz()
    llenarMatriz(matriz,m,n)
    c=str(input("Presione enter para ver los datos...: "))
    mostrar(matriz,m,n) 
    print()
    c=str(input("Presione enter para ver el total de ingresos por ventas...: "))
    mostrarTotalVentas(matriz,m,n)
    print()
    c=str(input("Presione enter para ver el producto que más ventas tiene por cada sede...: "))
    mostrarMayor(matriz,m,n)
    c=str(input("Presione enter para ver el promedio de ventas por productos...: "))
    mostrarPromedioProductos(matriz, m, n)
    c=str(input("Presione enter para ver el promedio de ventas por cada sede...: "))
    mostrarPromedioSedes(matriz, m, n)
    c=str(input("Presione enter para ver cuantas sedes tiene un promedio de ventas mayor al de la tienda...: "))
    print("Promedio de ventas de la tienda: "+str(promedioTienda()))
    cant = compararPromedios(matriz,m,n)
    print("La cantidad de sedes que cumplen esto son: "+str(cant))
    print()
main()
