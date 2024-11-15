import flet as ft

def main(tela: ft.Page):
    tela.theme_mode = ft.ThemeMode.DARK

    def valida_peso(e):
        peso = tf_peso.value
        try:
            float_peso = float(peso)
            if float_peso <= 0:
                tf_peso.error_text = "Por favor, insira um peso válido"
                tf_peso.value = ""
            else:
                tf_peso.error_text = None
        except ValueError:
            tf_peso.error_text = "Por favor, insira um peso válido"
            tf_peso.value = ""
        tela.update()

    def valida_altura(e):
        altura = tf_altura.value
        try:
            float_altura = float(altura)
            if float_altura <= 0:
                tf_altura.error_text = "Por favor, insira uma altura válida"
                tf_altura.value = ""
            else:
                tf_altura.error_text = None
        except ValueError:
            tf_altura.error_text = "Por favor, insira uma altura válida"
            tf_altura.value = ""
        tela.update()

    def calcular_imc(e):
        try:
            peso = float(tf_peso.value)
            altura = float(tf_altura.value)
            if peso > 0 and altura > 0:
                imc = peso / (altura ** 2)
                if imc < 16:
                    text_mensagem.value = f"Seu IMC é de: {imc:.2f}, você está com uma magreza grave, tome cuidado!"
                elif imc >= 16 and imc < 16.9:
                    text_mensagem.value = f"Seu IMC é de: {imc:.2f}, você está com uma magreza moderada, tome cuidado!"
                elif imc >= 17 and imc < 18.4:
                    text_mensagem.value = f"Seu IMC é de: {imc:.2f}, você está com uma magreza leve, tome cuidado!"
                elif imc >= 18.5 and imc < 24.9:
                    text_mensagem.value = f"Seu IMC é de: {imc:.2f}, você está no peso ideal, continue assim!"
                elif imc >= 25 and imc < 29.9:
                    text_mensagem.value = f"Seu IMC é de: {imc:.2f}, você está com sobrepeso, tome cuidado!"
                elif imc >= 30 and imc < 34.9:
                    text_mensagem.value = f"Seu IMC é de: {imc:.2f}, você está com uma obesidade grau 1, tome cuidado!"
                elif imc >= 35 and imc < 39.9:
                    text_mensagem.value = f"Seu IMC é de: {imc:.2f}, você está com uma obesidade severa, tome cuidado!"
                elif imc > 40:
                    text_mensagem.value = f"Seu IMC é de: {imc:.2f}, você está com uma obesidade mórbida, tome cuidado!"
            else:
                text_mensagem.value = "Por favor, insira valores válidos para peso e altura."
        except ValueError:
            text_mensagem.value = "Por favor, insira valores válidos para peso e altura."
        
        tela.update()

    tela.appbar = ft.AppBar(
        title=ft.Text(value="Calculadora IMC", size=22, color="white", weight="bold"),
        center_title=True,
        bgcolor="#4CADE4"
    )

    tf_peso = ft.TextField(label="Digite seu peso em Quilos(KG)", on_change=valida_peso, width=300)
    tf_altura = ft.TextField(label="Digite sua altura em Metros", on_change=valida_altura, width=300)
    bt_imc = ft.ElevatedButton("Calcular IMC", on_click=calcular_imc)
    text_mensagem = ft.Text("Insira as informações para iniciarmos!", size=22, weight=150)
    result_img = ft.Image(src="src/imcIcon.png", width=150, height=150)

    tela.add(
        ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        tf_peso,
                        tf_altura,
                        ft.Row(
                            controls=[
                                result_img,
                                bt_imc,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        text_mensagem
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True
        )
    )

ft.app(target=main)