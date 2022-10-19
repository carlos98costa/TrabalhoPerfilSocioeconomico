import PySimpleGUI as sg

def file_browser_window(theme):
    sg.theme(theme)
    menu_def = [["Ajuda", ["Sobre", "Equipe", "Sair"]]]
    layout_fb = [[sg.MenubarCustom(menu_def, tearoff=False, background_color='#404040', bar_background_color='#4F4F4F', bar_text_color='white', text_color='white')],
                [sg.T('Perfil Socioeconômico', pad=(80), font='_ 18', justification='c', expand_x=True)],
                [sg.T('Escolha um arquivo') , sg.Input(k='-input-', disabled=True, background_color='gray', text_color='black',), sg.FileBrowse('Escolha um arquivo', k='-FILEBROWSE-', button_color='gray')],
                 [sg.Ok('Continuar', button_color='gray'), sg.Cancel('Voltar', button_color='gray'), sg.Cancel('Sair', button_color='red')]

                 ]

    return sg.Window('Perfil Socioeconômico - Buscar arquivo', layout=layout_fb, finalize=True, size=(800, 310))

