def mcd(num1, num2):
    resto = max(num1, num2) % min(num1, num2)
    if resto == 0:
        return min(num1, num2)
    else:
        divisor = min(num1, num2)
        while True:
            divisor = divisor % resto
            if resto != 0:
                resto = divisor
                continue
            else:
                return divisor

numero = mcd(60,40)
print(numero)
