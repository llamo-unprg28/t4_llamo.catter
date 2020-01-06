# DETECTAR BUENOS NAVEGADORES CON LA SUMA DE LOS QUE USAN EDGE, SAFARI Y OPERA EN AFRICA
edge=0.0
safari=0.0
opera=0.0
#INPUT
edge=float(input("ingrese la cantidad de edge:"))
safari=float(input("ingrese la cantidad de safari:"))
opera=float(input("ingrese la cantidad de opera:"))

#PROCESSING
total=(edge+safari+opera)

# DETECTOR
# seran buenos navegadores cuando el total >5
buenos_navegadores=(total>5)


#OUTPUT
print("############################################################################")
print("# SUMA DE LOS QUE USAN EDGE, SAFARI Y OPERA EN AFRICA #")
print("#####################################################################")
print("# edge: ",edge,"  # ")
print("# safari: ",safari,"  #")
print("# opera: ",opera,"    #")
print("# total: ", total)
print("#####################################################################")
print("# total:% ",total,"   #")
print("# buenos navegadores: ",buenos_navegadores,"   #")
print("####################################################")
