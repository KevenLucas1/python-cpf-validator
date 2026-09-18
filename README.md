# 🛡️ Python CPF Validator (Validador de CPF Inteligente)

Ferramenta interativa desenvolvida em Python para validar a autenticidade de CPFs utilizando o algoritmo oficial de cálculo dos dígitos verificadores, contando com formatação automática e menu contínuo.

## 🚀 Tecnologias e Funcionalidades
* **Linguagem:** Python 3
* **Módulos Nativos:** `re` (para limpeza e manipulação de expressões regulares).
* **Principais Recursos:**
  * Validação matemática real do 1º e 2º dígitos verificadores.
  * Filtro de segurança contra sequências numéricas falsas (ex: `111.111.111-11`).
  * Formatação automática de máscara (`000.000.000-00`).
  * Menu interativo com loop de repetição para múltiplas consultas sem fechar o terminal.

## ⚙️ Como executar
1. Certifique-se de ter o Python instalado.
2. Baixe o arquivo `validador_cpf.py`.
3. Execute no seu terminal:
   ```bash
   python validador_cpf.py
4. Digite o CPF quando solicitado.
5. Escolha se deseja realizar uma nova consulta ou sair.
