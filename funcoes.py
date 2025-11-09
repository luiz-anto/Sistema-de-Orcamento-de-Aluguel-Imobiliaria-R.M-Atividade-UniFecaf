import csv

def calcular_aluguel_base(tipo_imovel):
    if tipo_imovel == 1:
        return 700.00
    elif tipo_imovel == 2:
        return 900.00
    elif tipo_imovel == 3:
        return 1200.00

def calcular_adicionais(tipo_imovel, quantidade_quartos, possui_vaga, quantidade_vagas_estudio):
    valor_adicional = 0
    if tipo_imovel == 1 and quantidade_quartos == 2:
        valor_adicional += 200.00
    elif tipo_imovel == 2 and quantidade_quartos == 2:
        valor_adicional += 250.00
    if (tipo_imovel == 1 or tipo_imovel == 2) and possui_vaga == "S":
        valor_adicional += 300.00
    if tipo_imovel == 3:
        if quantidade_vagas_estudio >= 2:
            valor_adicional += 250.00
        if quantidade_vagas_estudio > 2:
            vagas_extras = quantidade_vagas_estudio - 2
            valor_adicional += vagas_extras * 60.00
    return valor_adicional

def desconto(valor_aluguel, tipo_imovel, possui_criancas):
    if tipo_imovel == 1 and possui_criancas == "N":
        valor_aluguel *= 0.95
    return valor_aluguel

def gerar_csv(valor_aluguel, valor_parcela_contrato, parcelas):
    with open("parcelas_orcamento.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Mês", "Valor mensal (R$)", "Observação"])
        for mes in range(1, 13):
            if mes <= parcelas:
                valor_mes = valor_aluguel + valor_parcela_contrato
                observacao = f"Aluguel + parcela do contrato ({mes}/{parcelas})"
            else:
                valor_mes = valor_aluguel
                observacao = "Apenas aluguel"
            escritor.writerow([f"{mes}º mês", f"R$ {valor_mes:.2f}", observacao])
