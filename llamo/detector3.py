# DETTECTAR SI ES UNA MALA VENTA LA SUMA DE LAS VENTAS NETAS DEL AÑO 2007 Y 2008
ventas_netas_2007=0
ventas_netas_2008=0
total=0
#INPUT
ventas_netas_2007=int(input("ingrese ventas netas 2007:"))
ventas_netas_2008=int(input("ingrese ventas netas 2008:"))

#PROCESSING
total=(ventas_netas_2007+ventas_netas_2008)

# DETECTOR
# sera una mala venta neta si el total >150000
mala_venta_neta=(total<150000)

#OUTPUT
print("############################################################################")
print("# SUMA DE LAS VENTAS NETAS DEL AÑO 2007 Y 2008 #")
print("#####################################################################")
print("# ventas netas 2007: ",ventas_netas_2007,"   #"  )
print("# ventas netas 2008: ",ventas_netas_2008,"   #")
print("###########################################")
print("# total:s/. ",total,"      #")
print("# mala venta neta: ",mala_venta_neta,"      #")
print("#####################################################################")

