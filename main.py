# Exercício 04 - Condiçoes com if, elif e els
nome = input("Digite o nome do aluno: ").strip()
nota1 = float(input("Digite a primeira nota: ").replace(",", "."))
nota2 = float(input("Digite a segunda nota: ").replace(",", "."))

media = (nota1 + nota2) / 2

if media >= 7:
    situação = "Aprovado"
elif media >= 5:
    situação = "Recuperação"
else:
    situação = "Reprovado"
    
print("\n--- RESULTADO ESCOLAR ---")
print(f"Aluno: {nome}")
print(f"Média: {media:.1f}")
print(f"Situação: {situação}")