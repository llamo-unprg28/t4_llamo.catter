# DETTECTAR SI ES UNA BUENA UTILIDAD SI EL INCREMENTO DE LA UTILIDAD BRUTA DEL AÑO 2005 Y 2006
utilidad_bruta_2005=0
utilidad_bruta_2006=0
total=0
#INPUT
utilidad_bruta_2005=float(input("ingrese la cantidad de utilidad_bruta_2005:"))
utilidad_bruta_2006=float(input("ingrese la cantidad de utilidad_bruta_2006:"))
#PROCESSING
total=(utilidad_bruta_2006-utilidad_bruta_2005)

# DETECTOR
# seran buena utildad bruta si al restar entre los dos años sea > 20000
buena_utildad=(total>20000)

#OUTPUT
print("############################################################################")
print("# INCREMENTO DE LA UTILIDAD BRUTA DEL AÑO 2005 Y 2006 #")
print("#####################################################################")
print("# utilidad bruta 2005: ", utilidad_bruta_2005,"    # ")
print("# utilidad bruta 2006: ", utilidad_bruta_2006,"     #")
print("#####################################################################")
print("# total: s/. ", total,"       #")
print("# buena_utildad: ", buena_utildad,"       #")
print("#####################################################################")
