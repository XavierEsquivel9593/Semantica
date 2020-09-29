#Esquivel Macías Erick Xavier 16590461 
#Gómez Olvera Jacob Misael 16590474 
TIENE = [
    ("Tortuga","Garras"),
    ("Tortuga","Proteccion Queratina (plumas o escamas)"), 
    ("Gallo","Garras"),
    ("Gallo","Proteccion Wueratina (plumas o escamas)"), 
    ("Cocodrilo","Garras"),
    ("Cocodrilo","Proteccion queratina (plumas o escamas)"), 
    ("Iguana","Garras"),
    ("Iguana","Proteccion queratina (plumas o escamas)"), 
    ("Gato","Garras"),
    ("Gato","Pelo"),
    ("Gato","GlandulasM"),
    ("Oso","Garras"),
    ("Oso","Pelo"),
    ("Oso","GlandulasM"),
    ("Ballena","Proteccion queratina (plumas o escamas)"), 
    ("Ballena","GlandulasM"),
    ("Delfin","GlandulasM") ]

VIVE = [ 
    ("Tortuga","Agua"),
    ("Tortuga","Tierra"), 
    ("Gallo","Tierra"), 
    ("Cocodrilo","Agua"), 
    ("Cocodrilo","Tierra"), 
    ("Iguana","Tierra"), 
    ("Gato","Tierra"), 
    ("Oso","Tierra"), 
    ("Ballena","Agua"), 
    ("Delfin","Agua")
]
    
ES = [
    ("Delfin","Viviparo"), 
    ("Ballena","Viviparo"), 
    ("Oso","Viviparo"), 
    ("Gato","Viviparo"), 
    ("Tortuga","Oviparo"), 
    ("Iguana","Oviparo"), 
    ("Cocodrilo","Oviparo"), 
    ("Gallo","Oviparo"), 
    ("Tortuga","Oviparo"), 
    ("Viviparo","Mammalia"),
    ("Oviparo","Sauropsidos"), 
    ("Sauropsidos","Tetrapodos"), 
    ("Mammalia","Tetrapodos"), 
    ("Tetrapodos","Vertebrados")
]

def tiene(A,B,Conocimiento):
    o=0
    while o < len(Conocimiento):
        if Conocimiento[o][0] == A:
            if Conocimiento[o][1] == B:
                return True
            o=o+1
        return False

def vive(A,B,Conocimiento):
    o=0
    while o < len(Conocimiento):
        if Conocimiento[o][0] == A:
            if Conocimiento[o][1] == B:
                return True
        o=o+1
    return False

def es(A,B,Conocimiento):
    o=0
    while o < len(Conocimiento):
        if Conocimiento[o][0] == A:
            if Conocimiento[o][1] == B:
                return True
            A = Conocimiento[o][1]
        o=o+1
    return False

print("")
print("El Gallo TIENE GlandulasM ",tiene("Gallo","GlandulasM",TIENE))
print("El Cocodrilo TIENE Pelo ",tiene("Cocodrilo","Pelo",TIENE))
print("El Delfin TIENE Proteccion queratina (plumas o escamas) ",tiene("Delfin","Proteccion queratina (plumas o escamas)",TIENE))

print("")
print("El Cocodrilo VIVE en Tierra ",vive("Cocodrilo","Tierra",VIVE))
print("El Oso VIVE en Agua ",vive("Oso","Agua",VIVE))
print("La Ballena VIVE en Tierra ",vive("Ballena","Tierra",VIVE))

print("")
print("El Cocodrilo ES Oviparo ",es("Cocodrilo","Oviparo",ES))
print("El Oso ES Sauropsidos ",es("Oso","Sauropsidos",ES))
print("El Oso ES Mammalia ",es("Oso","Mammalia",ES)) 
