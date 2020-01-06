#DETECTAR EL NAVEGADOR SI ES MAS USADO AMERICA DEL SUR
chrome=0.0
firefox=0.0
total=0.0
#INPUT

firefox=float(input("ingrese firefox:"))
#PROCESSING
total=(chrome+firefox)

# DETECTOR
# sera mas usado el navegador firefox si el total es >7
mas_usado_firefox=(total>7)

#OUTPUT
print("##########################################################")
print("# SUMA DE LOS QUE USAN CHROME Y FIREFOX EN AMERICA DEL SUR  #")
print("#####################################################################")
print("# firefox: ", firefox,"       #"     )
print("#####################################################################")
print("# total: % ",total,"      #")
print("# mas usado firefox:  ",mas_usado_firefox,"      #")
print("#####################################################################")
