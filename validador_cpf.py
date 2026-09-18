import re

def formatar_cpf(cpf):
    """Formata a string para o padrão 000.000.000-00"""
    cpf_limpo = re.sub(r'[^0-9]', '', cpf)
    if len(cpf_limpo) == 11:
        return f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}"
    return cpf # Retorna original caso não tenha 11 dígitos

def validar_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)
    
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    # Cálculo do 1º Dígito Verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito_1 = (soma * 10) % 11
    if digito_1 == 10:
        digito_1 = 0
        
    # Cálculo do 2º Dígito Verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito_2 = (soma * 10) % 11
    if digito_2 == 10:
        digito_2 = 0
        
    return cpf[-2:] == f"{digito_1}{digito_2}"

def main():
    while True:
        print("\n" + "="*40)
        print("     VALIDADOR DE CPF INTELIGENTE")
        print("="*40)
        
        entrada = input("Digite o CPF (apenas números ou formatado): ").strip()
        
        # Valida e formata
        if validar_cpf(entrada):
            cpf_formatado = formatar_cpf(entrada)
            print(f"\n[SUCESSO] O CPF {cpf_formatado} é matematicamente VÁLIDO.")
        else:
            print(f"\n[AVISO] O CPF informado é INVÁLIDO.")
            
        # Pergunta se deseja continuar
        opcao = input("\nDeseja validar outro CPF? (1 - Sim / 2 - Sair): ").strip()
        if opcao != '1':
            print("\nEncerrando o programa. Até logo!")
            break

if __name__ == "__main__":
    main()