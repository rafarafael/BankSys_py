class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.saques_diarios = 0
        self.limite_saques_diarios = 3
        self.limite_saque = 500.00

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido. O depósito deve ser um valor positivo.")

    def sacar(self, valor):
        if self.saques_diarios >= self.limite_saques_diarios:
            print("Limite de saques diários atingido.")
        elif valor > self.limite_saque:
            print(f"Erro: O valor máximo de saque é R$ {self.limite_saque:.2f}")
        elif valor > self.saldo:
            print("Erro: Saldo insuficiente.")
        elif valor > 0:
            self.saldo -= valor
            self.saques_diarios += 1
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido. O saque deve ser um valor positivo.")

    def mostrar_extrato(self):
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            print("\nExtrato:")
            for movimentacao in self.extrato:
                print(movimentacao)
            print(f"\nSaldo atual: R$ {self.saldo:.2f}\n")

# Função principal para testar o sistema
def main():
    banco = SistemaBancario()

    while True:
        print("\n=== Menu ===")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Visualizar Extrato")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor a ser depositado: R$ "))
            banco.depositar(valor)
        
        elif opcao == "2":
            valor = float(input("Digite o valor a ser sacado: R$ "))
            banco.sacar(valor)
        
        elif opcao == "3":
            banco.mostrar_extrato()

        elif opcao == "4":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
