# Calculadora de Consumo Elétrico Inteligente

print(" Calculadora de Consumo Elétrico ")

#Entrada
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário (horas): "))

#Processamento
consumo_mensal = (potencia * horas_dia * 30) / 1000
custo_estimado = (consumo_mensal * 0.75)

# Saída
print("\n===== RESULTADO =====")
print(f"Aparelho: {aparelho}")
print(f"Potência: {potencia:.0f} W")
print(f"Uso diário: {horas_dia:.1f} horas")
print(f"Consumo mensal estimado: {consumo_mensal:.2f} kWh")
print(f"Custo estimado R$: {custo_estimado:.2f}")