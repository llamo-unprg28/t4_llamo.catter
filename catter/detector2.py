#DETECTAR SI ES UNA MALA VENTA  EL TOTAL DE LIBROS VENDIDOS
#DECLARACION
libro_de_auditoria_tributaria=0
libro_manual_del_contador=0
compendio_laboral=0
total=0
#INPUT
libro_de_auditoria_tributaria=int(input("ingrese libro de auditoria tributaria:"))
libro_manual_del_contador=int(input("ingrese libro manual del contador:"))
compendio_laboral=int(input("ingrese compendio laboral:"))
#PROCESSING
total=(libro_de_auditoria_tributaria+libro_manual_del_contador+compendio_laboral)

# DETECTOR
# sera una mala venta neta si el total <4000
mala_venta=(total<4000)

#OUTPUT
print("#########################")
print("#   TOTAL DE LIBROS VENDIDOS   #")
print("#########################")
print("# libro de auditoria tributaria: ",libro_de_auditoria_tributaria,"   #"  )
print("# libro manual del contador: ",libro_manual_del_contador,"   #")
print("# compendio laboral: ",compendio_laboral,"   #")
print("###########################################")
print("# total:s/. ",total,"      #")
print("# mala venta: ",mala_venta,"      #")
print("#####################################################################")
