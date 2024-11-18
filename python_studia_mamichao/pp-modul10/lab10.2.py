#Napisz program, który zasymuluje 16 rzutów kostką do gry a następnie
#• zestaw wylosowanych wyników,
#• wyrzucaną wartość za 8 razem,
#• liczbę wyrzuconych szóstek,
#• maksymalną liczbę wyrzuconych tych samych wartości pod rząd


import random

DICE_ROLLS_TOTAL = 16
rolls = []

for i in range(DICE_ROLLS_TOTAL):
    rolls.append(random.randint(1, 6))

print("Zbiór wyników po", DICE_ROLLS_TOTAL, "rzutach kostki do gry to: ", rolls)

print()

print("Za ósmym razem wyrzucono wartoś: ", str(rolls[8 - 1]) + ".")

sixes_total = 0
for roll in rolls:
    if roll == 6:
        sixes_total += 1
print()
print("Wyrzuono", sixes_total, " razy szóstke.")

in_row_value_tmp = rolls[0]
in_row_total_tmp = 0
in_row_total = 0
in_row_value = 0

for roll in rolls:
    if roll == in_row_value_tmp:
        in_row_total_tmp +=1
    else:
        in_row_value_tmp = roll
        in_row_total_tmp = 1
    if in_row_total_tmp > in_row_total:
        in_row_total = in_row_total_tmp
        in_row_value = in_row_value_tmp
print()
print("Pod rząd wyrzucono ", in_row_total, " razy wartość ", str(in_row_value) + ".")