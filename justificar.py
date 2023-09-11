#IMPORT LIBS
from Bibliotecas.imports import *

def janela5_justificar():

    root = tk.Tk()
    _fundoIMG = tk.PhotoImage(file="imgs/fundoCSSecurityJustificar.png")
    _logoIMG = "imgs/logo.png"
    _BUTTON_activebackgroundcolor = "#C91818"
    _BUTTON_backgroundcolor = "#142643"
    _FUNDO_backgroundcolor = "#31529D"
    _foregroundcolorWHITE = "white"
    _ENTRY_backgroundcolor = "#a79fff"
    _ENTRY_insertbackgroundforegroundcolor = "#000833"
    _ENTRY_selectbackgroundcolor = "#5648ff"
    _FONT_padrao = "-family {Dubai Medium} -size 13"

######################################## JANELA 4 PROPRIEDADES ################################################
    
    root.geometry("450x600+458+40")
    root.minsize(450, 600)
    root.maxsize(450, 600)
    root.resizable(0,  0)
    root.title("CSSecurity - Justificar")

################################################  ICONE  ########################################################################

    root.iconphoto(False, tk.PhotoImage(file=_logoIMG))

###############################################  IMG DE FUNDO   #################################################################

    def unselectEntry(event):
        root.focus()# tira o foco dos entry
    LabelFundo = tk.Label(root)
    LabelFundo.place(relx=0.0, rely=0.0, width=450, height=600)
    LabelFundo.configure(image=_fundoIMG)
    LabelFundo.bind('<Button-1>', unselectEntry)#botao esquerdo
    LabelFundo.bind('<Button-3>', unselectEntry)#botao direito

###############################################  Label 1: Entrada + Entry 1 #################################################################
    
    Label1 = tk.Label(root)
    Label1.place(relx=0.165, rely=0.257, height=20, width=310)
    Label1.configure(
        background=_FUNDO_backgroundcolor, foreground=_foregroundcolorWHITE,font=_FONT_padrao, 
        text='''Entrada'''
    )

    Entry1 = tk.Entry(root)
    Entry1.place(relx=0.165, rely=0.293, height=30, relwidth=0.689)
    Entry1.configure(
        background=_ENTRY_backgroundcolor, insertbackground=_ENTRY_insertbackgroundforegroundcolor, foreground=_ENTRY_insertbackgroundforegroundcolor, font=_FONT_padrao, selectbackground=_ENTRY_selectbackgroundcolor, selectforeground=_foregroundcolorWHITE, borderwidth=4, relief="flat",
    )
    

###############################################  Label 2: Saída + Entry 2 #################################################################

    Label2 = tk.Label(root)
    Label2.place(relx=0.165, rely=0.36, height=20, width=310)
    Label2.configure(
        background=_FUNDO_backgroundcolor, foreground=_foregroundcolorWHITE,font=_FONT_padrao, 
        text='''Saída'''
    )

    Entry2 = tk.Entry(root)
    Entry2.place(relx=0.165, rely=0.4, height=30, relwidth=0.689)
    Entry2.configure(
        background=_ENTRY_backgroundcolor, insertbackground=_ENTRY_insertbackgroundforegroundcolor, foreground=_ENTRY_insertbackgroundforegroundcolor, font=_FONT_padrao, selectbackground=_ENTRY_selectbackgroundcolor, selectforeground=_foregroundcolorWHITE,  borderwidth=4, relief="flat",
    )

###############################################  Label 3: Justificar + Entry 3 #################################################################

    Label3 = tk.Label(root)
    Label3.place(relx=0.165, rely=0.463, height=20, width=310)
    Label3.configure(
        background=_FUNDO_backgroundcolor, foreground=_foregroundcolorWHITE,font=_FONT_padrao, 
        text='''Justificativa'''
    )

    Entry3 = tk.Entry(root)
    Entry3.place(relx=0.165, rely=0.507, height=30, relwidth=0.689)
    Entry3.configure(
        background=_ENTRY_backgroundcolor, insertbackground=_ENTRY_insertbackgroundforegroundcolor, foreground=_ENTRY_insertbackgroundforegroundcolor, font=_FONT_padrao, selectbackground=_ENTRY_selectbackgroundcolor, selectforeground=_foregroundcolorWHITE,  borderwidth=4, relief="flat",
    )        

######################################    Botao 1: Somente Hoje + Botao 2: Permanente      ########################################################################################
    def sucesso():
        mess.showinfo(title="Sucesso", message="Justificado como somente hoje!")

    Button1 = tk.Button(root)
    Button1.place(relx=0.165, rely=0.615, height=30, width=310)
    Button1.configure(
        activebackground=_BUTTON_activebackgroundcolor, activeforeground=_foregroundcolorWHITE, background=_BUTTON_backgroundcolor,foreground=_foregroundcolorWHITE, cursor="hand2", font=_FONT_padrao, borderwidth=0,
        text='''Somente Hoje''', command=sucesso
    )

    def sucesso2():
        mess.showinfo(title="Sucesso", message="Justificado como permanente!")
    
    Button2 = tk.Button(root)
    Button2.place(relx=0.165, rely=0.677, height=30, width=310)
    Button2.configure(
        activebackground=_BUTTON_activebackgroundcolor, activeforeground=_foregroundcolorWHITE, background=_BUTTON_backgroundcolor,foreground=_foregroundcolorWHITE, cursor="hand2", font=_FONT_padrao, borderwidth=0,
        text='''Permanente''', command=sucesso2
    )

###############################  Botao 3: Voltar ################################################################################################

    #FUNÇÃO VOLTAR PARA JANELA 'CONSULTAR DADOS'
    def voltar_consultar():
        root.destroy()
        import alteracao_dados as alteracao_dados
        alteracao_dados.janela5_alteracaodados()

    Button3 = tk.Button(root)
    Button3.place(relx=0.165, rely=0.79, height=30, width=310)
    Button3.configure(
        activebackground=_BUTTON_activebackgroundcolor, activeforeground=_foregroundcolorWHITE, background=_BUTTON_backgroundcolor,foreground=_foregroundcolorWHITE, cursor="hand2", font=_FONT_padrao, borderwidth=0,
        text='''Voltar''', command=voltar_consultar
    )

    root.mainloop()



