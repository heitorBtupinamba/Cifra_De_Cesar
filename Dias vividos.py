print(" PROGRAMA CÁLCULO IDADE DE UMA PESSOA EM DIAS")
print()

anos=int(input(" Digite quantos anos você tem: "))
print()

meses=int(input(" Digite quantos meses adicionais você tem além dos anos: "))
print()

dias=int(input(" Digite quantos dias adicionais você tem além dos meses: "))
print()


anostransformados= anos * 365

mesestransformados= meses * 30

diasvividos= anostransformados + mesestransformados + dias

print(f" Você viveu um total de: {diasvividos} dias.")