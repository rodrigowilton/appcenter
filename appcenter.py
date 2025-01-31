import flet as ft

def main(page:ft.Page):
    page.scroll = "adaptive"
    page.padding = ft.padding.all(30)
    page.bgcolor = ft.Colors.BLACK
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Image(src='img/emergencia.png', width=20, height=20),label="Emergência"),
            ft.NavigationBarDestination(icon=ft.Image(src='img/whatsapp.png', width=20, height=20),label="Whatsapp"),
            ft.NavigationBarDestination(icon=ft.Image(src='img/configuracao.png', width=20, height=20),label="Solicitações"),
            ft.NavigationBarDestination(icon=ft.Image(src='img/inf.png', width=20, height=20),label="Informações"),
        ],
    )

    def _camera1():
        camera1 = ft.Container(
            #expand=True,
            padding=ft.padding.all(10),
            bgcolor=ft.Colors.TRANSPARENT,
            border_radius=ft.border_radius.all(20),
            shadow=ft.BoxShadow(blur_radius=5, color='white'),


            content=ft.Image(
                src="imagem/foto1.jpg", 
                fit="cover", 
                width=400,
                height=350,
            )
        )        

        return camera1
    
    
    def _camera2():
        camera2 = ft.Container(
            #expand=True,
            padding=ft.padding.all(10),
            bgcolor=ft.Colors.TRANSPARENT,
            border_radius=ft.border_radius.all(20),
            shadow=ft.BoxShadow(blur_radius=5, color='white'),


            content=ft.Image(
                src="imagem/foto2.jpg", 
                fit="cover", 
                width=400,
                height=350,
            )
        )        

        return camera2
    
    
    def _camera3():
        camera3 = ft.Container(
            #expand=True,
            padding=ft.padding.all(10),
            bgcolor=ft.Colors.TRANSPARENT,
            border_radius=ft.border_radius.all(20),
            shadow=ft.BoxShadow(blur_radius=5, color='white'),


            content=ft.Image(
                src="imagem/foto3.jpg", 
                fit="cover", 
                width=400,
                height=350,
            )
        )        

        return camera3
    
    
    def _camera4():
        camera4 = ft.Container(
            #expand=True,
            padding=ft.padding.all(10),
            bgcolor=ft.Colors.TRANSPARENT,
            border_radius=ft.border_radius.all(20),
            shadow=ft.BoxShadow(blur_radius=5, color='white'),


            content=ft.Image(
                src="imagem/foto4.jpg", 
                fit="cover", 
                width=400,
                height=350,
            )
        )        

        return camera4
    
    
    def _camera5():
        camera5 = ft.Container(
            #expand=True,
            padding=ft.padding.all(10),
            bgcolor=ft.Colors.TRANSPARENT,
            border_radius=ft.border_radius.all(20),
            shadow=ft.BoxShadow(blur_radius=5, color='white'),


            content=ft.Image(
                src="imagem/foto5.jpg", 
                fit="cover", 
                width=400,
                height=350,
            )
        )        

        return camera5
    
    
    def _camera6():
        camera6 = ft.Container(
            #expand=True,
            padding=ft.padding.all(10),
            bgcolor=ft.Colors.TRANSPARENT,
            border_radius=ft.border_radius.all(20),
            shadow=ft.BoxShadow(blur_radius=5, color='white'),


            content=ft.Image(
                src="imagem/foto6.jpg", 
                fit="cover", 
                width=400,
                height=350,
            )
        )        

        return camera6
       
    def _caixaIcon():
        caixaIcon=ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        _botaoIcon(),
                        ft.Text("Pessoas",size=10, weight=ft.FontWeight.BOLD),
                        
                    ]
                ),
                ft.Column(
                     controls=[
                        _botaoIcon2(),
                        ft.Text("Permissões", size=10, weight=ft.FontWeight.BOLD)

                     ]
                ),
                ft.Column(
                     controls=[
                     _botaoIcon3(),
                     ft.Text("Funcionários", size=10, weight=ft.FontWeight.BOLD)

                     ]
                ),
                ft.Column(
                     controls=[
                     _botaoIcon4(),
                     ft.Text("Veículos", size=10, weight=ft.FontWeight.BOLD)
                          
                     ]
                ),
                ft.Column(
                     controls=[
                     _botaoIcon5(),
                     ft.Text("Câmeras", size=10, weight=ft.FontWeight.BOLD)
                          
                     ]
                ),
                ft.Column(
                     controls=[
                     _botaoIcon6(),
                     ft.Text("Acesso", size=10, weight=ft.FontWeight.BOLD)
                          
                     ]
                )
            ],
            scroll='auto',
            alignment=ft.MainAxisAlignment.CENTER,
        )

        return caixaIcon
    
    def _botaoIcon():
        botaoIcon = ft.Row(
                controls=[
                    ft.Container(
                            width=70,
                            height=70,
                            bgcolor=ft.Colors.BLUE_300,
                            border_radius=10,
                            shadow=ft.BoxShadow(blur_radius=5, color='black'),
                            image_src='icon/pessoa.png',
                            image_fit=ft.ImageFit.FIT_HEIGHT,
                    ),

                ]
        )
        
        return botaoIcon
    
    def _botaoIcon2():
        botaoIcon2 = ft.Row(
                controls=[
                    ft.Container(
                            width=70,
                            height=70,
                            bgcolor=ft.Colors.BLUE_300,
                            border_radius=10,
                            shadow=ft.BoxShadow(blur_radius=5, color='black'),
                            image_src='icon/permissao.png',
                            image_fit=ft.ImageFit.FIT_HEIGHT
                    ),

                ]
        )
        
        return botaoIcon2   
    
    def _botaoIcon3():
        botaoIcon3 = ft.Row(
                controls=[
                    ft.Container(
                            width=70,
                            height=70,
                            bgcolor=ft.Colors.BLUE_300,
                            border_radius=10,
                            shadow=ft.BoxShadow(blur_radius=5, color='black'),
                            image_src='icon/funccondominio.png',
                            image_fit=ft.ImageFit.FIT_HEIGHT
                    ),

                ]
        )
        
        return botaoIcon3  

    def _botaoIcon4():
        botaoIcon4 = ft.Row(
                controls=[
                    ft.Container(
                            width=70,
                            height=70,
                            bgcolor=ft.Colors.BLUE_300,
                            border_radius=10,
                            shadow=ft.BoxShadow(blur_radius=5, color='black'),
                            image_src='icon/veiculo.png',
                            image_fit=ft.ImageFit.FIT_HEIGHT
                    ),

                ]
        )
        
        return botaoIcon4  

    def _botaoIcon5():
        botaoIcon5 = ft.Row(
                controls=[
                    ft.Container(
                            width=70,
                            height=70,
                            bgcolor=ft.Colors.BLUE_300,
                            border_radius=10,
                            shadow=ft.BoxShadow(blur_radius=5, color='black'),
                            image_src='icon/cameras.png',
                            image_fit=ft.ImageFit.FIT_HEIGHT
                    ),
                ]
        )
        
        return botaoIcon5                                  
    
    def _botaoIcon6():
        botaoIcon6 = ft.Row(
                controls=[
                    ft.Container(
                            width=70,
                            height=70,
                            bgcolor=ft.Colors.BLUE_200,
                            border_radius=10,
                            shadow=ft.BoxShadow(blur_radius=5, color='black'),
                            image_src='icon/acesso.png',
                            image_fit=ft.ImageFit.FIT_HEIGHT
                    ),
                ]
        )
        
        return botaoIcon6    
      

    def _botaoCameras():
        botaoCameras = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Tabs(
                        selected_index=0,

                        tabs=[
                            ft.Tab(
                                text="Câmera 1",                                
                                content=ft.Row(
                                    controls=[
                                        _camera1()
                                    ],
                                    wrap=True
                                )

                            ),
                            ft.Tab(
                                text='Câmera 2',
                                content=ft.Row(
                                    controls=[
                                        _camera2()

                                    ],
                                    wrap=True
                                )
                            ),
                            ft.Tab(
                                text='Câmera 3',
                                content=ft.Row(
                                    controls=[
                                        _camera3()

                                    ],
                                    wrap=True
                                )
                            ),
                            ft.Tab(
                                text='Câmera 4',
                                content=ft.Row(
                                    controls=[
                                        _camera4()

                                    ],
                                    wrap=True
                                )
                            ),
                            ft.Tab(
                                text='Câmera 5',
                                content=ft.Row(
                                    controls=[
                                        _camera5()

                                    ],
                                    wrap=True
                                )
                            ),
                            ft.Tab(
                                text='Câmera 6',
                                content=ft.Row(
                                    controls=[
                                        _camera6()

                                    ],
                                    wrap=True
                                )
                            )
                        ]
                    )
                ]
            )
        )
  
        return botaoCameras
    
    

    layout = ft.Column(
        expand=True,
        controls=[
            ft.Row(
              controls=[
                   ft.Image(src='icon/icon.png', width=65),

                ]
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[

                     ft.Text(value='Tattica Center', color=ft.Colors.WHITE, text_align=ft.alignment.center, size=20),

                ]

            ),

            ft.Container(
                padding=ft.padding.all(30),
                bgcolor=ft.Colors.TRANSPARENT,
                border_radius=ft.border_radius.all(20),
                margin=ft.margin.symmetric(vertical=30),
                shadow=ft.BoxShadow(blur_radius=5, color='white'),

                content=ft.Row(
                    controls=[
                         _caixaIcon()

                    ],
                    scroll='auto'

                )                  
            ),
            _botaoCameras(),

        ]

    )

    page.add(ft.SafeArea(layout)),
        

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')