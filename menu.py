#IMPORT LIBS
from ast import Break
from Bibliotecas.imports import *


#FUNÇÃO DA TELA INICIAL DO SISTEMA
def janela1_menu():

    root = tk.Tk()
    _fundoIMG = tk.PhotoImage(file="imgs/fundoCSSecurityMenu.png")
    _logoIMG = "imgs/logo.png"   
    _BUTTON_activebackgroundcolor = "#C91818"
    _BUTTON_backgroundcolor = "#142643"
    _FUNDO_backgroundcolor = "#31529D"
    _foregroundcolorWHITE = "white"
    _TREEVIEW_backgroundcolor = "#9BABCC"
    _TREEVIEW_foregroundcolor = "#000833"
    _TREEVIEW_selectedbackgroundcolor = "#5648ff"
    _FONT_padrao = "-family {Dubai Medium} -size 13"
    _FONT_datahorario = "-family {Dubai Medium} -size 16"
    _FONT_insertTREEVIEW = "-family {Dubai Medium} -size 11"
    _FONT_selectedinsertTREEVIEW = "-family {Dubai Medium} -size 12"


    #FUNÇÃO PARA VALIDAR SE HÁ TODOS OS ARQUIVOS NECESSÁRIOS
    def validacao_arqv(path):
        dir = os.path.dirname(path) # dir = DIRETÓRIO 
        if not os.path.exists(dir):
            os.makedirs(dir)

    #FUNÇÃO ENTRE CONTATO, ERRO NA VALIDAÇÃO(arquivo.xml INEXISTENTE)
    def checar_facepadrao():
        exists = os.path.isfile("face_padrao.xml") # exists = face_padrao.xml
        if exists:
            pass
        else:
            mess.showinfo(title='Arquivo faltando', message='Entre em contato conosco para obter ajuda')
            window.destroy()

    #FUNÇÃO CONTATO COM O SUPORTE DEV
    def contato():
        mess.showinfo(title='Contate-nos', message="Suporte : 'cssecurity@gmail.com' ")

    #FUNÇÃO SALVAR SENHA
    def salvar_senha():
        validacao_arqv("DadosGerais/")
        exists1 = os.path.isfile("DadosGerais\senha.txt")
        if exists1:
            tf = open("DadosGerais\senha.txt", "r")
            key = tf.read()
        else:
            master.destroy()
            new_pas = tsd.askstring('Senha antiga não encontrada', 'Por favor, digite uma nova senha abaixo', show='*')
            if new_pas == None:
                mess.showinfo(title='Nenhuma senha inserida', message='Senha não definida! Por favor, tente novamente')
            else:
                tf = open("DadosGerais\senha.txt", "w")
                tf.write(new_pas)
                mess.showinfo(title='Senha registrada', message='Nova senha registrada com sucesso!')
                return
        op = (old.get())
        newp= (new.get())
        nnewp = (nnew.get())
        if (op == key):
            if(newp == nnewp):
                txf = open("DadosGerais\senha.txt", "w")
                txf.write(newp)
            else:
                mess.showinfo(title='Erro', message='Confirme a nova senha novamente!')
                return
        else:
            mess.showinfo(title='Senha incorreta', message='Por favor, digite a senha antiga correta.')
            return
        mess.showinfo(title='Senha alterada', message='Senha alterada com sucesso!')
        master.destroy()

    #FUNÇÃO MUDAR SENHA
    def mudar_senha():
        global master
        master = tk.Tk()
        master.geometry("400x160")
        master.resizable(False,False)
        master.title("Mudar senha")
        master.configure(background="white")
        lbl4 = tk.Label(master,text='    Digite a senha antiga: ',bg='white',font=('times', 12, ' bold '))
        lbl4.place(x=10,y=10)
        global old
        old=tk.Entry(master,width=25 ,fg="black",relief='solid',font=('times', 12, ' bold '),show='*')
        old.place(x=180,y=10)
        lbl5 = tk.Label(master, text='   Digite a nova senha: ', bg='white', font=('times', 12, ' bold '))
        lbl5.place(x=10, y=45)
        global new
        new = tk.Entry(master, width=25, fg="black",relief='solid', font=('times', 12, ' bold '),show='*')
        new.place(x=180, y=45)
        lbl6 = tk.Label(master, text='Confirme nova senha: ', bg='white', font=('times', 12, ' bold '))
        lbl6.place(x=10, y=80)
        global nnew
        nnew = tk.Entry(master, width=25, fg="black", relief='solid',font=('times', 12, ' bold '),show='*')
        nnew.place(x=180, y=80)
        cancel=tk.Button(master,text="Cancelar", command=master.destroy ,fg="black"  ,bg="red" ,height=1,width=25 , activebackground = "white" ,font=('times', 10, ' bold '))
        cancel.place(x=200, y=120)
        save1 = tk.Button(master, text="Salvar", command=salvar_senha, fg="black", bg="#3ece48", height = 1,width=25, activebackground="white", font=('times', 10, ' bold '))
        save1.place(x=10, y=120)
        master.mainloop()

    def localizar_images():
        checar_facepadrao()
        validacao_arqv("Historico/")
        validacao_arqv("DadosAlunos/")
        for k in tv.get_children():
            tv.delete(k)
        msg = ''
        i = 0
        j = 0

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        exists3 = os.path.isfile("DadosGerais\pontos_faces.yml")
        if exists3:
            recognizer.read("DadosGerais\pontos_faces.yml")
        else:
            mess.showinfo(title='Dados ausentes', message='Por favor, clique em Salvar Perfil para redefinir os dados!')
            return
        harcascadePath = "face_padrao.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath);

        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        col_names = ['Id', '', 'Nome', '', 'Data', '', 'Hora']
        exists1 = os.path.isfile("DadosAlunos\dados_alunos.csv")
        if exists1:
            df = pd.read_csv("DadosAlunos\dados_alunos.csv")
        else:
            mess.showinfo(title='Detalhes ausentes', message='Faltam detalhes dos alunos, verifique!')
            cam.release()
            cv2.destroyAllWindows()
            window.destroy()
        while True:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
                serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
                if (conf < 50):
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa = df.loc[df['ID'] == serial]['NOME'].values
                    ID = df.loc[df['ID'] == serial]['RM'].values
                    ID = str(ID)
                    ID = ID[1:-1]
                    bb = str(aa)
                    bb = bb[2:-2]
                    Historico = [str(ID), '', bb, '', str(date), '', str(timeStamp)]
                else:
                    Id = 'Desconhecido'
                    bb = str(Id)
                cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
            cv2.imshow('CSSecurity', im)
            if (cv2.waitKey(1) == 27):
                break
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
        exists = os.path.isfile("Historico\Historico_" + date + ".csv")
        if exists:
            with open("Historico\Historico_" + date + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(Historico)
            csvFile1.close()
        else:
            with open("Historico\Historico_" + date + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(col_names)
                writer.writerow(Historico)
            csvFile1.close()
        with open("Historico\Historico_" + date + ".csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for lines in reader1:
                i = i + 1
                if (i > 1):
                    if (i % 2 != 0):
                        iidd = str(lines[0]) + '   '
                        tv.insert('', 0, text=iidd, values=(str(lines[0]), str(lines[2]), str(lines[4]), str(lines[6])))
        csvFile1.close()
        cam.release()
        cv2.destroyAllWindows()
    
######################################## JANELA 1 PROPRIEDADES ################################################

    root = root
    root.geometry("760x680+296+14")# tamanho da janela e posição que ela aparece
    root.minsize(760, 680)
    root.maxsize(760, 680)
    root.resizable(0,  0)
    root.title("CSSecurity - Sistema")

################################################  ICONE E NAVBAR ########################################################################

    root.iconphoto(False, tk.PhotoImage(file=_logoIMG))

    menubar = tk.Menu(root, relief='ridge')
    filemenu = tk.Menu(menubar,tearoff=0)
    filemenu.add_command(label='Mudar senha', command = mudar_senha)
    filemenu.add_command(label='Contate-nos', command = contato)
    filemenu.add_command(label='Sair',command = root.destroy)
    menubar.add_cascade(label='Ajuda',font=('times', 29, ' bold '),menu=filemenu)       
    root.configure(menu=menubar)

###############################################  IMG DE FUNDO   #################################################################

    def unselectInsertTreeview(event):
        tv.selection_remove(tv.focus())#tira o foco dos inserts do treeview 
    LabelFundo = tk.Label(root)
    LabelFundo.place(relx=0.0, rely=0.0, width=760, height=680)
    LabelFundo.configure(image=_fundoIMG)#img de fundo
    LabelFundo.bind('<Button-1>', unselectInsertTreeview)#botao esquerdo
    LabelFundo.bind('<Button-3>', unselectInsertTreeview)#botao direito

####################################################     RELÓGIO E DATA    ##########################################################

    def data_hora():
        time_string = time.strftime('%H:%M:%S')
        clock.config(text=time_string)
        clock.after(200,data_hora)

    date = datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y')
    day,month,year=date.split("-")

    mês={
        '01':'Janeiro', '02':'Fevereiro', '03':'Março', '04':'Abril', '05':'Maio', '06':'Junho',
        '07':'Julho', '08':'Agosto','09':'Setembro', '10':'Outubro', '11':'Novembro', '12':'Dezembro'
    }

    datef = tk.Label(text = day+" "+mês[month]+" "+year, bg=_FUNDO_backgroundcolor, fg=_foregroundcolorWHITE, font=_FONT_datahorario)
    datef.place(x=125, y=162, height=24)

    clock = tk.Label(bg=_FUNDO_backgroundcolor, fg=_foregroundcolorWHITE, font=_FONT_datahorario)
    clock.place(x=570, y=162, height=24, width=77)   
    data_hora()

#####################################   Botão 1:  CSSecurity - Validação   ############################################################

    Button1 = tk.Button(root)
    Button1.place(relx=0.165, rely=0.290, height=40, width=522)
    Button1.configure(
        activebackground=_BUTTON_activebackgroundcolor, activeforeground=_foregroundcolorWHITE, background=_BUTTON_backgroundcolor,foreground=_foregroundcolorWHITE, cursor="hand2", font=_FONT_padrao, borderwidth=0,
        text='''CSSecurity - Validação''', command=localizar_images
    )
    
    
##############################################    Treeview    ######################################################################

    #criação Treeview
    tv= ttk.Treeview(root, columns = ('RM','nome','data','horario'), show='headings', takefocus=0)
    tv.place(relx=0.165, rely=0.368, height=278, width=510)
    tv.heading('RM', text ='RM')
    tv.heading('nome', text ='NOME E SÉRIE')
    tv.heading('data', text ='DATA')
    tv.heading('horario', text ='HORÁRIO', anchor="w")
    tv.column('RM', width=80, anchor="center")
    tv.column('nome', width=260)
    tv.column('data', width=102, anchor="center")
    tv.column('horario', width=72, anchor="center")

    #design Treeview
    styleTreeview = ttk.Style()
    styleTreeview.theme_use("clam")# Tema da treeview
    styleTreeview.configure("Treeview", 
        background=_TREEVIEW_backgroundcolor, fieldbackground=_TREEVIEW_backgroundcolor, foreground= _TREEVIEW_foregroundcolor, font=_FONT_insertTREEVIEW, rowheight="30", borderwidth="2"          
    )
    styleTreeview.map("Treeview", 
        background=[("selected",_TREEVIEW_selectedbackgroundcolor)], foreground=[("selected",_foregroundcolorWHITE)], font=[("selected",_FONT_selectedinsertTREEVIEW)],
    )

    #criação da scrollbar do Treeview
    scrollbar = ttk.Scrollbar(root, orient='vertical', command=tv.yview)
    scrollbar.place(x=635, y=245, height=278)
    tv.configure(yscrollcommand=scrollbar.set)

#########################################    Botão 2:  Área do Coordenador    ###############################################################
    
    #FUNÇÃO TRANSIÇÃO -> 'ÁREA DO COODERNADOR'
    def areaCoordenador():
        root.destroy()
        import area_coordenador as area_coordenador
        area_coordenador.janela2_ac()

    Button2 = tk.Button(root)
    Button2.place(relx=0.165, rely=0.8, height=40, width=522)
    Button2.configure(
        activebackground=_BUTTON_activebackgroundcolor, activeforeground=_foregroundcolorWHITE, background=_BUTTON_backgroundcolor,foreground=_foregroundcolorWHITE, cursor="hand2", font=_FONT_padrao, borderwidth=0,
        text='''Área do Coordenador''', command=areaCoordenador
    )

    root.mainloop()