#DETECTAR SI EL NAVEGADOR CHROME ES MAS USADO EN AMERICA DEL NORTE
chrome=0.0
firefox=0.0
total=0.0
#INPUT
chrome=float(input("ingrese chrome:"))
firefox=float(input("ingrese firefox:"))
#PROCESSING
total=(chrome)

# DETECTOR
# sera mas usado el navegador chrome si el porcentaje es >4.5
mas_usado_chrome=(total>4.5)

#OUTPUT
print("##########################################################")
print("# SUMA DE LOS QUE USAN CHROME Y FIREFOX EN AMERICA DEL NORTE  #")
print("#####################################################################")
print("# chrome: ", chrome,"       #")
print("# firefox: ", firefox,"       #"     )
print("#####################################################################")
print("# total: % ",total,"      #")
print("# mas usado chrome:  ",mas_usado_chrome,"      #")
print("#####################################################################")
