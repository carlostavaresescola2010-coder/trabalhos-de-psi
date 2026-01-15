print("=== GERADOR DE SIGLAS ===\n")

while True:
    frase = input("Digite uma frase: ")

    if not frase.strip():
        print("Erro: Digite algo!\n")
        continue

    palavras = frase.split()

    sigla = ""
    for palavra in palavras:
        sigla += palavra[0].upper()

    print(f"\nFrase: {frase}")
    print(f"Sigla: {sigla}")
    print(f"Número de palavras: {len(palavras)}\n")

    continuar = input("Gerar outra? (s/n): ")

    if continuar != 's':
        print("\nPrograma encerrado!")
        break
