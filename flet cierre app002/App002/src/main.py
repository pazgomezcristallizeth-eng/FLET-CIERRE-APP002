import flet as ft
import time


def main(page: ft.Page):
	page.title="¿Me perdonas"
	page.bgcolor=ft.Colors.LIGHT_GREEN_800
	page.horizontal_alignment=ft.CrossAxisAlignmet.CENTER
	page.vertical_alignment=ft.MaimAxisAlignmet.CENTER
	
	
	label=ft.Text(
		"¿Me perdonas",
		style=ft.TextStyle(size=40,weight="bold")
	    )
	image=ft.Image(src="triste.png"width=200,height=200)
	
	button_yes=ft.ElevatedButton(text="Si",color=ft.Colors.GREEN,width=100,height=50)
	button_no=ft.ElevatedButton(text="No",color=ft.Colors.RED,width=100,height=50)
	button_maybe=ft.ElevatedButton(text="Quizas",color=ft.Colors.YELLOW,width=100,height=50)
	
	
	def no_click(e):
		button_yes.width+=20
		button_yes.height+=10
	
	def yes_click(e):
		image.src="feliz.png"
		image.update()
	
	def maybe_click(e):
		image.src("Quiza.png"
		image.update()

				  
		time.sleep(2)
		reset_app()
	
	def reset_app():
		image.src="triste.png"
		button_yes.width=100
		button_yes.height=50
		page.update()
	
	button_no.on_click=no_click
	button_yes.on_click=yes_click
	button_maybe.on_click=maybe_click
	
	page.add(
		ft.Column(
			[label,
			image,
			ft.Row([
				button_yes,
				button_no,
				button_maybe
			],
				  alignment=ft.MainAxisAlignment.CENTES
				  )
			],
			
		)
	)


ft.app(main)
