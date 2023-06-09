

Conversion = input("Conversor: Responde 1 si quieres convertir de pesos a dólares o responde 2 si quieres convertir dólares a pesos: ")
if Conversion == "1": #PESOS A DÓLARES
 Cambio = 17.56
 PesoMX = (int(input("Ingresa cantidad en pesos: ")))
 EquivalenciaPaD = PesoMX / Cambio
 print("Esto equivale a:", round(EquivalenciaPaD, 2) , "dólares")
elif Conversion == "2": #DÓLARES A PESOS
 Cambio = 17.56
 Dolar = (int(input("Ingresa cantidad en dólares: ")))
 EquivalenciaDaP = Dolar * Cambio
 print("Esto equivale a:", round(EquivalenciaDaP, 2) , "pesos mexicanos")
 
 
 
 #pesos a dolares, a euros, yanes, dolares a euros, dolares a yuanes y euros a yuanes
 
 print ("Nota de venta" .center(60,"-"))