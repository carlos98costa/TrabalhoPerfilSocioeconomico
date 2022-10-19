import PySimpleGUI as sg



def tela_inicial(theme):
    sg.theme(theme)
    menu_def = [["Ajuda", ["Sobre", "Equipe", "Sair"]]]
    layout_inicial = [[sg.MenubarCustom(menu_def, tearoff=False, background_color='#404040', bar_background_color='#4F4F4F', bar_text_color='white', text_color='white')],
                    [sg.T('Bem-vindo ao programa de Perfil Socioeconômico!', size=(23, 2), pad=(80), font='_ 18', justification='c', expand_x=True)],
                    [sg.Ok('Continuar', button_color='gray'), sg.Cancel('Sair', button_color='red')]

                 ]

    return sg.Window('Perfil Socioeconômico - Buscar arquivo', layout=layout_inicial, finalize=True, size=(800, 310))


