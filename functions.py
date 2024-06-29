# functions.py
from dados import usuarios, conteudos #importação dos dicionários

def cadastrar_usuario(nome, email, senha, tipo_assinatura):
    if tipo_assinatura != 'b' and tipo_assinatura != 'p': # caso o tipo de assinatura não for existente com os planos do sistema
        return None
    else:
        if tipo_assinatura == 'b': tipo_assinatura = 'básica' 
        else: tipo_assinatura='premium'
        id_usuario = max(usuarios.keys(), default=0) + 1 # adiciona um novo id para o novo usuário, retorna a lista de chaves de id's e retorna o maior valor entre ela, e caso não tenha chave, o valor será do novo id será 0+1
        usuarios[id_usuario] = {'nome': nome, 'email': email, 'senha': senha, 'tipo_assinatura': tipo_assinatura, 'preferencias': [], 'historico': []} #adiciona mais um atributo do objeto usuário
        return id_usuario


def login_usuario(email, senha):
    for id, usuario in usuarios.items(): #para cada id no dicionário usuarios
        if usuario['email'] == email and usuario['senha'] == senha:
            return id #retorna o id do usuário logado
    return None #retorna valor nulo se não for validado o login

def excluir_usuario(id_usuario):
    if id_usuario and id_usuario in usuarios:
    #if id_usuario:
        #if id_usuario in usuarios:
        del usuarios[id_usuario] #deleta a chave de usuário e seus valores no dicionário
        return True #existe no dicionário
    return False #não existe mais no dicionário

def alterar_senha(id_usuario, nova_senha):
    if id_usuario and id_usuario in usuarios:
        usuarios[id_usuario]['senha'] = nova_senha #troca o valor de senha daquele usuário específico, identificando pela sua chave ou ID
        return True
    return False

def listar_conteudos(): #função para printar a lista dos conteúdos disponíveis no sistema, utilizando o dicionário de conteudos
    conteudo_info = []
    for id, conteudo in conteudos.items():
        conteudo_info.append(f"ID: {id}, Título: {conteudo['titulo']}, Tipo: {conteudo['tipo']}, Descrição: {conteudo['descricao']}")
    return conteudo_info

def assistir_conteudo(id_usuario, id_conteudo): # função que vai servir como contador ao histórico do usuário. Na teoria é uma função para realizar a ação de assistir o conteúdo
    if id_usuario and id_conteudo in conteudos:
        usuarios[id_usuario]['historico'].append(id_conteudo)
        usuarios[id_usuario]['historico'] = usuarios[id_usuario]
        ['historico'][-3:] #deixa apenas os três últimos conteúdos
        return conteudos[id_conteudo]['titulo']
    

def ver_tipo_assinatura(id_usuario):
    if id_usuario and id_usuario in usuarios:
        return usuarios[id_usuario]['tipo_assinatura']
    

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
    

def alterar_preferencias(id_usuario, genero, adicionar=True):
    #primeiro verifica se o atributo está ON, para saber se e o usuário está logado ou não, para depois verificar se ele está no dicionário 'usuario'
    if id_usuario and id_usuario in usuarios:
        if adicionar:
            if genero not in usuarios[id_usuario]['preferencias']:
                usuarios[id_usuario]['preferencias'].append(genero)
        else:
            if genero in usuarios[id_usuario]['preferencias']:
                usuarios[id_usuario]['preferencias'].remove(genero)
        return True
    return False    #essa função vai fazer com que você adiciona ou remova as preferências, se você digitar para a entrada uma preferência já existente, ela irá ser removida, se ela for nova, ela será adicionada para o dicionário e valor da chave especifíca. Entretanto, esse esquema nada prático será corrigido na main.py


def ver_historico(id_usuario):
    if id_usuario and id_usuario in usuarios:
        historico_ids = usuarios[id_usuario]['historico'][-3:]
        return [conteudos[id]['titulo'] for id in historico_ids]
   

def recomendar_conteudos(id_usuario):
    if id_usuario in usuarios:
        preferencias = usuarios[id_usuario]['preferencias']
        if not preferencias:
            return "Usuário sem preferência"

        recomendados = []
        for id_conteudo, conteudo in conteudos.items():
            #função any verifica se ao menos um dos elementos do iterável é verdadeiro
            if any(generos in conteudo['generos'] for generos in preferencias):
                recomendados.append(f"ID: {id_conteudo}, Título: {conteudo['titulo']}, Tipo: {conteudo['tipo']}, Descrição: {conteudo['descricao']}")

        if not recomendados:
            return "Nenhum conteúdo corresponde às suas preferências."
        return recomendados

    return "Erro: Usuário não logado."

