def calcular_previdencia(salario_total):
    faixas_inss = [
        (1412.00, 0.075),
        (2666.68, 0.09),
        (4000.03, 0.12),
        (7786.02, 0.14)
    ]

    desconto_previdencia = 0.0
    limite_anterior = 0.0

    for limite, taxa in faixas_inss:
        if salario_total > limite:
            desconto_previdencia += (limite - limite_anterior) * taxa
            limite_anterior = limite
        else:
            desconto_previdencia += (salario_total - limite_anterior) * taxa
            break

    return min(desconto_previdencia, 7786.02 * 0.14)


def calcular_imposto(salario_total, previdencia):
    base_calculo = salario_total - previdencia - 564.80

    if base_calculo <= 2259.20:
        return 0.0
    elif base_calculo <= 2826.65:
        return base_calculo * 0.075 - 169.44
    elif base_calculo <= 3751.05:
        return base_calculo * 0.15 - 381.44
    elif base_calculo <= 4664.68:
        return base_calculo * 0.225 - 662.77
    else:
        return base_calculo * 0.275 - 896.00


def calcular_liquido(salario_total):
    previdencia = calcular_previdencia(salario_total)
    imposto = calcular_imposto(salario_total, previdencia)
    salario_final = salario_total - previdencia - imposto
    return previdencia, imposto, salario_final


salario_bruto = float(input("Digite o valor do salário: R$ "))
previdencia, imposto_renda, salario_liquido = calcular_liquido(salario_bruto)

print("\nSalário bruto:", salario_bruto)
print("Desconto Previdência:", previdencia)
print("Desconto IR:", imposto_renda)
print("Salário líquido:", salario_liquido)
