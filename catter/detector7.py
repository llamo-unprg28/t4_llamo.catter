#DETECTAR SI EL RESULATDO AL DIVIDIR CHROME Y FIREFOX SON MAS USADOS EN OCEANIA
chrome=0.0
firefox=0.0
total=0.0
#INPUT
chrome=float(input("ingrese chrome:"))
firefox=float(input("ingrese firefox:"))
#PROCESSING
total=(chrome+firefox)/2

# DETECTOR
# sera mas usados los navegadores si al dividir el resultado es >6
mas_usados=(total>6)

#OUTPUT
print("##########################################################")
print("# SUMA DE LOS QUE USAN CHROME Y FIREFOX EN OCEANIA  #")
print("#####################################################################")
print("# chrome: ", chrome,"       #")
print("# firefox: ", firefox,"       #"     )
print("#####################################################################")
print("# total: % ",total,"      #")
print("# mas usados:  ",mas_usados,"      #")
print("#####################################################################")
