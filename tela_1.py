import PySimpleGUI as sg

def file_browser_window(theme):
    sg.theme(theme)
    layout_fb = [[sg.T('SOCIOECONÔMICO', font='_ 18', justification='c', expand_x=True)],
                [sg.T('Escolha um arquivo') , sg.Input(), sg.FileBrowse('Escolha um arquivo', k='-FILEBROWSE-', button_color='gray')],
                 [sg.Ok('Continuar', button_color='gray'), sg.Cancel('Sair', button_color='red')]

                 ]

    return sg.Window('Perfil Socioeconômico - Buscar arquivo', layout=layout_fb, finalize=True, size=(800, 300))

