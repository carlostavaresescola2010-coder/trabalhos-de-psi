def gerar_sigla(frase):
    """
    Gera uma sigla a partir de uma frase.
    Extrai a primeira letra de cada palavra e converte para maiúsculas.
    """
    palavras = frase.split()
    sigla = ''.join(palavra[0].upper() for palavra in palavras if palavra)
    return sigla


def main():
    print("=" * 50)
    print("GERADOR DE SIGLAS")
    print("=" * 50)
    print()

    while True:
        # Pedir ao utilizador uma frase
        frase = input("Digite uma frase (ou 'sair' para terminar): ").strip()

        # Verificar se o utilizador quer sair
        if frase.lower() == 'sair':
            print("\nObrigado por usar o Gerador de Siglas!")
            break

        # Verificar se a frase não está vazia
        if not frase:
            print("⚠️  Por favor, digite uma frase válida.\n")
            continue

        # Gerar e mostrar a sigla
        sigla = gerar_sigla(frase)

        print("\n" + "-" * 50)
        print(f"Frase original: {frase}")
        print(f"Sigla gerada: {sigla}")
        print("-" * 50)
        print()


if __name__ == "__main__":
    main()
