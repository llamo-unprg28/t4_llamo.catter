#DETECTAR SI LA SUMA DE LOS NAVEGADOREs QUE USAN SAMSUNG INTERNET E INTERNET EXPLORE EN ASIA SON MALOS
samsung_internet=0.0
internet_explore=0.0
total=0.0
#INPUT
samsung_internet=3.16
internet_explore=0.0
#PROCESSING
total=(samsung_internet+internet_explore)

# DETECTOR
# sera malos navegadores si la suma  no es >10.5
malos_navegadores=(total<150000)

#OUTPUT
print("############################################################################")
print("# SUMA DE LOS QUE USAN SAMSUNG INTERNET E INTERNET EXPLORE EN AFRICA  #")
print("#####################################################################")
print("# samsung_internet: ", samsung_internet,"       #")
print("# internet_explor: ",internet_explore,"       #"     )
print("#####################################################################")
print("# total: % ",total,"      #")
print("# malos navegadores:  ",malos_navegadores,"      #")
print("#####################################################################")
