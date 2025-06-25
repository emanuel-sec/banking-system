# banking-system
# - Desafio proporcionado pela DIO (@digitalinnovationone) - Bootcamp Santander 2025 (Backend Python)

# 💰 Projeto: Sistema Bancário em Python

Este é um projeto simples de terminal que simula um sistema bancário, feito em Python como prática de lógica de programação e controle de fluxo.

## 🚀 Tecnologias usadas
- Python 3

## 🧠 Funcionalidades

- Depósito de valores
- Saque com limite por transação e limite diário de saques
- Visualização de extrato com histórico de movimentações
- Validação de entradas (ex: valor negativo, entrada inválida, etc.)

## 📋 Regras do sistema

- O usuário pode fazer até **3 saques por dia**
- O limite de saque por transação é de **R$500,00**
- O sistema trabalha com valores em **centavos** para evitar problemas com `float`
- O extrato mostra **todas as operações**, incluindo tentativas negadas
