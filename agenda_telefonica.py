AGENDA = {}

# Exemplo de contatos iniciais
AGENDA['joao'] = {
    'endereco': 'Rua dolores fonseca 326',
    'email': 'joao10@gmail.com',
    'telefone': '119 3568-7643'
}

AGENDA['maria'] = {
    'endereco': 'Rua martins de andrade 27',
    'email': 'mariay@gmail.com',
    'telefone': '119 3577-7643'
}


# --- FUNÇÕES ---

def mostrar_contatos_ordenados():
    """Mostra todos os contatos na agenda em ordem alfabética."""
    if AGENDA:
        # Obtém e ordena os nomes dos contatos
        nomes_ordenados = sorted(AGENDA.keys())
        for contato in nomes_ordenados:
            mostrar_agenda_decontatos(contato)
            print('---------------------------')
    else:
        print(' >>> AGENDA VÁZIA!')
        print('---------------------------')


def mostrar_agenda_decontatos(contato):
    """Mostra os detalhes de um contato específico."""
    try:
        print()
        print('INFORMACAO DO CONTATO')
        print('nome: ', contato)
        print('endereco: ', AGENDA[contato]['endereco'])
        print('email: ', AGENDA[contato]['email'])
        print('telefone: ', AGENDA[contato]['telefone'])
    except KeyError:
        print('>>> Este contato não existe!')
    except Exception as erro:
        print('Algum erro ocorreu!')
        print('>>>', erro)


def detalhes_do_contato():
    """Solicita os detalhes de um novo contato ao usuário."""
    endereco = input('Digite o endereço: ')
    email = input('Digite o email: ')
    telefone = input('Digite o telefone: ')
    return endereco, email, telefone


def adicionar_editar_contato(contato, endereco, email, telefone, silencioso=False):
    """
    Adiciona ou edita um contato e salva no arquivo.
    O parâmetro 'silencioso' evita a impressão da mensagem de sucesso.
    """
    AGENDA[contato] = {
        'endereco': endereco,
        'email': email,
        'telefone': telefone,
    }
    salvar()  # Chama a função para salvar após a alteração
    if not silencioso:
        print('---------------------------')
        print(' >>> Contato {} editado ou adicionado com sucesso'.format(contato))
        print()


def excluir_contato(contato):
    """Exclui um contato da agenda."""
    try:
        AGENDA.pop(contato)
        salvar()
        print(' >>> Contato {} excluído com sucesso!'.format(contato))
        print('---------------------------')
    except KeyError:
        print(' >>> Contato inexistente!')
    except Exception as erro:
        print('Algum erro ocorreu!')
        print('---------------------------')
        print('Erro: >>>', erro)
        print('---------------------------')


def excluir_todos_contatos():
    """Exclui todos os contatos da agenda com confirmação."""
    global AGENDA
    if not AGENDA:
        print(' >>> A agenda já está vazia!')
        print('---------------------------')
        return

    resposta = input('Tem certeza que deseja excluir TODOS os contatos? (S/N): ').upper()
    print('---------------------------')
    if resposta == 'S':
        AGENDA.clear()
        salvar()
        print(' >>> Todos os contatos foram excluídos com sucesso!')
        print('---------------------------')
    else:
        print(' >>> Operação cancelada.')
        print('---------------------------')


def buscar_contato():
    """Busca um contato por nome, email ou telefone."""
    opcoes_busca = ['nome', 'email', 'telefone']
    tipo_busca = input(f"Buscar por {opcoes_busca}? Digite o tipo: ").lower()
    print('---------------------------')

    if tipo_busca not in opcoes_busca:
        print(">>> Tipo de busca inválido. Por favor, escolha entre nome, email ou telefone.")
        print('---------------------------')
        return

    termo_busca = input(f"Digite o {tipo_busca} para buscar: ")
    print('---------------------------')
    encontrados = []

    # Se a busca for por nome, fazemos uma busca direta no dicionário
    if tipo_busca == 'nome':
        if termo_busca.lower() in [key.lower() for key in AGENDA.keys()]:
            encontrados.append(termo_busca)
    else:
        # Se a busca for por email ou telefone, iteramos por todos os contatos
        for nome_contato, detalhes in AGENDA.items():
            if tipo_busca in detalhes and detalhes[tipo_busca].lower() == termo_busca.lower():
                encontrados.append(nome_contato)

    if encontrados:
        print(f">>> Contato(s) encontrado(s) por '{termo_busca}':")
        for contato in encontrados:
            mostrar_agenda_decontatos(contato)
    else:
        print(f">>> Nenhum contato encontrado com o {tipo_busca} '{termo_busca}'.")
    print('---------------------------')


