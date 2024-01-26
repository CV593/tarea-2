#CAPITALIZAR TEXTO
tx = "hoLa Mundo"
rs = tx.capitalize()
print(rs)
#METODO BUSCAR
tx = "Hola Mundo"
rs = tx.find("undo")  # cuantos caracteres hay hasta encontrar la palabra "undo"
print(rs)
#METODO CENTER  (centra el texto en un conjunto de caracteres)
tx = "Hola Mundo"
rs1 = tx.center(20)
print(rs1)
#METODO ISALFNUM  (dice si es un tipo de dato alfanumerico)
tx = "125479*"
rs1 = tx.isalnum() #Avienta True o False
print("Hay alfanumericos?" ,rs1)
#METODO ISDIGIT (dice si es un numero)
tx = "254874"
rs1 = tx.isdigit() #Avienta True o False
print("Hay numeros?" ,rs1)
#METODO ISLOWER  (dice si todos los caracteres de la cadena estan en minuscula)
tx = "python es genial"
rs1 = tx.islower() #Avienta True o False
print("Hay minusculas?" ,  rs1)
#METODO ISSPACE()  (dice si hay espacio dentro de la cadena)
tx = "      "
rs1 = tx.isspace() #Avienta True o False
print("Hay espacios?" , rs1)
# METODO ISALPHA()
tx = "setenta 70 "
rs1 = tx.isalpha() #Avienta True o False si solo contiene letras
print("Hay texto?" ,rs1)
# METODO replace()
tx = "Hola Este es un programa en pyton"
rs1 = tx.replace(" ","**") #remplazara espacio por **
print(rs1)
# METODO lstrip()
tx = "      Hola hay 5 espacios"
rs1 = tx.lstrip() #Avienta la cadena con los blancos iniciales omitidos
print(rs1)
# METODO rstrip()
tx = "ESTO ES UNA CADENA CON MUCHOS ESPACIOS    "
rs1 = tx.rstrip() +" Metodo rstrip"#Avienta la cadena con los blancos finales omitidos
print(rs1)
# METODO split()
tx = "Bienvenido de nuevo usuario"
rs1 = tx.split('s') #omite la letra s y la cambia por un espacio con ' , '
print(rs1)
# METODO isupper()
tx = "ESTO ES VERDADERO"
rs1 = tx.isupper() #Avienta True o False
print("Hay mayusculas?" ,rs1)

