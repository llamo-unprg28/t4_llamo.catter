#DETECTAR LA SUMA DE LOS QUE USAN CHROME Y FIREFOX EN AFRICA
#DECLARAR
chrome=0.0
firefox=0.0
total=0.0
#INPUT
chrome=float(input("ingrese chrome:"))
firefox=float(input("ingrese firefox:"))
#PROCESSING
total=(chrome+firefox)

# DETECTOR
# seran buenos navegadores si el porcentaje es >5
buenos_navegadores=(total>5)

#OUTPUT
print("##########################################################")
print("# SUMA DE LOS QUE USAN CHROME Y FIREFOX EN AFRICA  #")
print("#####################################################################")
print("# chrome: ", chrome,"       #")
print("# firefox: ", firefox,"       #"     )
print("#####################################################################")
print("# total: % ",total,"      #")
print("# buenos navegadores:  ",buenos_navegadores,"      #")
print("#####################################################################")