def exportar_arquivo(nome_do_arquivo='database.csv', silencioso=False):
    """
    Exporta todos os contatos para um arquivo CSV.
    O parâmetro 'silencioso' evita a impressão da mensagem de sucesso.
    """
    try:
        with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
            for contato, detalhes in AGENDA.items():
                endereco = detalhes['endereco']
                email = detalhes['email']
                telefone = detalhes['telefone']
                arquivo.write('{},{},{},{}\n'.format(contato, endereco, email, telefone))
        if not silencioso:
            print(' >>> Contatos exportados com sucesso para {}!'.format(nome_do_arquivo))
            print('---------------------------')
    except Exception as erro:
        print(' >>> Algum erro ocorreu!')
        print(' >>> Erro: ', erro)


def importar_arquivo(nome_do_arquivo='database.csv'):
    """Importa contatos de um arquivo CSV de forma silenciosa."""
    try:
        with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                if len(detalhes) == 4:
                    nome = detalhes[0].strip()
                    endereco = detalhes[1].strip()
                    email = detalhes[2].strip()
                    telefone = detalhes[3].strip()
                    # Chamamos a função de forma silenciosa ao carregar
                    adicionar_editar_contato(nome, endereco, email, telefone, silencioso=True)
            print(' >>> Contatos importados com sucesso de {}!'.format(nome_do_arquivo))
    except FileNotFoundError:
        print(' >>> Arquivo {} não encontrado. Iniciando com uma agenda vazia.'.format(nome_do_arquivo))
    except Exception as erro:
        print('Algum erro ocorreu ao importar o arquivo!')
        print('Erro:', erro)
        print('---------------------------')


def salvar():
    """Salva a agenda no arquivo padrão de forma silenciosa."""
    exportar_arquivo('database.csv', silencioso=True)


def carregar():
    """Carrega a agenda do arquivo padrão."""
    importar_arquivo('database.csv')


def menu_agenda():
    """Exibe o menu de opções."""
    print('>>> MENU AGENDA <<<')
    print('1- Mostrar contatos')
    print('2- Buscar contatos')
    print('3- Adicionar contatos')
    print('4- Editar contatos')
    print('5- Excluir contato')
    print('6- Excluir todos os contatos')
    print('7- Exportar arquivo CSV/TXT')
    print('8- Importar arquivo CSV/TXT')
    print('0- Encerrar o programa')


# --- INÍCIO DO PROGRAMA ---
carregar()

while True:
    menu_agenda()
    print('---------------------------')
    entrada = input('Digite uma das opções: ')
    print('---------------------------')

    if entrada == '1':
        mostrar_contatos_ordenados()
    elif entrada == '2':
        buscar_contato()
    elif entrada == '3':
        contato = input('Digite o nome do contato: ')
        if contato in AGENDA:
            print('Contato já existente!')
        else:
            endereco, email, telefone = detalhes_do_contato()
            adicionar_editar_contato(contato, endereco, email, telefone)
            print('---------------------------')
    elif entrada == '4':
        contato = input('Digite o nome do contato: ')
        if contato in AGENDA:
            print('>>> Editando contato: ', contato)
            endereco, email, telefone = detalhes_do_contato()
            adicionar_editar_contato(contato, endereco, email, telefone)
        else:
            print('Contato não encontrado!')
            print('---------------------------')
    elif entrada == '5':
        contato = input('Digite o nome do contato a ser excluído: ')
        excluir_contato(contato)
    elif entrada == '6':
        excluir_todos_contatos()
    elif entrada == '7':
        nome_do_arquivo = input('Digite o nome do arquivo para exportar: ')
        exportar_arquivo(nome_do_arquivo)
    elif entrada == '8':
        nome_do_arquivo = input('Digite o nome do arquivo para importar: ')
        importar_arquivo(nome_do_arquivo)
    elif entrada == '0':
        print('>>> Programa encerrado.')
        print('---------------------------')
        break
    else:
        print('>>> Opção inválida!')
        print('---------------------------')
