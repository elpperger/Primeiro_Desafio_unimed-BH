######### Desafio das duas torres - somente cálculo #########

entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

icm = float()

icm = distancia/(diametro1 + diametro2)
print(f"{icm:,.2f}")

######### Desafio do cachorro quente - somente cálculo #########

valores = input().split()

num_med = float()

num_med = int(valores[0]) / int(valores[1])
print(f"{num_med:,.2f}")


######### Desafio do cálculo de viagem - somente cálculo #########

valores = input().split()

quant_litros = float()

# o carro faz 12 Km/L

quant_litros = int(valores[0]) * int(valores[1]) / 12
print(f"{quant_litros: .3f}")
