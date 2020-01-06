# DETECTAR SI ES UNA BUENA VENTA LA SUMA DE LAS VENTAS NETAS DEL AÑO 2005 Y 2006
ventas_netas_2005=0
ventas_netas_2006=0
total=0
#INPUT
ventas_netas_2005=int(input("ingrese ventas netas 2005:"))
ventas_netas_2006=int(input("ingrese ventas netas 2006:"))

#PROCESSING
total=(ventas_netas_2005+ventas_netas_2006)

# DETECTOR
# sera una buena venta neta si el total >40000
buena_venta=(total>40000)

#OUTPUT
print("############################################################################")
print("# SUMA DE LAS VENTAS NETAS DEL AÑO 2005 Y 2006 #")
print("#####################################################################")
print("# ventas netas 2005: ",ventas_netas_2005,"   #"  )
print("# ventas netas 2006: ",ventas_netas_2006,"   #")
print("###########################################")
print("# total:s/. ",total,"      #")
print("# buena venta: ",buena_venta,"      #")
print("#####################################################################")
