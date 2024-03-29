def comparar_datas(data1, data2):
    dia1, mes1, ano1 = data1
    dia2, mes2, ano2 = data2
    
    if ano1 < ano2:
        return "A primeira data ocorreu antes."
    elif ano1 > ano2:
        return "A segunda data ocorreu antes."
    else:
        if mes1 < mes2:
            return "A primeira data ocorreu antes."
        elif mes1 > mes2:
            return "A segunda data ocorreu antes."
        else:
            if dia1 < dia2:
                return "A primeira data ocorreu antes."
            elif dia1 > dia2:
                return "A segunda data ocorreu antes."
            else:
                return "Datas iguais."

print("Digite a primeira data:")
dia1 = int(input("Dia: "))
mes1 = int(input("Mês: "))
ano1 = int(input("Ano: "))

print("\nDigite a segunda data:")
dia2 = int(input("Dia: "))
mes2 = int(input("Mês: "))
ano2 = int(input("Ano: "))

msg = comparar_datas((dia1, mes1, ano1), (dia2, mes2, ano2))

# Imprimir o resultado
print("\nResultado:", msg)