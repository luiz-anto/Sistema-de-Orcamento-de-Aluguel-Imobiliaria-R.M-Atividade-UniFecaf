# 🏡 Sistema de Orçamento de Aluguel – Atividade UniFecaf

Este projeto foi desenvolvido como parte da disciplina **Algorithmic Thinking & Introduction to Object-Oriented Programming** da UniFecaf.  
O objetivo é criar uma aplicação em Python que **gere orçamentos de aluguel** para uma imobiliária fictícia chamada **R.M Imobiliária**, automatizando o cálculo do valor total com base em diferentes tipos de imóveis e condições de contrato.

---

## 🎯 **Objetivo do Projeto**

O sistema tem como foco **automatizar a geração de orçamentos** para clientes interessados em alugar imóveis.  
Ele permite selecionar o tipo de imóvel, a quantidade de quartos, vagas de garagem e outras opções que influenciam o valor final do aluguel.

---

## ⚙️ **Funcionalidades Principais**

- Escolha do tipo de imóvel:
  - Apartamento (R$ 700,00)
  - Casa (R$ 900,00)
  - Estúdio (R$ 1.200,00)
- Adicionais:
  - Quartos extras e vagas de garagem.
  - Vagas específicas para estúdios.
- Desconto de **5%** em apartamentos sem crianças.
- Cálculo do **valor do contrato (R$ 2.000,00)**, que pode ser parcelado em até **5 vezes**.
- Geração de um arquivo **`.csv`** com o resumo do orçamento.

---

## 💻 **Como o Sistema Funciona**

1. O usuário informa o tipo de imóvel e características desejadas.  
2. O programa calcula automaticamente:
   - Valor base do aluguel;
   - Adicionais (quartos e vagas);
   - Descontos (quando aplicável);
   - Valor do contrato parcelado.
3. O sistema exibe o valor total e gera um arquivo CSV com os dados do orçamento.  

---

## 🧠 **Conceitos Envolvidos**

- Estruturas condicionais (`if`, `else`)
- Funções reutilizáveis (`def`)
- Manipulação de entrada e saída de dados (`input`, `print`)
- Operações matemáticas
- Geração e escrita em arquivos (`.csv`)

---

## 👨‍💻 **Autor**

**Luiz Antônio Marcos**  
🔗 LinkedIn: www.linkedin.com/in/luiz-antonio-marcos
