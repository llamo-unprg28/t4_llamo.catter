#DETECTAR SI LA SUMA DE AMBOS NAVEGADORES QUE USAN CHROME Y FIREFOX EN ASIA SON BUENOS
chrome=0.0
firefox=0.0
total=0.0
#INPUT
chrome=56.47
firefox=3.25
#PROCESSING
total=(chrome+firefox)

# DETECTOR
# seran buenos navegadores si la suma es  >34.5
buenos_navegadores=(total>34.5)

#OUTPUT
print("############################################################################")
print("# SUMA DE LOS QUE USAN SAMSUNG INTERNET E INTERNET EXPLORE EN AFRICA  #")
print("#####################################################################")
print("# samsung_internet: ", samsung_internet,"       #")
print("# internet_explor: ",internet_explore,"       #"     )
print("#####################################################################")
print("# total: % ",total,"      #")
print("# buenos navegadores:  ",buenos_navegadores,"      #")
print("#####################################################################")
