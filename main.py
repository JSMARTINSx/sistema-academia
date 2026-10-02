
alunos = []

while True:
    print("SISTEMA DA ACADEMIA")
    print("1 - Cadastrar aluno")
    print("2 - Consultar aluno")
    print("3 - Listar alunos")
    print("4 - Remover aluno")
    print("5 - Sair")

    opcao = input("Escolha uma opcao: ")
    if opcao == "1":
        nome = input("Nome completo: ")
        idade = input("Idade: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")

        aluno = {

            "nome": nome,
            "idade": idade,
            "cpf": cpf,
            "telefone": telefone

        }

        alunos.append(aluno)
        print("Aluno cadastrado com sucesso")


    elif opcao == "2":
        if len(alunos) == 0:
           print("Nenhum aluno cadastrado")
           continue

        cpf_busca = input("CPF: ")
        encontrado = False


        for aluno in alunos:
            if cpf_busca == aluno["cpf"]:
                print("Nome: ", aluno["nome"])
                print("Idade: ", aluno["idade"])
                print("CPF: ", aluno["cpf"])
                print("Telefone: ", aluno["telefone"])
                encontrado = True

        if encontrado == False:
           print("Aluno não encontrado")

    elif opcao == "3":
          print("Lista de alunos cadastrados")

          if len(alunos) == 0:
              print("Nenhum aluno cadastrado")

          for aluno in alunos:

              print("Nome: ", aluno["nome"])
              print("Idade: ", aluno["idade"])
              print("CPF: " , aluno["cpf"])
              print("Telefone: ", aluno["telefone"])
              print("------------------------------")

    elif opcao == "4":
        if len(alunos) == 0:
           print("Nenhum aluno cadastrado")
           continue

        cpf_busca = input("CPF: ")
        encontrado = False
        for aluno in alunos:
            if cpf_busca == aluno["cpf"]:
                alunos.remove(aluno)
                print("Aluno removido com sucesso: ", aluno["nome"])
                encontrado = True

        if encontrado == False:
             print("Aluno não encontrado")


    elif opcao == "5":
        break