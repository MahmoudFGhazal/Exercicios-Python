def notas(* n, sit=False):
    x = dict()
    x["total"] = len(n)
    x["maior"] = max(n)
    x["menor"] = min(n)
    x["media"] = sum(n)/len(n)
    if sit:
        if x["media"] >= 8:
            x["situação"] = "Otimo"
        elif x["media"] >= 7:
            x["situação"] = "Bom"
        elif x["media"] >= 6:
            x["situação"] = "Razoavel"
        else:
            x["situação"] = "RUIM"
    return x



resp = notas(9, 10, sit=True)
print(resp)
