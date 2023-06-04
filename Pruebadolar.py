Conversion = input("¿Quieres convertir dólares a pesos? Responde 1 si quieres convertir de pesos a dólares o responde 2 si quieres convertir dólares a pesos: ")
if Conversion == "1":
 Dolar = 17.56
 PesoMX = (int(input("Ingresa cantidad en pesos: ")))
 EquivalenciaPaD = PesoMX / Dolar
 print("Esto equivale a:", round(EquivalenciaPaD, 2) , "dólares")
elif Conversion == "2":
 PesoMX = 0.057
 EquivalenciaDaP = Dolar * PesoMX
 print("Esto equivale a:", round(EquivalenciaDaP, 2) , "pesos mexicanos")