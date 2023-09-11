#IMPORT LIBS
from Bibliotecas.imports import *

def janela3_registrar():

    root = tk.Tk()
    _fundoIMG = tk.PhotoImage(file="imgs/fundoCSSecurityRegistrar.png")
    _logoIMG = "imgs/logo.png"
    _BUTTON_activebackgroundcolor = "#C91818"
    _BUTTON_backgroundcolor = "#142643"
    _FUNDO_backgroundcolor = "#31529D"
    _foregroundcolorWHITE = "white"
    _ENTRY_backgroundcolor = "#a79fff"
    _ENTRY_insertbackgroundforegroundcolor = "#000833"
    _ENTRY_selectbackgroundcolor = "#5648ff"
    _FONT_padrao = "-family {Dubai Medium} -size 13"


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

    def senha():
        validacao_arqv("DadosGerais/")
        exists1 = os.path.isfile("DadosGerais\senha.txt")
        if exists1:
            tf = open("DadosGerais\senha.txt", "r")
            key = tf.read()
        else:
            new_pas = tsd.askstring('Senha antiga não encontrada', 'Por favor, digite uma nova senha abaixo', show='*')
            if new_pas == None:
                mess.showinfo(title='Nenhuma senha inserida', message='Senha não definida! Por favor, tente novamente')
            else:
                tf = open("DadosGerais\senha.txt", "w")
                tf.write(new_pas)
                mess.showinfo(title='Senha registrada', message='Nova senha registrada com sucesso!')
                return
        password = tsd.askstring('Senha', 'Digite a senha', show='*')
        if (password == key):
            detectar_face()
            mess.showinfo(title='Sucesso', message='Usuário cadastrado com sucesso!')
        elif (password == ''):
            mess.showerror(title='Erro', message='Senha não digitada!')
        else:
            mess.showerror(title='Erro', message='Você digitou a senha errada')

    def coleta_dados(path):
        # get the path of all the files in the folder
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        # create empth face list
        faces = []
        # create empty ID list
        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting it to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            ID = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(ID)
        return faces, Ids

    def detectar_face():
        checar_facepadrao()
        validacao_arqv("DadosGerais/")
        recognizer = cv2.face_LBPHFaceRecognizer.create()
        harcascadePath = "face_padrao.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        faces, ID = coleta_dados("FacesAlunos")
        try:
            recognizer.train(faces, np.array(ID))
        except:
            mess.showinfo(title='Sem registros', message='Por favor, registre alguém primeiro!')
            return
        recognizer.save("DadosGerais\pontos_faces.yml")
        res = "Perfil salvo com sucesso"

    def TakeImages(Entry1, Entry2):
        checar_facepadrao()
        columns = ['ID', '', 'RM', '', 'NOME']
        validacao_arqv("DadosAlunos/")
        validacao_arqv("FacesAlunos/")
        serial = 0
        exists = os.path.isfile("DadosAlunos\dados_alunos.csv")
        if exists:
            with open("DadosAlunos\dados_alunos.csv", 'r') as csvFile1:
                reader1 = csv.reader(csvFile1)
                for l in reader1:
                    serial = serial + 1
            serial = (serial // 2)
            csvFile1.close()
        else:
            with open("DadosAlunos\dados_alunos.csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(columns)
                serial = 1
            csvFile1.close()
        Id = (Entry1)
        name = (Entry2)
        if ((name.isalpha()) or (' ' in name)):
            cam = cv2.VideoCapture(0)
            harcascadePath = "face_padrao.xml"
            detector = cv2.CascadeClassifier(harcascadePath)
            sampleNum = 0
            while (True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    # incrementing sample number
                    sampleNum = sampleNum + 1
                    # saving the captured face in the dataset folder FacesAlunos
                    cv2.imwrite("FacesAlunos\ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                                gray[y:y + h, x:x + w])
                    # display the frame
                    cv2.imshow('Tirar Foto', img)
                # wait for 100 miliseconds
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                # break if the sample number is morethan 100
                elif sampleNum > 100:
                    break
            cam.release()
            cv2.destroyAllWindows()
            res = "Imagens tiradas para identificação : " + Id
            row = [serial, '', Id, '', name]
            with open('DadosAlunos\dados_alunos.csv', 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
        else:
            if (name.isalpha() == False):
                res = "Digite o nome correto"
                

######################################## JANELA 3 PROPRIEDADES ################################################

    root.geometry("450x600+458+40")
    root.minsize(450, 600)
    root.maxsize(450, 600)
    root.resizable(0,  0)
    root.title("CSSecurity - Registrar")

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

###############################################  Label 1: RA + Entry 1 #################################################################
    

    Label1 = tk.Label(root)
    Label1.place(relx=0.165, rely=0.247, height=20, width=310)
    Label1.configure(
        background=_FUNDO_backgroundcolor, foreground=_foregroundcolorWHITE,font=_FONT_padrao, 
        text='''RM'''
    )

    root.Entry1 = tk.Entry(root)
    root.Entry1.place(relx=0.165, rely=0.283, height=30, relwidth=0.689)
    root.Entry1.configure(
        background=_ENTRY_backgroundcolor, insertbackground=_ENTRY_insertbackgroundforegroundcolor, foreground=_ENTRY_insertbackgroundforegroundcolor, font=_FONT_padrao, selectbackground=_ENTRY_selectbackgroundcolor, selectforeground=_foregroundcolorWHITE, borderwidth=4, relief="flat",
    )
    

###############################################  Label 2: Nome e Curso + Entry 2 #################################################################

    Label2 = tk.Label(root)
    Label2.place(relx=0.165, rely=0.35, height=20, width=310)
    Label2.configure(
        background=_FUNDO_backgroundcolor, foreground=_foregroundcolorWHITE,font=_FONT_padrao, 
        text='''Nome e Curso'''
    )

    root.Entry2 = tk.Entry(root)
    root.Entry2.place(relx=0.165, rely=0.39, height=30, relwidth=0.689)
    root.Entry2.configure(
        background=_ENTRY_backgroundcolor, insertbackground=_ENTRY_insertbackgroundforegroundcolor, foreground=_ENTRY_insertbackgroundforegroundcolor, font=_FONT_padrao, selectbackground=_ENTRY_selectbackgroundcolor, selectforeground=_foregroundcolorWHITE,  borderwidth=4, relief="flat",
    )

##################################    Label 3:   1 - Tirar Foto  2 - Salvar Perfil    #############################################################################################################        

    Label3 = tk.Label(root)
    Label3.place(relx=0.165, rely=0.51, height=20, width=310)
    Label3.configure(
        background=_FUNDO_backgroundcolor, foreground=_foregroundcolorWHITE,font=_FONT_padrao, 
        text='''1 - Tirar Foto  2 - Salvar Perfil'''
    )

######################################    Botao 1: Tirar foto + Botao 2: Salvar Perfil      ########################################################################################
    
    Button1 = tk.Button(root)
    Button1.place(relx=0.165, rely=0.605, height=30, width=310)
    Button1.configure(
        activebackground=_BUTTON_activebackgroundcolor, activeforeground=_foregroundcolorWHITE, background=_BUTTON_backgroundcolor,foreground=_foregroundcolorWHITE, cursor="hand2", font=_FONT_padrao, borderwidth=0,
        text='''Tirar Foto''', command=lambda:TakeImages(root.Entry1.get(), root.Entry2.get())
    )

    Button2 = tk.Button(root)
    Button2.place(relx=0.165, rely=0.668, height=30, width=310)
    Button2.configure(
        activebackground=_BUTTON_activebackgroundcolor, activeforeground=_foregroundcolorWHITE, background=_BUTTON_backgroundcolor,foreground=_foregroundcolorWHITE, cursor="hand2", font=_FONT_padrao, borderwidth=0,
        text='''Salvar Perfil''', command=senha
    )
###############################  Botao 3: Voltar ################################################################################################
    
    #FUNÇÃO VOLTAR PARA JANELA 'CONSULTAR DADOS'
    def areaCoordenador():
        root.destroy()
        import area_coordenador as area_coordenador
        area_coordenador.janela2_ac()

    Button3 = tk.Button(root)
    Button3.place(relx=0.165, rely=0.79, height=30, width=310)
    Button3.configure(
        activebackground=_BUTTON_activebackgroundcolor, activeforeground=_foregroundcolorWHITE, background=_BUTTON_backgroundcolor,foreground=_foregroundcolorWHITE, cursor="hand2", font=_FONT_padrao, borderwidth=0,
        text='''Voltar''', command=areaCoordenador
    )

    root.mainloop()