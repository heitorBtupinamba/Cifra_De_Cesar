print(" PROGRAMA CÁLCULO DE COMBUSÍVEL")
print()

tempo=int(input(" Digite o tempo total em horas gasto na viagem: "))
print()

velocidademedia=int(input(" Digite o a velocidade média em km/h durante a viagem:  "))
print()

distancia= tempo * velocidademedia

litrosusados= distancia / 12

print(f" A velocidade média durante a viagem foi de: {velocidademedia} km/h.")


if tempo == 1 :
    print(" O tempo gasto foi de: 1 hora.")
else : print(f" O tempo gasto na viagem foi de: {tempo} horas.")


print(f" A distância percorrida na viagem foi de: {distancia} km")

print(f" A quantidade de litros utilizada na viagem foi de: {litrosusados} litros.")
