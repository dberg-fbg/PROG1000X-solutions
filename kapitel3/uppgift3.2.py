pris_arskort = int(input("Vad kostar ett årskort?: "))
pris_enkelbiljett = int(input("Vad kostar en enkelbiljett?: "))
antal_gympass = int(input("Hur många gånger kommer du att gymma i år?: "))

if pris_enkelbiljett * antal_gympass > pris_arskort:
    print("Det lönar sig att köpa ett årskort")
else:
    print("Det lönar sig inte att köpa ett årskort")



