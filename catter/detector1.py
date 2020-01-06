#DETECTAR LAS BUENAS VENTAS  EL TOTAL DEL IMPORTE
#DECLARACION

libro_de_auditoria_tributaria=0.0
libro_manual_del_contador=0.0
compendio_laboral=0.0
total=0.0

#INPUT
libro_de_auditoria_tributaria=int(input("ingrese libro de auditoria tributaria:"))
libro_manual_del_contador=int(input("ingrese libro manual del contador:"))
compendio_laboral=int(input("ingrese compendio laboral:"))

#PROCESSING
total=(libro_de_auditoria_tributaria+libro_manual_del_contador+compendio_laboral)

# DETECTOR
# sera una buena venta neta si el total >40000
buena_venta=(total>4000)

#OUTPUT
print("#########################")
print("#  TOTAL DEL IMPORTE   #")
print("#########################")
print("# libro de auditoria tributaria: ",libro_de_auditoria_tributaria,"   #"  )
print("# libro manual del contador: ",libro_manual_del_contador,"   #")
print("# compendio laboral: ",compendio_laboral,"   #")
print("###########################################")
print("# total:s/. ",total,"      #")
print("# buena venta: ",buena_venta,"      #")
print("#####################################################################")
