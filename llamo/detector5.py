# DETECTAR EL DESCUENTO DE LA SUMA DE LOS DOS PRIMEROS PRODUCTOS VENDIDOS
#DECLARACION

libro_de_auditoria_tributaria=0.0
libro_manual_del_contador=0.0
total=0.0

#INPUT
libro_de_auditoria_tributaria=float(input("ingrese la cantidad de libro_de_auditoria_tributaria:"))
libro_manual_del_contador=float(input("ingrese la cantidad de libro_manual_del_contador:"))

#PROCESSING
total=(libro_de_auditoria_tributaria+libro_manual_del_contador)

# DETECTOR
#se hara un descuento del 10% al comprar mas de tres libros y el total sea mayor a>1200
descuento=(total>1200)

#OUTPUT
print("#####################################################")
print("#  SUMA DE LOS DOS PRIMEROS PRODUCTOS VENDIDOS  #")
print("#########################")
print("# libro de auditoria tributaria: ", libro_de_auditoria_tributaria,"   #")
print("# libro manual del contador: ", libro_manual_del_contador,"    #")
print("################################################################")
print("# total: ", total,"     #")
print("# descuento del 10%: ",descuento,"     #")
print("#########################")
