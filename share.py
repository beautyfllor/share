# Função para receber a opção desejada pelo usuário
def recebe_opcao():
    print()
    opcao = int(input("Escolha uma opção: \n(1) Cadastrar como ONG \n(2) Cadastrar como Empresa" 
                      + "\n(3) ONGs parceiras \n(4) Empresas parceiras \nOpção: "))
    return opcao

#Função para cadastrar a ONG
def cadastro_ong():

    print()
    nome = input("Digite o nome da ONG: ")
    ongs.append(nome)
    email = input("Digite o email da ONG (Ex: ong@gmail.com): ")
    ong_emails.append(email)
    telefone = input("Digite o telefone da ONG: (Ex: (11) 9 0000-0000): ")
    ong_tel.append(telefone)
    cep = input("Digite o CEP da ONG (Ex: 00000-000): ")
    estatuto = input("Insira o arquivo do documento do estatuto social da ONG (Ex: estatuto_social.pdf): ")

    print()
    print(f"A ONG {nome} foi cadastrada com sucesso!!")
    print()

    return ongs, ong_emails, ong_tel, nome, email, telefone, cep, estatuto

#Função para cadastrar a empresa
def cadastro_empresa():

    print()
    nome = input("Digite o nome da empresa: ")
    empresas.append(nome)
    email = input("Digite o email da empresa (Ex: ong@gmail.com): ")
    empresa_emails.append(email)
    telefone = input("Digite o telefone da empresa (Ex: (11) 9 0000-0000): ")
    empresa_tel.append(telefone)
    cep = input("Digite o CEP da empresa (Ex: 00000-000): ")
    cnpj = input("Digite o CNPJ da empresa (Ex: 00.000.000/0000-00): ")

    print()
    print(f"A Empresa {nome} foi cadastrada com sucesso!!")
    print()

    return empresas, empresa_emails, empresa_tel, nome, email, telefone, cep, cnpj

#Função para exibir as ONGs cadastradas
def exibir_ongs(ongs, ong_emails, ong_tel):
    print()
    print(f"As ONGs parceiras são: ")
    print()

    for i in range(len(ongs)):
        print(f"{i + 1}. {ongs[i]}\n \nEntre em contato através desses canais:\nEmail: {ong_emails[i]}\nTelefone: {ong_tel[i]}")
        print()

#Função para exibir as empresas cadastradas
def exibir_empresas(empresas, empresa_emails, empresa_tel):
    print()
    print(f"As empresas parceiras são: ")
    print()

    for i in range(len(empresas)):
        print(f"{i + 1}. {empresas[i]}\n \nEntre em contato através desses canais:\nEmail: {empresa_emails[i]}\nTelefone: {empresa_tel[i]}")
        print()

#Função para definir a opção escolhida pelo usuário a fim de chamar as funções operacionais corretas
def define_opcao(opcao):
    while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
        opcao = int(input("Opção inválida, digite <1>, <2>, <3> ou <4> para prosseguir: "))
    match opcao:
            case 1:
               cadastro_ong()
            case 2:
               cadastro_empresa()
            case 3:
                exibir_ongs(ongs, ong_emails, ong_tel)
            case 4:
                exibir_empresas(empresas, empresa_emails, empresa_tel)

#Código de teste (main/principal)
print()    
print("S H A R E")

nome = ""
email = ""
telefone = ""
cep = ""
estatuto = ""
cnpj  = ""

ongs = ["ONG 00 Fome", "Instituto O Plano Contra a Fome", "Instituto Colheita Solidária", "Banquete da Vida"]
empresas = ["Mercado Atacadasso", "Mercado Açaí", "Restaurante Comida Brasileira", "Lanchonete Lanches Felizes"]
ong_emails = ["ong00fome@gmail.com", "ipcfome@gmail.com", "icsolidaria@gmail.com", "banquetevida@gmai.com"]
empresa_emails = ["atacadasso@gmail.com", "mercadoacai@gmail.com", "comidabra@gmail.com", "lanchesfelizes@gmail.com"]
ong_tel = ["(11) 9 2385-8945", "(11) 9 7894-1248", "(11) 9 9630-0894", "(11) 9 5546-5872"]
empresa_tel = ["(11) 9 5688-2193", "(11) 9 7469-5887", "(11) 9 0189-5695", "(11) 9 6579-2426"]

continua = 1

while continua == 1:

    opcao = recebe_opcao()
    define_opcao(opcao)

    continua = int(input("Deseja continuar? \n(1) Sim \n(2) Não \nResposta: "))

print()
print("Obrigada! :)")