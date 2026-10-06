
pris_inklusive_moms = float(input("Vad kostar varan? (inklusive moms): "))
moms_sats = float(input("Ange momssatsen i procent: "))


pris_exklusive_moms = pris_inklusive_moms / (1 + moms_sats /  100)
moms = pris_inklusive_moms - pris_exklusive_moms

print(f"varan kostar {pris_exklusive_moms: .02f} kr med en moms på {moms: .02f}")

