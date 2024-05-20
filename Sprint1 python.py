
#print para receber o usuario no programa
print("Bem vindo ao Porta Car-Fix")

#Criação de listas para armazenar e organizar dados inseridos pelo usuario
emails = []
nomes = []
placas = []
feedbacks = []
duvidas = []

#função para caso o usuario escolha fazer cadastro no programa
def cadastro():
    while True:
        cadastro = str(input("ja tem uma conta ? \n"))
        #laço caso o usuario escolha uma função que não esta presente nas opções
        while cadastro != "sim" and cadastro != "não":
            cadastro = str(input("ja tem uma conta ? \n"))
        if cadastro == "sim":
            email = str(input("Digite seu email: "))
            senha = str(input("Digite sua senha: "))
        else:

            print("Crie sua conta aqui")

            nomes.append(str(input("Digite seu nome:\n")))
            emails.append(str(input("Digite seu email:\n")))
            senha = str(input("Digite sua senha:\n"))
            confirmSenha = str(input("Confirme sua senha:\n"))
            while senha != confirmSenha:
                print("ERRO!Algum campo foi preenchido errado ")
                senha = str(input("Digite sua senha:\n"))
                confirmSenha = (str(input("Confirme sua senha:\n")))
            print("Seu cadastro foi realizado com sucesso!")
            
            cadastrarVeiculo = str(input("Deseja cadastrar algum veiculo ?"))
            match cadastrarVeiculo:
                case "sim":
                    placas.append(str(input("Para Começarmos, digite os digitos da sua placa:\n")))
                case "não":
                    print("Tudo bem !! Obrigado por utilizar o Porta Car-Fix, volte sempre que precisar de uma ajuda com seus veiculos ")
                case _:
                    print("Opção não cadastrada")


            print(f"O email cadastrado foi {emails}")

            break

##função para alterar alguma informação cadastrada
def mudarInfor ():
    print("Escolha a informação que deseja alterar:")

#função caso o usuario escolha ver os planos do nosso serviço
def planos():
    while True:
        planos = str(input("Quer visualizar todos nossos planos ? \n"))
        #laço caso o usuario escolha uma opção que não esta disponivel
        while planos != "sim" and planos != "não":
            planos = str(input("Quer visualizar todos nossos planos ? \n"))
        if planos == "sim":
            print("Temos o planos de: Cobertura Total, que concede acesso a todos serviços dentro do nosso site \nCobertura Parcial, que vai de acordo com a sua região, automovel, e equipamento\nCobertura Mecânica, nesse plano tera acesso apenas acesso a analise de um mecanico ")

            detalhesPlanos = str(input("Deseja ver com mais detalhe algum plano ?\nSe quiser ver o plano de Cobertura Total digite '1'\nSe quiser ver o plano Cobertura Parcial digite '2'\n Se quiser ver o plano Cobertura Mecânica digite '3'"))
            match detalhesPlanos:
                case "1":
                    print("Neste plano sera possivel ter acesso a todas funções dentro do nosso sistema, como uso completo da nossa IA capaz de analisar os dados que o usuario digitar e sugerir alguns possiveis problemas e quais seriam as possiveis soluções, neste plano tambem esta incluso o  uso de mecanicas parceiras ao nosso sistema, sera disponibilizado uma inteligencia artificial que ira dar a devida atenção ao cliente ")
                case "2":
                    print("Neste plano você vai ter acesso ao nosso chat-bot, que tem a função de te ajudar a auto-diagnosticar os problemas do seu veiculo, passar uma media de preço para o conserto, mas não vai ter auxilio mecanico cobrado pelo plano!")
                case "3":
                    print("Neste plano você tera acesso aos mecanicos parceiros do nosso sistema e ter um desconto ou cobertura total do preço do seu problema")
        else:
            print("para vizualiar seus planos faça cadastro")
        


            
        break

#função caso o usuario escolha mandar uma duvida para a central de atendimento
def duvida():
    while True:
        duvidas = str(input("digite sua duvida, referente ao auto atendimento, a resposta pode ser rapida ou levar horas: "))
        break

#função caso o usuario queira dar um feedback para a empresa
def feedback():
    while True:
        feedbacks = str(input("Digite aqui seu feedback para que podemos melhorar nosso serviço e oferecer uma melhor entrega de resultados: "))
        break

while True:
    #variavel para saber o que o usuario quer fazer dentro do menu 
    intencao = str(input("O que deseja fazer ? \n Você pode acessar seu perfil digitando '1' \n Você pode ver as opções de planos disponiveis e quais você tem acesso digitando '2' \n Alguma duvida digite '3'\n Caso queira dar um feedback digite '4' \n "))

    #laço de repetiçao para caso o usuario insira uma opção não cadastrada
    while intencao != "1" and intencao != "2" and intencao != "3" and intencao != "4":
    
        intencao  = str(input("Aqui temos algumas opções possiveis dentro do nosso site\n Você pode acessar seu perfil digitando '1', caso queira mudar alguma informção de cadastro digite 'alterar'\n Você pode ver as opções de planos disponiveis e quais você  tem acesso digitando '2'\n Alguma duvida digite '3'\n Caso queira dar um feedback digite '4' \n "))
    match intencao:
        case "1":cadastro()

        case "2":planos()

        case "3":duvida()

        case "4":feedback()

        case _:
            print("Opção não cadastrada")
