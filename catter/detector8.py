#DETECTAR SI SAMSUNG INTENET ES MAS USADO QUE INTERNET EXPLORE EN AFRICA
samsung_internet=0.0
internet_explore=0.0
total=0.0
#INPUT
samsung_internet=float(input("samsung_internet:"))
internet_explore=float(input("internet_explore:"))
#PROCESSING
total=(samsung_internet-internet_explore)

# DETECTOR
# sera mas usado el navegador samsung internet >6
samsung_internet_mas_usado=(total>6)

#OUTPUT
print("############################################################################")
print("# SUMA DE LOS QUE USAN SAMSUNG INTERNET E INTERNET EXPLORE EN AFRICA  #")
print("#####################################################################")
print("# samsung_internet: ", samsung_internet,"       #")
print("# internet_explor: ",internet_explore,"       #"     )
print("#####################################################################")
print("# total: % ",total,"      #")
print("# samsung internet mas usado:  ",samsung_internet_mas_usado,"      #")
print("#####################################################################")
