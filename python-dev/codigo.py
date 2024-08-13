import flet as ft

def create_theme():
    return {
        "primary_color": "#b2b39f",
        "secondary_color": "#f5f7bd",
        "background_color": "#dedfc5",
        "text_color": "#3d423c",  # Cor do texto
        "input_text_color": "#3d423c",
        "button_text_color": "#b2b39f",
        "text_clean": "#f8f1e9"
    }

def main(pagina):
    theme = create_theme()
    pagina.bgcolor = theme["background_color"]

    # Cria um título para a página com o texto "Sala de estudos" e tamanho de fonte 40
    titulo = ft.Text("Sala de estudos", size=40, color=theme['text_clean'])

    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    # Cria o botão "Iniciar chat"
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup)

    # Adiciona o título e o botão de iniciar à página, centralizados vertical e horizontalmente
    pagina.add(
        ft.Container(
            content=ft.Column(
                controls=[titulo, botao_iniciar],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,  # Faz com que o container expanda para ocupar todo o espaço disponível
        )
    )

    chat = ft.Column()

    campo_usuario = ft.TextField(label="Digite seu nome", color=theme["input_text_color"])

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem, color=theme["text_color"]))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    titulo_janela = ft.Text("Bem-vindo à sala de estudos", color=theme["text_color"])

    def enviar_mensagem(evento):
        texto = f"{campo_usuario.value}: {texto_menssagem.value}"
        pagina.pubsub.send_all(texto)
        texto_menssagem.value = ""
        pagina.update()

    # Define a largura da caixa de texto e ajusta a cor do texto para ser mais visível
    texto_menssagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem, width=300, color=theme["input_text_color"])
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    # Centraliza o campo de texto e o botão "Enviar"
    linha_mensagem = ft.Row(
        [texto_menssagem, botao_enviar],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER
    )

    def entrar_chat(evento):
        pagina.controls.clear()  # Remove todos os controles da página
        pagina.add(
            ft.Container(
                content=ft.Column(
                    controls=[chat, linha_mensagem],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                expand=True,  # Faz com que o container expanda para ocupar todo o espaço disponível
            )
        )
        texto_entrou_chat = f"{campo_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto_entrou_chat)
        janela.open = False  # Fechar o popup
        pagina.update()

    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    janela = ft.AlertDialog(title=titulo_janela, content=campo_usuario, actions=[botao_entrar])

#ft.app(main) # Aplicação Flet com um ambiente integrado.
ft.app(main, view=ft.WEB_BROWSER) # Aplicação em um navegador web
# Na versão de web, para parar de rodar o código digite ctrl+c no terminal
