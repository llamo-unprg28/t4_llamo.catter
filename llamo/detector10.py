# DETECTAR SI ES UNA BUENA SUMA EL PRODUCTO DEL TOTAL ACTIVO CON EL TOTAL PASIVO AÑO 2008
total_activo_2008=0
total_pasivo_2008=0
total=0
#INPUT
total_activo_2008=int(input("ingrese ventas netas total activo 2008:"))
total_pasivo_2008=int(input("ingrese ventas netas total activo 2008:"))
#PROCESSING
total=(total_activo_2008*total_pasivo_2008)

# DETECTOR
# sera bueno si la suma del producto con total pasivo >150000
buena_suma=(total<150000)

#OUTPUT
print("############################################################################")
print("# PRODUCTO DEL TOTAL ACTIVO CON EL TOTAL PASIVO AÑO 2008 #")
print("#####################################################################")
print("# total activo 2008: ", total_activo_2008,"     #")
print("# total pasivo 2008: ", total_pasivo_2008,"    #")
print("#####################################################################")
print("# total: ", total,"    #")
print("# buena suma: ", buena_suma,"     #")
print("#####################################################################")
