def maior(* list):
    m = 0
    print("=-"*30)
    for c in list:
        print(f"{c} ", end="")
    print(f"Foram informados {len(list)} valores ao todo.")
    for c in range(0, len(list)):
        if c == 0 or list[c] > m:
            m = list[c]
    if len(list) == 0:
        m = "nenhum"
    print(f"O maior valor informado foi {m}.")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

