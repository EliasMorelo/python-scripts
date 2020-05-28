
def main():
    import random 
    m=int(input("Ingrese la cantidad de n...: "))
    n=int(input("Ingrese la cantidad de m...: "))
    a=[]
    nom=["NULL"]*m
    
    for i in range(0, m):
        a.append([999]*n)
    
    def llenar(ma,z,w):
        for i in range(0,z,1):
            nom[i]=str(input("Ingrese nombre del vendedor y presione enter: "))
            for j in range(0,w,1):
                comision = (random.random())*2000000
                ma[i][j] = round (comision,2)
        return

    def mostrar(ma,z,w):
        for i in range(0,z,1):
            print()
            print(nom[i]," ",end="") 
            for j in range(0,w,1):
                print(ma[i][j],'\t',end="")
        return
    
    totales = [0]*m
    def mostrarTotalVentas(ma,z,w):
        total = 0 
        v = 0
        for i in range(0,z,1):
            print()
            print(nom[i]," ",end="")
            for j in range(0,w,1):
                total+=ma[i][j]
                v = total
            print(total)
            totales[i] = v
        return
    def buscarMayor(t, m):
        posMayor = 0
        mayor = 0
        for i in range(0, m, 1):
            temp = t[i]
            if(temp > mayor):
                posMayor = i
                mayor = temp
        return posMayor

    def mostrarTotalMeses(ma,z,w):
        total = 0 
        for j in range(0,w,1):
            print()
            print("Mes "+str(j)+" ",end="")
            for i in range(0,z,1):
                total+=ma[i][j]
            print(total)
        return
     
    print ("INICIALIZANDO")
    mostrar(a,m,n) 
    print()
    c=str(input("Presione enter para ingresar los datos...........: "))
    llenar(a,m,n)
    c=str(input("Presione enter para ver los datos...: "))
    mostrar(a,m,n) 
    print()
    c=str(input("Presione enter para ver el total de cada vendedor...: "))
    mostrarTotalVentas(a,m,n)
    print()
    c=str(input("Presione enter para ver el vendedor con mayor comision...: "))
    mayor = buscarMayor(totales, m);
    print("La mejores comisiones las obtuvo el vendedor: "+nom[mayor]+ " con $"+str(totales[mayor]))
    print()
    c=str(input("Presione enter para ver el total de los meses...: "))
    mostrarTotalMeses(a,m,n)
    print()
    print ("Terminamos.........................")
main()
