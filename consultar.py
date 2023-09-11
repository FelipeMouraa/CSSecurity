#IMPORT LIBS
from tkinter import Label
from Bibliotecas.imports import *

def janela4_consultar():

    root = tk.Tk()
    _fundoIMG = tk.PhotoImage(file="imgs/fundoCSSecurityConsultar.png")
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

    root.geometry("450x500+470+110")
    root.minsize(450, 500)
    root.maxsize(450, 500)
    root.resizable(0,  0)
    root.title("CSSecurity - Consultar")

################################################  ICONE  ########################################################################

    root.iconphoto(False, tk.PhotoImage(file=_logoIMG))

###############################################  IMG DE FUNDO   #################################################################

    def unselectEntry(event):
        root.focus()# tira o foco dos entry
    LabelFundo = tk.Label(root)
    LabelFundo.place(relx=0.0, rely=0.0, width=450, height=500)
    LabelFundo.configure(image=_fundoIMG)
    LabelFundo.bind('<Button-1>', unselectEntry)#botao esquerdo
    LabelFundo.bind('<Button-3>', unselectEntry)#botao direito


###############################################  Label 1: Dias #################################################################
    
    Label1 = tk.Label(root)
    Label1.place(relx=0.165, rely=0.250, height=20, width=310)
    Label1.configure(
        background=_FUNDO_backgroundcolor, foreground=_foregroundcolorWHITE,font=_FONT_padrao, 
        text='''Dias'''
    )

    cal = DateEntry(root)
    cal.place(relx=0.340, rely=0.300, height=35, width=150)
    

###############################################  Label 2: Turmas  #################################################################
    
    Label2 = tk.Label(root)
    Label2.place(relx=0.165, rely=0.380, height=20, width=310)
    Label2.configure(
        background=_FUNDO_backgroundcolor, foreground=_foregroundcolorWHITE,font=_FONT_padrao, 
        text='''Turmas'''
    )

    var = tk.StringVar()
    var.set("")
    data=("3DA", "3DB", "2DA", "2DB", "1DA", "1DB")
    cb=Combobox(root, values=data)
    cb.place(relx=0.340, rely=0.440, height=35, width=150)
    

###############################################  Label 3: RM  #################################################################
    
    Label2 = tk.Label(root)
    Label2.place(relx=0.165, rely=0.520, height=20, width=310)
    Label2.configure(
        background=_FUNDO_backgroundcolor, foreground=_foregroundcolorWHITE,font=_FONT_padrao, 
        text='''RM'''
    )

    root.Entry2 = tk.Entry(root)
    root.Entry2.place(relx=0.340, rely=0.570, height=35, width=150)
    root.Entry2.configure(
        background=_ENTRY_backgroundcolor, insertbackground=_ENTRY_insertbackgroundforegroundcolor, foreground=_ENTRY_insertbackgroundforegroundcolor, font=_FONT_padrao, selectbackground=_ENTRY_selectbackgroundcolor, selectforeground=_foregroundcolorWHITE,  borderwidth=4, relief="flat",
    )
    

######################################    Botao 1: Consultar    ########################################################################################
    def consulta():
        aluno = []
        with open("Historico\Historico_" + "29-11-2022" + ".csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for lines in reader1:
                aluno.append(str(lines))
            rm = str(root.Entry3.get())
            turmas = str(cb.get())
            for linha in aluno:
                if rm in linha and turmas in linha:
                    mess.showinfo(title='Consulta', message=str(linha))
                elif linha == "[]" or "Id" in linha:
                    pass
                else:
                    mess.showerror(title='Erro', message="Aluno não encontrado")

    Button1 = tk.Button(root)
    Button1.place(relx=0.165, rely=0.690, height=30, width=310)
    Button1.configure(
        activebackground=_BUTTON_activebackgroundcolor, activeforeground=_foregroundcolorWHITE, background=_BUTTON_backgroundcolor,foreground=_foregroundcolorWHITE, cursor="hand2", font=_FONT_padrao, borderwidth=0,
        text='''Consultar''', command=consulta
    )
    
###############################  Botao 2: Voltar ################################################################################################

    #FUNÇÃO VOLTAR PARA JANELA 'MENU'
    def areaCoordenador():
        root.destroy()
        import area_coordenador as area_coordenador
        area_coordenador.janela2_ac()

    Button2 = tk.Button(root)
    Button2.place(relx=0.165, y=400, height=30, width=310)
    Button2.configure(
        activebackground=_BUTTON_activebackgroundcolor, activeforeground=_foregroundcolorWHITE, background=_BUTTON_backgroundcolor,foreground=_foregroundcolorWHITE, cursor="hand2", font=_FONT_padrao, borderwidth=0,
        text='''Voltar''', command=areaCoordenador
    )

    root.mainloop()



