lista_p = []
for i in range(0, 4):
    p = str(input("Produto:"))
    lista_p.append(p)

lista_v = []
for i in range(0, 4):
    v = float(input("Valor: "))
    lista_v.append(v)

valor_total = int(sum(lista_v))
cupom = input("Digite cupom: ")
if (cupom=="hipodromo15"):
    valor_total *= 0.85
    print("Cupom aplicado")


print(lista_p)
print(lista_v)
print("Saiu do seu bolso:", valor_total)