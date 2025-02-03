item1 = input().split(" ")
item2 = input().split(" ")

id1 = int(item1[0])
amount1 = int(item1[1])
unityPrice1 = float(item1[2])

id2 = int(item2[0])
amount2 = int(item2[1])
unityPrice2 = float(item2[2])

total = (amount1 * unityPrice1) + (amount2 * unityPrice2)

print(f"VALOR A PAGAR: R$ {total:.2f}")