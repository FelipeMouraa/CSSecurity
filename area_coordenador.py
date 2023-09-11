#IMPORT LIBS
from Bibliotecas.imports import *

def janela2_ac():
    root = tk.Tk()
    _fundoIMG = tk.PhotoImage(file="imgs/fundoCSSecurityAreaCoordenador.png")
    _logoIMG = "imgs/logo.png"
    _BUTTON_activebackgroundcolor = "#C91818"
    _BUTTON_backgroundcolor = "#142643"
    _FUNDO_backgroundcolor = "#31529D"
    _foregroundcolorWHITE = "white"
    _ENTRY_backgroundcolor = "#a79fff"
    _ENTRY_insertbackgroundforegroundcolor = "#000833"
    _ENTRY_selectbackgroundcolor = "#5648ff"
    _FONT_padrao = "-family {Dubai Medium} -size 13"

######################################## JANELA 2 PROPRIEDADES ################################################

    root.geometry("450x600+470+110")
    root.minsize(450, 600)
    root.maxsize(450, 600)
    root.resizable(0,  0)
    root.title("CSSecurity - Área do Coodernador")

################################################  ICONE  ########################################################################

    root.iconphoto(False, tk.PhotoImage(file=_logoIMG))

###############################################  IMG DE FUNDO   #################################################################

    LabelFundo = tk.Label(root)
    LabelFundo.place(relx=0.0, rely=0.0, width=450, height=600)
    LabelFundo.configure(image=_fundoIMG)

###############################################  Botão 1: Registrar #################################################################
    
    #FUNÇÃO TRANSIÇÃO -> 'REGISTRAR DADOS'
    def registrar():
        root.destroy()
        import registrar as registrar
        registrar.janela3_registrar()

    Button1 = tk.Button(root)
    Button1.place(relx=0.165, rely=0.600, height=30, width=310)
    Button1.configure(
        activebackground=_BUTTON_activebackgroundcolor, activeforeground=_foregroundcolorWHITE, background=_BUTTON_backgroundcolor,foreground=_foregroundcolorWHITE, cursor="hand2", font=_FONT_padrao, borderwidth=0,
        text='''Registrar''', command=registrar
    )
###############################################  Botão 3: Alteração Dados #################################################################
    
    #FUNÇÃO TRANSIÇÃO -> 'CONSULTAR DADOS'
    def consultar():
        root.destroy()
        import consultar as consultar
        consultar.janela4_consultar()

    Button2 = tk.Button(root)
    Button2.place(relx=0.165, rely=0.675, height=30, width=310)
    Button2.configure(
        activebackground=_BUTTON_activebackgroundcolor, activeforeground=_foregroundcolorWHITE, background=_BUTTON_backgroundcolor,foreground=_foregroundcolorWHITE, cursor="hand2", font=_FONT_padrao, borderwidth=0,
        text='''Consultar''', command=consultar
    )

    
###############################################  Botão 3: Alteração Dados #################################################################
    
    #FUNÇÃO TRANSIÇÃO -> 'CONSULTAR DADOS'
    def alteracao_dados():
        root.destroy()
        import alteracao_dados as alteracao_dados
        alteracao_dados.janela5_alteracaodados()

    Button2 = tk.Button(root)
    Button2.place(relx=0.165, rely=0.750, height=30, width=310)
    Button2.configure(
        activebackground=_BUTTON_activebackgroundcolor, activeforeground=_foregroundcolorWHITE, background=_BUTTON_backgroundcolor,foreground=_foregroundcolorWHITE, cursor="hand2", font=_FONT_padrao, borderwidth=0,
        text='''Alteração de Dados''', command=alteracao_dados
    )

###############################  Botao 4: Voltar ################################################################################################

    #FUNÇÃO TRANSIÇÃO -> 'MENU'root
    def menu():
        root.destroy()
        import menu as menu
        menu.janela1_menu()

    Button3 = tk.Button(root)
    Button3.place(relx=0.165, rely=0.830, height=30, width=310)
    Button3.configure(
        activebackground=_BUTTON_activebackgroundcolor, activeforeground=_foregroundcolorWHITE, background=_BUTTON_backgroundcolor,foreground=_foregroundcolorWHITE, cursor="hand2", font=_FONT_padrao, borderwidth=0,
        text='''Menu''', command=menu
    )

    root.mainloop()