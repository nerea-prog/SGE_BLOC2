import create_registre as cr
import read_registre as rr

cr.create_reg()

#Llamada read_registre
results = rr.read_reg()
print(type(results))
