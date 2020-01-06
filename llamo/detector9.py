# DETETCATR SI ES UNA BUENA SUMA  EL PRODUCTO DEL TOTAL ACTIVO CON EL TOTAL PASIVO AÑO 2007
total_activo_2007=0
total_pasivo_2007=0
total=0
#INPUT
total_activo_2007=int(input("ingrese ventas netas total activo 2007:"))
total_pasivo_2007=int(input("ingrese ventas netas total activo 2007:"))
#PROCESSING
total=(total_activo_2007*total_pasivo_2007)

# DETECTOR
# sera bueno si la suma del producto con total pasivo >30000
buena_suma=(total>30000)

#OUTPUT
print("############################################################################")
print("# PRODUCTO DEL TOTAL ACTIVO CON EL TOTAL PASIVO AÑO 2007 #")
print("#####################################################################")
print("# total activo 2007: ", total_activo_2007,"     #")
print("# total pasivo 2007: ", total_pasivo_2007,"      #")
print("#####################################################################")
print("# total: ", total,"    #")
print("# buena suma: ", buena_suma,"     #")
print("#####################################################################")
