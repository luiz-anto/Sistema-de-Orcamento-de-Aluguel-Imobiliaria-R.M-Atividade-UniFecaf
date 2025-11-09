from funcoes import *

print("\n===== SISTEMA DE ORÇAMENTO DE ALUGUEL - IMOBILIÁRIA R.M =====\n")

print("""Escolha o tipo de imóvel:
1 - Apartamento (R$ 700,00)
2 - Casa        (R$ 900,00)
3 - Estúdio     (R$ 1200,00)""")
tipo_imovel = int(input("Selecione uma opção: "))

if tipo_imovel in (1, 2):
    quantidade_quartos = int(input("Quantos quartos? (1 ou 2): "))
else:
    quantidade_quartos = 1

if tipo_imovel in (1, 2):
    possui_vaga = input("Deseja vaga de garagem? (S/N): ").upper()
else:
    possui_vaga = "N"

if tipo_imovel == 3:
    quantidade_vagas_estudio = int(input("Quantidade de vagas no estúdio (mínimo 0): "))
else:
    quantidade_vagas_estudio = 0

if tipo_imovel == 1:
    possui_criancas = input("Possui crianças? (S/N): ").upper()
else:
    possui_criancas = "S"

valor_base = calcular_aluguel_base(tipo_imovel)
valor_adicional = calcular_adicionais(tipo_imovel, quantidade_quartos, possui_vaga, quantidade_vagas_estudio)
valor_aluguel = valor_base + valor_adicional
valor_aluguel = desconto(valor_aluguel, tipo_imovel, possui_criancas)

valor_contrato = 2000.00
parcelas = int(input("\nDeseja dividir o contrato em quantas vezes? (1 a 5): "))
valor_parcela_contrato = valor_contrato / parcelas

print("\n===== ORÇAMENTO GERADO =====")
print(f"Valor do aluguel mensal (somente aluguel): R$ {valor_aluguel:.2f}")
print(f"Valor mensal do contrato parcelado ({parcelas}x): R$ {valor_parcela_contrato:.2f}")
print(f"Total nos meses com parcela do contrato: R$ {(valor_aluguel + valor_parcela_contrato):.2f}")

gerar_csv(valor_aluguel, valor_parcela_contrato, parcelas)
print("\nArquivo 'parcelas_orcamento.csv' gerado com sucesso!\n")
