import PySimpleGUI as sg

def file_browser_window(theme):
    sg.theme(theme)
    layout_fb = [[sg.Input(), sg.FileBrowse('Escolha um arquivo', k='-FILEBROWSE-')],
                  #[sg.Text("Tipo do arquivo:"),
                   #sg.Radio("Ler CSV", "TypeFile", default=True, size=(8, 4), k='-CSV-'),
                 #sg.Radio("Ler Excel", "TypeFile", size=(8, 4), k='-EXCEL-')],
                 [sg.Ok('Continuar'), sg.Cancel('Sair')]

                 ]

    return sg.Window('Perfil Socioeconômico - Buscar arquivo', layout=layout_fb, finalize=True, size=(800, 300))

