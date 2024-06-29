from dados import usuarios, conteudos #importação dos dicionários

def cadastrar_usuario(nome, email, senha, tipo_assinatura):
    email = email.lower()  # Converte o email para minúsculas
    if tipo_assinatura != 'b' and tipo_assinatura != 'p':
        return None
    else:
        tipo_assinatura = 'básica' if tipo_assinatura == 'b' else 'premium'
        id_usuario = max(usuarios.keys(), default=0) + 1
        usuarios[id_usuario] = {
            'nome': nome,
            'email': email,
            'senha': senha,
            'tipo_assinatura': tipo_assinatura,
            'preferencias': [],
            'historico': []
        }
        return id_usuario


def login_usuario(email, senha):
    email = email.lower()  # Converte o email para minúsculas
    senha = senha.lower()  # Converte a senha para minúsculas (opcional)
    for id, usuario in usuarios.items():
        if usuario['email'] == email and usuario['senha'] == senha:
            return id
    return None


def excluir_usuario(id_usuario):
    if id_usuario and id_usuario in usuarios:
        del usuarios[id_usuario]
        return True
    return False


def alterar_senha(id_usuario, nova_senha):
    if id_usuario and id_usuario in usuarios:
        usuarios[id_usuario]['senha'] = nova_senha
        return True
    return False


def listar_conteudos():
    conteudo_info = []
    for id, conteudo in conteudos.items():
        conteudo_info.append(f"ID: {id}, Título: {conteudo['titulo']}, Tipo: {conteudo['tipo']}, Descrição: {conteudo['descricao']}")
    return conteudo_info


def assistir_conteudo(id_usuario, id_conteudo):
    if id_usuario and id_conteudo in conteudos:
        usuarios[id_usuario]['historico'].append(id_conteudo)
        usuarios[id_usuario]['historico'] = usuarios[id_usuario]['historico'][-3:]
        return conteudos[id_conteudo]['titulo']
    return None


def ver_tipo_assinatura(id_usuario):
    if id_usuario and id_usuario in usuarios:
        return usuarios[id_usuario]['tipo_assinatura']
    return None


def alterar_tipo_assinatura(id_usuario, novo_tipo):
    if id_usuario and id_usuario in usuarios:
        if novo_tipo not in ['b', 'p']:
            return None
        else:
            novo_tipo = 'básica' if novo_tipo == 'b' else 'premium'
            usuarios[id_usuario]['tipo_assinatura'] = novo_tipo
        return True
    return False


def ver_preferencias(id_usuario):
    if id_usuario and id_usuario in usuarios:
        return usuarios[id_usuario]['preferencias']
    return None


def alterar_preferencias(id_usuario, genero, adicionar=True):
    if id_usuario and id_usuario in usuarios:
        genero = genero.lower()  # Converte o gênero para minúsculas
        
        # Obtém a lista de todos os gêneros disponíveis nos conteúdos
        generos_existentes = set()
        for conteudo in conteudos.values():
            for g in conteudo['generos']:
                generos_existentes.add(g.lower())
        
        if genero not in generos_existentes:
            print("Gênero inválido. Por favor, escolha um gênero existente.")
            return False

        if adicionar:
            if genero not in usuarios[id_usuario]['preferencias']:
                usuarios[id_usuario]['preferencias'].append(genero)
        else:
            if genero in usuarios[id_usuario]['preferencias']:
                usuarios[id_usuario]['preferencias'].remove(genero)
        return True
    return False


def ver_historico(id_usuario):
    if id_usuario and id_usuario in usuarios:
        historico_ids = usuarios[id_usuario]['historico'][-3:]
        return [conteudos[id]['titulo'] for id in historico_ids]
    return None


def recomendar_conteudos(id_usuario):
    if id_usuario in usuarios:
        preferencias = [genero.lower() for genero in usuarios[id_usuario]['preferencias']]  # Converte as preferências para minúsculas
        if not preferencias:
            return "Usuário sem preferência"

        recomendados = []
        for id_conteudo, conteudo in conteudos.items():
            conteudo_generos = [genero.lower() for genero in conteudo['generos']]  # Converte os gêneros dos conteúdos para minúsculas
            if any(genero in conteudo_generos for genero in preferencias):
                recomendados.append(f"ID: {id_conteudo}, Título: {conteudo['titulo']}, Tipo: {conteudo['tipo']}, Descrição: {conteudo['descricao']}")

        if not recomendados:
            return "Nenhum conteúdo corresponde às suas preferências."
        return recomendados

    return "Erro: Usuário não logado."
