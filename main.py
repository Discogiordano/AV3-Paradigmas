# main.py
from functions import (cadastrar_usuario, login_usuario, excluir_usuario, alterar_senha,
                       listar_conteudos, assistir_conteudo, ver_tipo_assinatura, alterar_tipo_assinatura,
                       ver_preferencias, alterar_preferencias, ver_historico, recomendar_conteudos)

def main():
    usuario_logado = None # variável que armazena o ID do usuário logado, tem o default de 0.

    #menu do sistema
    while True:
        print("\nMenu:")
        print("1. Cadastrar Usuário")
        print("2. Login")
        print("3. Excluir Usuário")
        print("4. Alterar Senha")
        print("5. Listar Conteúdos")
        print("6. Assistir Conteúdo")
        print("7. Ver Tipo de Assinatura")
        print("8. Alterar Tipo de Assinatura")
        print("9. Ver Preferências")
        print("10. Alterar Preferências")
        print("11. Ver Histórico")
        print("12. Recomendação por preferência")
        print("13. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")
            tipo_assinatura = input("Tipo de Assinatura (básica, premium) (b/p): ")                
            cadastrar_usuario(nome, email, senha, tipo_assinatura) #chamada de função
            if tipo_assinatura in ['b', 'p']:
                print("Usuário cadastrado com sucesso!") 
            else: 
                print("Erro de cadastro")
            
            

        elif escolha == '2':
            email = input("Email: ")
            senha = input("Senha: ")
            usuario_logado = login_usuario(email, senha)
            if usuario_logado:
                print("Login bem-sucedido!")
            else:
                print("Email ou senha incorretos.")

        elif escolha == '3':
            if usuario_logado and excluir_usuario(usuario_logado): #caso ambos forem verdadeiros
                print("Usuário excluído com sucesso.")
                usuario_logado = None
            else:
                print("Falha ao excluir usuário.")

        elif escolha == '4':
            if usuario_logado:
                nova_senha = input("Nova senha: ")
                if alterar_senha(usuario_logado, nova_senha):
                    print("Senha alterada com sucesso.")
                else:
                    print("Falha ao alterar senha.")
            else:
                print("Erro: Usuário não logado.")

        elif escolha == '5':
            conteudos = listar_conteudos()
            for conteudo in conteudos:
                print(conteudo)

        elif escolha == '6':
            if usuario_logado:
                id_conteudo = int(input("ID do Conteúdo para assistir: ")) #diga o ID do filme que você quer assistir
                resultado = assistir_conteudo(usuario_logado, id_conteudo)
                print(f"Assistido: {resultado}")
            else:
                print("Erro: Usuário não logado.")

        elif escolha == '7':
            if usuario_logado:
                tipo_assinatura = ver_tipo_assinatura(usuario_logado)
                print(f"Tipo de Assinatura: {tipo_assinatura}")
            else:
                print("Erro: Usuário não logado.")

        elif escolha == '8':
            if usuario_logado:
                novo_tipo = input("Novo tipo de assinatura (básica, premium): (b/p)")
                if alterar_tipo_assinatura(usuario_logado, novo_tipo) and novo_tipo in ('b','p'):
                    print("Tipo de assinatura atualizado com sucesso.")
                else:
                    print("Falha ao atualizar tipo de assinatura.")
            else:
                print("Erro: Usuário não logado.")

        elif escolha == '9':
            if usuario_logado:
                preferencias = ver_preferencias(usuario_logado)
                print("Preferências:", ', '.join(preferencias)) #concartenar as strings do atributo preferencias
                if not preferencias:
                    print("sem preferencias")
            else:
                print("Erro: Usuário não logado.")

        elif escolha == '10':
            if usuario_logado:
                genero = input("Gênero para adicionar ou remover: ")
                acao = input("Adicionar ou Remover? (a/r): ")
                if alterar_preferencias(usuario_logado, genero, adicionar=(acao.lower() == 'a')): #se a resposta for 'a' então adicionar será true, satisfazendo a condição de adicionar, do contrário, será remove
                    print("Preferências atualizadas com sucesso.")
                else:
                    print("Falha ao atualizar preferências.")
            else:
                print("Erro: Usuário não logado.")

        elif escolha == '11':
            if usuario_logado:
                historico = ver_historico(usuario_logado)
                print("Histórico de visualizações:", ', '.join(historico))
            else:
                print("Erro: Usuário não logado.")

        elif escolha == '12':
            if usuario_logado:
                recomendados = recomendar_conteudos(usuario_logado)
                #verificar se recomendados é uma instância da classe list
                if isinstance(recomendados, list):
                    print("Conteúdos recomendados:")
                    for conteudo in recomendados:
                        print(conteudo)
                else:
                    print(recomendados)
            else:
                print("Erro: Usuário não logado.")

        elif escolha == '13':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

#caso o script for executado diretamente
if __name__ == "__main__":
    main()
