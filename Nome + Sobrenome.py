import sys
sys.stdin.reconfigure(encoding='utf-8')

print("PROGRAMA NOME E SOBRENOME")
print()

nome=str(input("Digite seu primeiro nome: "))
print()

sobrenome=str(input("Digite seu sobrenome: "))
print()

nomecompleto= nome + " " + sobrenome

print("Seu nome completo é: ", nomecompleto + ".")