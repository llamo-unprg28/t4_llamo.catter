#DETECTAR SI SON MALOS LOS NAVEGADORES SI LA SUMA DE LOS QUE USAN CHROME Y FIREFOX EN EUROPA
chrome=0.0
firefox=0.0
total=0.0
#INPUT
chrome=float(input("ingrese chrome:"))
firefox=float(input("ingrese firefox:"))
#PROCESSING
total=(chrome+firefox)

# DETECTOR
# seran malos navegadores si el porcentaje es >3
malos_navegadores=(total>3)

#OUTPUT
print("##########################################################")
print("# SUMA DE LOS QUE USAN CHROME Y FIREFOX EN EUROPA  #")
print("#####################################################################")
print("# chrome: ", chrome,"       #")
print("# firefox: ", firefox,"       #"     )
print("#####################################################################")
print("# total: % ",total,"      #")
print("# malos navegadores:  ",malos_navegadores,"      #")
print("#####################################################################")
