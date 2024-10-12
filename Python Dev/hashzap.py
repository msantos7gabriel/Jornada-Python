import flet as ft

def main(pagina):

    # Função que recebe mensagens através do túnel pubsub
    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    # Inscreve a função enviar_mensagem_tunel para receber mensagens
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    # Função para abrir o popup e exibir a tela de entrada
    def abrir_popup(event):
        pagina.overlay.append(popup)
        popup.open = True
        pagina.update()
        print('Clicou no Botão')

    # Função para entrar no chat
    def entrar_chat(event):
        popup.open = False
        pagina.remove(titulo)
        pagina.remove(botão)
        mensagem = f'{caixa_nome.value} entrou no Chat'
        pagina.pubsub.send_all(mensagem)  # Envia mensagem para todos
        pagina.add(chat)
        pagina.add(linha_enviar)
        pagina.update()

    # Função para enviar mensagem pelo chat
    def enviar_msg(event):
        nome_usuário = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        if texto_campo_mensagem:  # Verifica se o campo não está vazio
            mensagem = f'{nome_usuário}: {texto_campo_mensagem}'
            pagina.pubsub.send_all(mensagem)  # Envia mensagem para todos
            campo_enviar_mensagem.value = ''  # Limpa o campo de mensagem
            pagina.update()

    #  Index - Tela inicial
    titulo = ft.Text('Hashzap')
    botão = ft.ElevatedButton('Iniciar Chat', on_click=abrir_popup)

    # Chat
    campo_enviar_mensagem = ft.TextField(
        label="Digite aqui sua mensagem", on_submit=enviar_msg)
    botão_enviar = ft.ElevatedButton('Enviar', on_click=enviar_msg)
    linha_enviar = ft.Row([campo_enviar_mensagem, botão_enviar])
    chat = ft.Column()

    # Popup para inserir nome
    titulo_popup = ft.Text('Bem Vindo ao Hashzap')
    caixa_nome = ft.TextField(label="Insira seu nome")
    botão_popup = ft.ElevatedButton('Entrar Chat', on_click=entrar_chat)
    popup = ft.AlertDialog(
        title=titulo_popup, content=caixa_nome, actions=[botão_popup])

    pagina.add(titulo)
    pagina.add(botão)


# Inicializa o aplicativo
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
