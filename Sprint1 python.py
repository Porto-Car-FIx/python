print("Bem vindo ao Porta Car-Fix")

intecao = str(input("O que deseja fazer ? \n Você pode acessar seu perfil digitando '1' \n Você pode ver as opções de planos disponiveis e quais você  tem acesso digitando '2' \n Alterar as configurações do site digitando '3'\n"))

while intecao != "1" and intecao != "2" and intecao != "3" :

    intecao = int(input("O que deseja fazer ? \n Você pode acessar seu perfil digitando '1' \n Você pode ver as opções de planos disponiveis e quais você  tem acesso digitando '2' \n Alterar as configurações do site digitando '3' \n"))

if intecao == "1":
    cadastro = str(input("ja tem uma conta ? \n"))
    while cadastro != "sim" and cadastro != "não":
        cadastro = str(input("ja tem uma conta ? \n"))
    if cadastro == "sim":
        email = str(input("Digite seu email: "))
        senha = str(input("Digite sua senha: "))
    else:
        print("Crie sua conta aqui")
        email = str(input("Digite seu email: "))
        senha = str(input("Digite sua senha: "))
    

if intecao == "2":
    planos = str(input("Quer visualizar todos nossos planos ? \n"))
    while planos != "sim" and planos != "não":
         planos = str(input("Quer visualizar todos nossos planos ? \n"))
    if planos == "sim":
        print("Temos o planos de: Cobertura Total, que concede acesso a todos serviços dentro do nosso site \nCobertura Parcial, que vai de acordo com a sua região, automovel, e equipamento\nCobertura Mecânica, nesse plano tera acesso apenas acesso a analise de um mecanico ")

#if intecao == 3:
