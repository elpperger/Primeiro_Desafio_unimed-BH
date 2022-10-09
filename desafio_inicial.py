distancia = int()
diametro_sauron = int()
diametro_saruman = int()
icm = float()

print("Cálculo da Interferência de Comunicação Mágica (ICM)")
print()

distancia = int(input("Informe a distância entre os dois Palantir's: "))
if distancia > 0 and distancia < 10000:
    print("Distância aceita para cálculo!")
    print()
else:
    print("Digite uma distância que seja maior que 0 e menor que 10000")
    distancia = int(input("Informe a distância entre os dois Palantir's: "))
    print()

diametro_sauron = int(input("Digite o diametro do Palantir de Sauron: "))
if diametro_sauron > 0 and diametro_sauron < 100:
    print("Diâmetro aceito para cálculo!")
    print()
else:
    print("Digite um diâmetro que seja maior que 0 e menor que 100")
    diametro_sauron = int(input("Digite o diametro do Palantir de Sauron: "))
    print()

diametro_saruman = int(input("Digite o diametro do Palantir de Saruman: "))
if diametro_saruman > 0 and diametro_saruman < 100:
    print("Diâmetro aceito para cálculo")
    print()
else:
    print("Digite um diâmetro que seja maior que 0 e menor que 100")
    diametro_saruman = int(input("Digite o diametro do Palantir de Saruman: "))
    print()

icm = distancia/(diametro_sauron + diametro_saruman)
print(f"O valor da ICM é de {icm:,.2f}.")
