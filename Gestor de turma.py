# ==================================
# Sistema de Gestão de uma Turma
# ==================================

# ---------- MINHA CLASSE ----------
class Aluno:
    def __init__(self, nome, idade, nota, curso):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        self.curso = curso
        self.faltas_presenca = 0
        self.faltas_disciplina = 0
        self.faltas_material = 0

    def total_faltas(self):
        return self.faltas_presenca + self.faltas_disciplina + self.faltas_material

    def __str__(self):
        return (
            f"Nome: {self.nome} | Idade: {self.idade} | Nota: {self.nota} | Curso: {self.curso}\n"
            f"Faltas -> Presença: {self.faltas_presenca}, "
            f"Disciplina: {self.faltas_disciplina}, "
            f"Material: {self.faltas_material}"
        )


# ---------- CLASSE TURMA ----------
class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        print("✅ Aluno adicionado com sucesso!")

    def listar_alunos(self):
        if not self.alunos:
            print("⚠️ Não existem alunos registados.")
            return False

        print("\n📋 Lista de Alunos:")
        for i, aluno in enumerate(self.alunos, start=1):
            print(f"\n{i}. {aluno}")
        return True

    def remover_aluno(self, indice):
        removido = self.alunos.pop(indice)
        print(f"🗑️ Aluno '{removido.nome}' removido com sucesso!")

    def marcar_falta(self, indice, tipo):
        aluno = self.alunos[indice]

        if tipo == "1":
            aluno.faltas_presenca += 1
        elif tipo == "2":
            aluno.faltas_disciplina += 1
        elif tipo == "3":
            aluno.faltas_material += 1

        print("⚠️ Falta registada com sucesso!")

    def estatisticas_aluno(self, indice):
        aluno = self.alunos[indice]

        print("\n📊 Estatísticas do Aluno")
        print(f"Nome: {aluno.nome}")
        print(f"Curso: {aluno.curso}")
        print(f"Nota: {aluno.nota}")
        print(f"Total de faltas: {aluno.total_faltas()}")
        print(f"- Presença: {aluno.faltas_presenca}")
        print(f"- Disciplina: {aluno.faltas_disciplina}")
        print(f"- Material: {aluno.faltas_material}")

    def listar_por_curso(self):
        if not self.alunos:
            print("⚠️ Não existem alunos.")
            return

        cursos = {}

        for aluno in self.alunos:
            cursos.setdefault(aluno.curso, []).append(aluno)

        print("\n📚 Alunos por Curso")
        for curso, alunos in cursos.items():
            print(f"\n🎓 Curso: {curso}")
            for aluno in alunos:
                print(f"- {aluno.nome}")

    def estatisticas_turma_por_curso(self):
        if not self.alunos:
            print("⚠️ Não existem alunos.")
            return

        # Lista de cursos existentes
        cursos = list(set(aluno.curso for aluno in self.alunos))
        print("\nCursos disponíveis:")
        for i, curso in enumerate(cursos, start=1):
            print(f"{i} - {curso}")

        # Escolher curso
        while True:
            escolha = input("Escolha o curso pelo número: ")
            if escolha.isdigit():
                indice = int(escolha) - 1
                if 0 <= indice < len(cursos):
                    curso_escolhido = cursos[indice]
                    break
            print("❌ Curso inválido. Tente novamente.")

        alunos_curso = [a for a in self.alunos if a.curso == curso_escolhido]

        total_presenca = sum(a.faltas_presenca for a in alunos_curso)
        total_disciplina = sum(a.faltas_disciplina for a in alunos_curso)
        total_material = sum(a.faltas_material for a in alunos_curso)

        print(f"\n📈 Estatísticas do Curso: {curso_escolhido}")
        print(f"Número de alunos: {len(alunos_curso)}")
        print(f"Total de faltas de presença: {total_presenca}")
        print(f"Total de faltas de disciplina: {total_disciplina}")
        print(f"Total de faltas de material: {total_material}")


# ---------- FUNÇÕES DE VALIDAÇÃO ----------
def ler_nome(mensagem="Nome"):
    while True:
        nome = input(f"{mensagem}: ").strip()
        if nome and nome.replace(" ", "").isalpha():
            return nome
        print("❌ Valor inválido. Use apenas letras.")


def ler_idade():
    while True:
        idade = input("Idade: ")
        if idade.isdigit() and 5 <= int(idade) <= 120:
            return int(idade)
        print("❌ Idade inválida.")


def ler_nota():
    while True:
        try:
            nota = float(input("Nota (0 a 20): "))
            if 0 <= nota <= 20:
                return nota
        except ValueError:
            pass
        print("❌ Nota inválida.")


def escolher_indice(maximo):
    while True:
        escolha = input("Número do aluno: ")
        if escolha.isdigit():
            indice = int(escolha) - 1
            if 0 <= indice < maximo:
                return indice
        print("❌ Aluno inválido.")


# ---------- MENUS ----------
def menu():
    print("\n====== GESTOR DE TURMA ======")
    print("1 - Adicionar aluno")
    print("2 - Listar alunos")
    print("3 - Marcar falta")
    print("4 - Estatísticas de um aluno")
    print("5 - Estatísticas da turma por curso")
    print("6 - Remover aluno")
    print("7 - Listar alunos por curso")
    print("0 - Sair")
    return input("Escolha uma opção: ")


def menu_faltas():
    print("\nTipo de falta:")
    print("1 - Falta de presença")
    print("2 - Falta disciplinar")
    print("3 - Falta de material")
    return input("Escolha: ")


# ---------- FUNÇÃO PRINCIPAL ----------
def main():
    turma = Turma()

    while True:
        opcao = menu()

        if opcao == "1":
            nome = ler_nome("Nome do aluno")
            idade = ler_idade()
            nota = ler_nota()
            curso = ler_nome("Curso")
            turma.adicionar_aluno(Aluno(nome, idade, nota, curso))

        elif opcao == "2":
            turma.listar_alunos()

        elif opcao == "3":
            if not turma.listar_alunos():
                continue
            indice = escolher_indice(len(turma.alunos))

            tipo = menu_faltas()
            while tipo not in ("1", "2", "3"):
                print("❌ Tipo inválido.")
                tipo = menu_faltas()

            turma.marcar_falta(indice, tipo)

        elif opcao == "4":
            if not turma.listar_alunos():
                continue
            indice = escolher_indice(len(turma.alunos))
            turma.estatisticas_aluno(indice)

        elif opcao == "5":
            turma.estatisticas_turma_por_curso()

        elif opcao == "6":
            if not turma.listar_alunos():
                continue
            indice = escolher_indice(len(turma.alunos))
            turma.remover_aluno(indice)

        elif opcao == "7":
            turma.listar_por_curso()

        elif opcao == "0":
            print("👋 Programa encerrado.")
            break

        else:
            print("❌ Opção inválida.")


# ---------- EXECUÇÃO ----------
if __name__ == "__main__":
    main()
