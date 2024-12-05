print(" PROGRAMA CONSUMO MÉDIO DE UM AUTOMÓVEL")
print()

totalcombustivel=float(input(" Digite a quantidade total de combustível gasto em litros: "))
print()


totaldistancia=float(input(" Digite a distância total percorrida em km: "))
print()

consumomedio= totalcombustivel / totaldistancia

print(f" O consumo médio de combustível deste automóvel é de {consumomedio:.2f} litros.")