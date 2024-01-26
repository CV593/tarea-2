def calculo (horas,precio):
    ho= float(horas)
    return ho*precio
h = input("INGRESE LAS HORAS TRABAJADAS: ")
p = float(input("INGRESE EL COSTE POR HORA: "))
print(f"LA PAGA CORRESPONDIENTE ES DE Q. {calculo(h,p)}")