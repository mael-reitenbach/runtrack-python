capital = 5000
rendement = 2

print(f"Gain annuel : {capital*rendement/100}")

capital += 5000 + capital*rendement/100
rendement += 2

print(f"Gain annuel : {capital*rendement/100}")

capital = capital - (capital/10) + capital*rendement/100
rendement -= 1

print(f"Gain annuel : {capital*rendement/100}")