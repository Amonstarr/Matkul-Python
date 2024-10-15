kalimat = input("Kalimat yang ingin dicek: ")

vokal = "aiueoAIUEO"

jumlah = 0

for huruf in kalimat:
    if huruf in vokal:
        jumlah += 1 

print(f"Jumlah huruf vokal pada kalimat \"{kalimat}\" adalah {jumlah}")
