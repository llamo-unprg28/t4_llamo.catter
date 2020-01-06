# DETECTAR SI ES MALA VENTA LA SUMA DE LOS COSTOS DE VENTA DEL AÑO 2007 HASTA 2009
costos_de_ventas_2007=0
costos_de_ventas_2008=0
costos_de_ventas_2009=0
total=0
#INPUT
costos_de_ventas_2007=int(input("ingrese costos de ventas 2007:"))
costos_de_ventas_2008=int(input("ingrese costos de ventas 2008:"))
costos_de_ventas_2009=int(input("ingrese costos de ventas 2009:"))

#PROCESSING
total=(costos_de_ventas_2007+costos_de_ventas_2008+costos_de_ventas_2009)

# DETECTOR
# sera malas ventas si el total < 800000
malas_ventas=(total<800000)

#OUTPUT
print("############################################################################")
print("# SUMA DE LOS COSTOS DE VENTA DEL AÑO 2007 HASTA 2009 #")
print("#####################################################################")
print("# costos de ventas 2007: ", costos_de_ventas_2007,"      #")
print("# costos de ventas 2008: ", costos_de_ventas_2008,"    #")
print("# costos de ventas 2009: ", costos_de_ventas_2009,"    #")
print("#####################################################################")
print("# total:s/. ", total,"   # ")
print("# malas ventas: ",malas_ventas,"    #")
print("#####################################################################")
