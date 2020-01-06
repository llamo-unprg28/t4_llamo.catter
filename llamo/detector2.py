# DETECTAR SI ES UNA BUENA VENTA LA DIVISION DEL PRIMER PRODUCTO Y EL TOTAL DEL IMPORTE
#DECLARACION

libro_de_auditoria_tributaria=0.0
total_del_importe=0.0
total=0.0

#INPUT
libro_de_auditoria_tributaria=float(input("ingrese la cantidad de auditoria tributaria :"))
total_del_importe=float(input("ingrese la cantidad de total del importe:"))

#PROCESSING
total=(libro_de_auditoria_tributaria/total_del_importe)

# DETECTOR
# sera una buena venta si al dividir los libros vendidos de auditoria tributaria entre el total del importe sea > 0.5
buena_venta =(total>5000)

#OUTPUT
print("###########################################################")
print("#  DIVISION DEL PRIMER PRODUCTO Y EL TOTAL DEL IMPORTE  #")
print("#########################")
print("# libro de auditoria tributaria: ", libro_de_auditoria_tributaria,"   # ")
print("# total del importe: ", total_del_importe,"      #")
print("#########################################################")
print("# total: ",total,"    # ")
print("# buena venta : ",buena_venta ,"    # ")
print("#########################################################")
