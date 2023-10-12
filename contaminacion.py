
def create():

    n=int(input("Digite el número de municipios"))

    for x in range (n):
        municipios=[]
        residuos=[]
        afectacion=[]

        olores=[]
        asentamientos=[]
        hidricas=[]

       
        
        for y in range (n):
            nombre=input("Digite el nombre del municipio ")
            residuo=int(input("Cantidad de residuos por día del municipio "))
            
            municipios.append(nombre)
            residuos.append(residuo)
            
            print("Respecto a los problemas ambientales digite el porcentaje que considere para cada uno. Debe sumar 100 porciento el total")
            olor=int(input("Cantidad de % por olores "))
            olores.append(olor)
            asent=int(input("Cantidad de % por asentamientos ilegales "))
            asentamientos.append(asent)
            hid=int(input("Cantidad de % por contaminación hidrica "))
            hidricas.append(hid)

            if (olor+asent+hid)!=100:
                print("No suma 100%, repita la operación")
                hidricas.clear()
                olores.clear()
                hidricas.clear()
                break


        return municipios, residuos, olores,asentamientos,hidricas

def more_tons():
    max_init=0
    for x in range(len(tons)):
            
            if tons[x]>max_init:               
                max_position=x
                max_init=tons[x]
                max=name[max_position]
    return print ("El municipio que más genera residuos es",max,"con", max_init, "toneladas/día" )

def min_tons():
    min_init=99
    for x in range(len(tons)):
            
            if tons[x]<min_init:               
                min_position=x
                min_init=tons[x]
                min=name[min_position]
        
    return print ("El municipio que menos residuos es",min,"con", min_init, "toneladas/día" )

def prom_tons():
    sum=0
    prom=0

    for x in range(len(tons)):
          sum=sum+ tons[x]
    
    prom= sum/len(tons)

    return print ("El promedio de toneladas/dia es",prom )

def prom_tons_month():
    sum=0
    prom=0

    for x in range(len(tons)):
          prom_month=(tons[x]*30)/30
          
          sum=sum+ prom_month

    
    prom= sum/len(tons)

    return print ("El promedio de toneladas/mes es",prom )


def problem():
    sum_olores=0
    sum_asen=0
    sum_hc=0
     
    for x in range (len(problem_olores)):
          sum_olores=sum_olores+problem_olores[x]
     
    for y in range (len(problem_asentamientos)):
          sum_asen=sum_asen+problem_asentamientos[x]
    
    for z in range (len(problem_hidricas)):
          sum_hc=sum_hc+problem_hidricas[x]
    
    if sum_olores>=sum_asen and sum_olores>=sum_hc:
         print("El mayor problema son los olores")
    elif sum_asen>=sum_olores and sum_asen>=sum_hc:
         print("El mayor problema son los asentamientos ilegales")
    elif sum_hc>=sum_olores and sum_hc>=sum_asen:
         print("El mayor problema son los hidricps")
    
    return sum_olores, sum_hc, sum_asen

def problem_min():
    sum_olores=0
    sum_asen=0
    sum_hc=0
     
    for x in range (len(problem_olores)):
          sum_olores=sum_olores+problem_olores[x]
     
    for y in range (len(problem_asentamientos)):
          sum_asen=sum_asen+problem_asentamientos[x]
    
    for z in range (len(problem_hidricas)):
          sum_hc=sum_hc+problem_hidricas[x]
    
    if sum_olores<=sum_asen and sum_olores<=sum_hc:
         print("El menor problema son los olores")
    elif sum_asen<=sum_olores and sum_asen<=sum_hc:
         print("Elm enor problema son los asentamientos ilegales")
    elif sum_hc<=sum_olores and sum_hc<=sum_asen:
         print("El menor problema son los hidricos")
    
    return sum_olores, sum_hc, sum_asen

def prom_olores():
    
    sum=0
    prom=0

    for x in range(len(problem_olores)):
          sum=sum+ problem_olores[x]
    
    prom= sum/len(problem_olores)

    return print ("El promedio de olores es ",prom )

def prom_asentamientos():
    
    sum=0
    prom=0

    for x in range(len(problem_asentamientos)):
          sum=sum+ problem_asentamientos[x]
    
    prom= sum/len(problem_asentamientos)

    return print ("El promedio de asentamientos ilegales es ",prom )

def prom_hidricas():
    sum=0
    prom=0

    for x in range(len(problem_hidricas)):
          sum=sum+ problem_hidricas[x]
    
    prom= sum/len(problem_hidricas)

    return print ("El promedio de corrientes hidricas es ",prom )

option= -1

while option!=0:
    print("--------MENU------")
    print("\n1. Ingresar datos de los municipios")
    print("2. Municipio que más toneladas al día genera")
    print("3. Municipio que menos toneladas al día genera")
    print("4. Promedio toneladas día")
    print("5. Promedio toneladas mes")
    print("6. Mayor problema ambiental")
    print("7. Menor problema ambiental")
    print("8. Promedio problema de olores")
    print("9. Promedio problema de asentamientos")
    print("10. Promedio problema de corrientes hidricas")
    print("0. Terminar")
   
    option= int(input("\nDigite la opción deseada:"))

    if option==1:
        compl_list= create()

        name=compl_list[0]
        tons= compl_list[1] 
        
        problem_olores=compl_list[2]
        problem_asentamientos=compl_list[3]
        problem_hidricas=compl_list[4]


    if option==2:
        more_tons()
    if option==3:
        min_tons()
    if option==4:
        prom_tons()
    if option==5:
        prom_tons_month()
    if option==6:
        problem()
    if option==7:
        problem_min()
    if option==8:
        prom_olores()
    if option==9:
        prom_asentamientos()
    if option==10:
        prom_hidricas()
    
