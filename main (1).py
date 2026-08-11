nome = input("Digite seu nome: ").strip()
idade = int(input("Digite sua idade:"))
idade_minima = 14

print("\n--- VERIFICAÇÃO DE ACESSO ---")

if idade >= idade_minima:
    print(f"{nome}, seu acesso a oficina foi liberado.")
    print("Você ja possui a idade minima exigida.")
else:
    anos_faltantes = idade_minima - idade
    print(f"{nome}, seu acesso ainda não foi liberado.")
    print(f"Faltam {anos_falantes} ano(s)para atringir idade minima.")