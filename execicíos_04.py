# 4 - Verificação de senha forte

senha = input("Digite uma senha: ")

erros = []

if len(senha) < 8:
    erros.append("• Deve conter pelo menos 8 caracteres.")
if not any(c.isupper() for c in senha):
    erros.append("• Deve conter pelo menos 1 letra maiúscula.")
if not any(c.islower() for c in senha):
    erros.append("• Deve conter pelo menos 1 letra minúscula.")
if not any(c.isdigit() for c in senha):
    erros.append("• Deve conter pelo menos 1 número.")
if not any(c in "!@#$%^&*()-_=+[]{}/?;:,.<>|" for c in senha):
    erros.append("• Deve conter pelo menos 1 caractere especial.")

print("\n---- VERIFICAÇÃO DE SENHA ----")
if len(erros) == 0:
    print("Senha Forte! ✔")
else:
    print("Senha Fraca! ✖")
    print("Regras não atendidas:")
    for erro in erros:
        print(erro)