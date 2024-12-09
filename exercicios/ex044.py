p = float(input("Preço Total: R$"))
m = "Formas de Pagamento\n"
m = m + "1. À Vista, em Sinheiro ou Cheque\n"
m = m + "2. À Vista no Catão\n"
m = m + "3. Em 2x no Cartão\n"
m = m + "4. Em 3x ou Mais vezes no Cartão"
print(m)
m = input("Qual é a sua opção? ")
m = m.strip()
if m == "1":
    print("Sua compra ficou {}".format(p*0.9))
elif m == "2":
    print("Sua compra ficou {}".format(p*0.95))
elif m == "3":
    print("Você vai pagar duas parcelas de {}\nÉ no total ficará {}".format(p/2,p))
elif m == "4":
    x = int(input("Em quantas parcelas você vai pagar? "))
    print("Você vai pagar {}} parcelas de {}\nÉ no total ficará {}".format(x,p/x,p*1.2))
else:
    print("Opção Invalida")
