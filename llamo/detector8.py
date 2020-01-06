# DETECTAR SI ES UNA BUENA SUMA  EL PRODUCTO DEL TOTAL ACTIVO CON EL TOTAL PASIVO AÑO 2006
total_activo_2006=0
total_pasivo_2006=0
total=0
#INPUT
total_activo_2006=int(input("ingrese ventas netas total activo 2006:"))
total_pasivo_2006=int(input("ingrese ventas netas total activo 2006:"))
#PROCESSING
total=(total_activo_2006*total_pasivo_2006)

# DETECTOR
# sera bueno si la suma del producto con total pasivo >10000
buena_suma=(total<10000)

#OUTPUT
print("############################################################################")
print("# PRODUCTO DEL TOTAL ACTIVO CON EL TOTAL PASIVO AÑO 2006 #")
print("#####################################################################")
print("# total activo 2008: ", total_activo_2006,"     #")
print("# total pasivo 2008: ", total_pasivo_2006,"    #")
print("#####################################################################")
print("# total: ", total,"    #")
print("# buena suma: ", buena_suma,"     #")
print("#####################################################################")
