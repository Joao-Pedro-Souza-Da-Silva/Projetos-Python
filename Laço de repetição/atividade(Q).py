areas = []
while True:
    nome = input("Digite o nome do cômodo: ")
    largura = float(input("Digite a largura do cômodo em metros: "))
    comprimento = float(input("Digite o comprimento do cômodo em metros: "))
    area = largura * comprimento
    print("A área do cômodo", nome, "é:", area, "metros quadrados.")
    areas.append(area)
    continuar = input("Deseja calcular a área de mais um cômodo? (Digite SIM ou NÃO): ")
    if continuar.upper() == "NÃO":
        area_total = sum(areas)
        print("A área total da residência é:", area_total, "metros quadrados.")
        break