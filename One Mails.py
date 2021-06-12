# Copyright © SAMI, SAMUEL IBOU MARONE
# Programme ONE Mails (Logicel d'envoie plus simple  email)
# Envoi des emails depuis une adresse mail GMAIL sur d'autre mails avec beaucoup d'options et de facilité

# Samuel Ibou Marone // @SAMI, @THe_CHoOSen_One // @SAMI, @ThE_HAckEr_One
# @ SAMI ©

# -------------------------------------------------------------------- #
#                              @ One Mails                             #
#                               @ By S@MI                              #
#                    @ SAMIUEL IBOU MARONE  // Sept 2018               #
# -------------------------------------------------------------------- #


from tkinter import *
import tkinter.ttk as ttk
from tkinter.filedialog import *
from tkinter.messagebox import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import re, webbrowser, random

class OneMails():
    def __init__(self):
        self.CODE = ['\t', '²','~','\n',' ', 'i', 'U','§','j', '[','©', '}','k', '(','P', 'l', ']','D', 'm', 'S', 'n', 'o', '-', '|', '&', 'p', 'q', 'C','{', 'a', 'b', 'c', 'd', 'e','E', 'H', 'F','_', 'é', 'ç', 'ê','ô', 'â', 'J', 'K', '8', 'L', '^', 'M', '\'', 'N','\"', 'O', 'Y', 'Z', 'f', 'g', 'h', 'r', 's', 't', 'u', 'v', 'w', 'x', '0', 'y', 'z' , '1', '2','A', '4', 'W', '5','G', '6', 'I','7', ",", '@', '!', '.', '?', ';', ':', '/', "'", '*', '+', 'T', '3', 'V', 'B', '#', 'Q', 'R', 'X', ')', 'î', '9']
        random.shuffle(self.CODE, random=lambda:0.6991)
        
        self.Francais = {'ID':'Identifiant', 'MP':'Mot de Passe', 'AffiMasqMP':'Afficher / Masquer Mp', 'EnregIDMP':'Enregistrer Id & Mp', \
        'ConnAuto':'Connexion Automatique', 'ConnecterVous':'Veuillez vous Connecter à votre adresse Gmail !', 'Valider':'Valider', 'Fenetre':'FENETRE',\
        'Quitter':'Quitter', 'OptionUnlessSec':'Verifier Options Unless Secure Compte Gmail', 'InfoUtil':'Informations d\'utilisation','SelectContacte':'Selectionner un Contacte', 'InfoApp':'Infos App',\
        'Contacter':'Contacter', 'TextMeContacter':'EN CAS DE BUG OU D\'ERREUR DE FONCTIONNEMENT  OU DE CONSEILLE D\'AMELIORATION\n\nVOUS POUVER CONTACTER L\'AUTEUR VIA CET EMAIL: \n\nEMAIL: hiservicesone@gmail.com\n\nCopyright © S MARONE',\
        'TitreMeContacter':'ME CONTACTER', 'TitreInfoApp':'INFORMATION', 'TextInfoApp':'ONE MAILS EST UN LOGICIEL QUI FACILITE L\'ENVOIE DE COURRIER (EMAIL) A PARTIR DE COMPTE GMAIL. TOUTES LES OPERATIONS SE FAISANT SUR L\'APPLICATION DEPUIS LA CONNEXION DU COMPTE GMAIL A L\'ENVOIE DU COURRIER !!! \n\nCopyright © S MARONE', \
        'TitreUnlessSecu':'OPTION UNLESS SECURE', 'TextUnlessSecu':'CETTE OPTION DOIT ETRE ACTIVE POUR QUE L\'ENVOIE EMAILS AVEC VOTRE ADRESSE MAIL GMAIL SOIT POSSIBLE\nUNE PAGE WEB VA SOUVRIR SUR LE LIEN POUR L\'ACTIVER \n\nCopyright © S MARONE!!!', \
        'TitreChampsVides':'CHAMPS VIDES', 'TextChampsVides':'VEUILLEZ REMPLIR LE(S) CHAMP(S) VIDE(ENT) EN RENSEIGNANT VOTRE ADRESSE MAIL GMAIL ET LE MOT DE PASSE !!!', \
        'TitreErreurAdr':'ERREUR ADRESSE MAIL', 'TextErreurAdr':'L\'ADDRESE MAIL RENSEIGNÉ N\'EST PAS VALIDE !!!','TitreErreurID':'ERREUR IDENTIFIANT',\
        'TextErreurID':'IDENTIFIANT OU MOT DE PASSE INCORRECTE !!!', 'InfoUtilOneMail':'INFORMATION D\'UTILISATION DE ONE MAILS',\
        'AffichListPieceJointe':'Afficher Liste Piece Jointe', 'EngAdrContacte':'Enregistrer les adresses mails dans contact', 'Deconnecter':'Se Déconnecter', \
        'TitreNonNumeric':'ERREUR VALEUR', 'TextNonNumeric':'LA VALEUR SAISIE  N\'EST PAS NUMERIC !!!', 'TitreValeurNonPrisEnCompte':'NON PRIS EN COMPTE', \
        'TextValeurNonPrisEnCompte':'LA VALEUR SAISIE N\'EST PAS PRISE EN COMPTE', 'TitreEmailDejaAjoute':'EMAIL DEJA AJOUTÉ', 'TextEmailDejaAjoute':'CETTE ADRESSE MAIL EST DÉJA AJOUTER AVEC SUCCES A LA LISTE DES DESTINATAIRE', \
        'TitreErreurAccesInternet':'ERREUR ACCES INTERNET', 'TextErreurAccesInternet':'NOUS NE PARVENONS PAS A ACCEDER A INTERNET, PAS DE CONNEXION INTERNET', \
        'Reglages':'Réglages', 'AffichLangue':'Langue d\'affichage', 'LangueFrancais':'Français', 'LangueAnglais':'Anglais', 'Appliquer':'Appliquer'

        }

        self.Anglais = {'ID':'  Login', 'MP':'Password', 'AffiMasqMP':'Show / Hide Password', 'EnregIDMP':'Save Id & Password', 'ConnAuto':'Automatic Connection', \
        'ConnecterVous':'Please login to your Gmail address!', 'Valider':'Validate', 'Fenetre':'WINDOW', 'Quitter':'Leave','SelectContacte':'Select a Contact', \
        'OptionUnlessSec':'Check Unless Secure Options  on your Gmail Account','InfoUtil':'Usage information', 'InfoApp':'App Infos', 'Contacter':'Contact', \
        'TextMeContacter':'IN CASE OF BUG OR ERROR OF OPERATION OR IMPROVEMENT ADVICE\n\nYOU CAN CONTACT THE AUTHOR TO THIS EMAIL:\n\nEMAIL: hiservicesone@gmail.com\n\nCopyright © S MARONE ', \
        'TitreMeContacter':'CONTACT ME', 'TitreInfoApp':'INFORMATION', 'TextInfoApp':'ONE MAILS IS A SOFTWARE THAT FACILITATES MAIL SENDING FROM GMAIL ACCOUNT. ALL THE OPERATIONS BEING ON THE APPLICATION SINCE THE CONNECTION OF THE GMAIL ACCOUNT TO THE SENDING OF THE MAIL !!!\n\nCopyright © S MARONE', \
        'TitreUnlessSecu':'UNLESS SECURE OPTION', 'TextUnlessSecu':'THIS OPTION MUST BE ACTIVATED SO THAT SEND MAILS WITH YOUR ADDRESS MAIL GMAIL IS POSSIBLE \nA WEB PAGE WILL REMEMBER ON THE LINK TO ENABLE IT \n\nCopyright © S MARONE !!! ', \
        'TitreChampsVides':'EMPTY FIELDS', 'TextChampsVides':'PLEASE COMPLETE THE EMPTY FIELD (S) BY INFORMING YOUR ADDRESS MAIL GMAIL AND PASSWORD !!!', \
        'TitreErreurAdr':'ERROR ADDRESS MAIL', 'TextErreurAdr':'INQUIRED MAIL ADDRESS IS NOT VALID !!!','TitreErreurID':'ERROR LOGIN',\
        'TextErreurID':'WRONG IDENTIFIER OR PASSWORD INCORRECT !!!', 'InfoUtilOneMail':'USE INFORMATION OF ONE MAILS', \
        'AffichListPieceJointe':'Show list attachment', 'EngAdrContacte':'Save email addresses in contact', 'Deconnecter':'Sign out', 'TitreNonNumeric':'ERROR VALUE', \
        'TextNonNumeric':'THE VALUE WRITTEN IS NOT NUMERIC VALUE', 'TitreValeurNonPrisEnCompte':'NOT TAKEN INTO ACCOUNT', \
        'TextValeurNonPrisEnCompte':'THE SEIZED VALUE IS NOT TAKEN INTO ACCOUNT', 'TitreEmailDajaAjoute':'EMAIL ALREADY ADDED', 'TextEmailDejaAjoute':'THIS ADDRESS MAIL IS ALREADY ADDED TO THE LIST OF RECIPIENTS',\
        'TitreErreurAccesInternet':'ERROR INTERNET ACCESS', 'TextErreurAccesInternet':'WE DO NOT GO TO ACCESS THE INTERNET, NO INTERNET CONNECTION', 'Reglages':'Settings',\
        'AffichLangue':'Display Language', 'LangueFrancais':'French', 'LangueAnglais':'English', 'Appliquer':'Apply'

        }
        
        self.Langue = self.Francais
        try:
            with open('OM.mrn', 'r') as f:
                self.Liste = f.read()
        except:
            with open('OM.mrn', 'x') as f:
                f.close()
            self.Liste = ''
        try:
            with open('One.dll', 'r') as f:
                self.Premiereutilisation = 1
        except:
            with open('One.dll', 'x') as f:
                f.close
            self.Premiereutilisation = 0
        with open('Connexion.dll', 'r') as f:
            self.EtatCon = self.decryptbin(f.read())
        
        if self.Liste != '':
            self.Liste = self.decryptbin(self.Liste).split('\n')
            
        self.fen = Tk()
        self.fen.title('ONE MAILS')
        self.fen.iconbitmap('Images\OneMails.ico')
        self.fen.resizable(width=False, height=False)
        self.fen.geometry('500x285+400+100')
        self.fen.config(bg='light sea green')
            
        self.menubar = Menu(self.fen)
            
        self.menu1 = Menu(self.menubar, tearoff=0)
        self.menu1.add_command(label='%s' % self.Langue['Quitter'], command=self.fen.destroy)
        self.menubar.add_cascade(label='%s' % self.Langue['Fenetre'], menu=self.menu1)

        self.menu2 = Menu(self.menubar, tearoff=0)
        self.menu2.add_command(label='%s' % self.Langue['OptionUnlessSec'], command=self.OptionUnlessSecure)
        self.menu2.add_command(label='%s' % self.Langue['InfoUtil'], command=self.PremiereUtilisation)
        self.menu2.add_command(label='%s' % self.Langue['Reglages'], command=self.Reglages)
        self.menubar.add_cascade(label='OPTIONS', menu=self.menu2)
            
        menu3 = Menu(self.menubar, tearoff=0)
        menu3.add_command(label='%s' % self.Langue['InfoApp'], command=self.Infos)
        menu3.add_separator()
        menu3.add_command(label='%s' % self.Langue['Contacter'], command=self.Contact)
        self.menubar.add_cascade(label='?', menu=menu3)

        self.fen.config(menu=self.menubar)
            
        photo1 = PhotoImage(file='Images\OneMails.png')
        item1 = Label(self.fen, image=photo1, bg='light sea green')
        item1.photo = photo1
        item1.pack()

        if self.EtatCon == '1':
            with open('UtCon.dll', 'r') as f:
                self.ValConnex = f.read()
            self.fen.bind("<Key>", self.clavierValider)
            self.Valider()
            self.fen.mainloop()
        else:
            self.fram0 = Frame(self.fen, bg='light sea green')
            self.fram0.pack()
            
            Label(self.fram0, text='     %s :' % self.Langue['ID'], font='calibri 12 bold italic', bg='light sea green').pack(side=LEFT, padx=5)
            self.entrut = Entry(self.fram0, font='calibri 12 bold italic', width=30, bg='bisque')
            self.entrut.pack()

            self.fram00 = Frame(self.fen, bg='light sea green')
            self.fram00.pack()
            
            Label(self.fram00, text='%s :'% self.Langue['MP'], font='calibri 12 bold italic', bg='light sea green').pack(side=LEFT, padx=5)
            self.entrmp = Entry(self.fram00, font='calibri 12 bold italic',width=30, bg='bisque', show='*')
            self.entrmp.pack(side=LEFT, pady=5)

            if self.Liste != []:
                try:
                    self.entrut.insert(0, self.Liste[0])
                    self.entrmp.insert(0, self.Liste[1])
                except:
                    rien = ''
                
            self.fram001 = Frame(self.fen, bg='light sea green')
            self.fram001.pack()
            self.value = IntVar()
            self.value1 = IntVar()
            self.value2 = IntVar()
            Checkbutton(self.fram001, text='%s'% self.Langue['AffiMasqMP'], font='normal 8 italic bold', variable=self.value, onvalue=1,command=self.affmasqu, offvalue=0, bg='light sea green').pack(side=LEFT, padx=5)
            Checkbutton(self.fram001, text='%s' % self.Langue['EnregIDMP'], font='normal 8 italic bold', variable=self.value1, onvalue=1, offvalue=0, bg='light sea green').pack(side=LEFT)
            Checkbutton(self.fram001, text='%s' % self.Langue['ConnAuto'], font='normal 8 italic bold', variable=self.value2, onvalue=1, offvalue=0, bg='light sea green').pack(side=LEFT)

            self.fram000 = Frame(self.fen, bg='light sea green')
            self.fram000.pack(fill=X)
            self.lab0 = Label(self.fram000,  text='%s' % self.Langue['ConnecterVous'], font='calibri 11 bold italic',fg='red', bg='light sea green')
            self.lab0.pack(pady=10, side=RIGHT)
            
            self.boutval = Button(self.fen, text='%s' % self.Langue['Valider'], font='calibri 12 italic bold', command=self.Valider, bg='bisque')
            self.boutval.pack(pady=5, side=BOTTOM)

            if self.Premiereutilisation == 0:
                self.PremiereUtilisation()

            self.fen.bind("<Key>", self.clavierValider)
            self.fen.mainloop()

    def Valider(self):
        if self.EtatCon == '1':
            self.adrmail = self.decryptbin(self.ValConnex).split('Space')[0]
            self.mp = self.decryptbin(self.ValConnex).split('Space')[1]
        else:
            self.adrmail = self.entrut.get()
            self.mp = self.entrmp.get()
        if self.adrmail == '' or self.mp == '':
            showinfo('%s' % self.Langue['TitreChampsVides'], '%s' % self.Langue['TextChampsVides'])
        elif self.adrmail[-10:] != '@gmail.com':
            showinfo('%s' % self.Langue['TitreErreurAdr'],'%s' % self.Langue['TextErreurAdr'])
            self.entrut.delete(1000000)
        else:
            try:
                self.server = smtplib.SMTP('smtp.gmail.com', 587)
            except:
                showinfo('%s' % self.Langue['TitreErreurAccesInternet'], '%s' % self.Langue['TextErreurAccesInternet'])
                self.SeDeconnecter()
            else:
                self.server.starttls()
                try:
                    self.server.login(self.adrmail, self.mp)
                except smtplib.SMTPAuthenticationError:
                    showinfo('%s' % self.Langue['TitreErreurID'], '%s' % self.Langue['TextErreurID'])
                    self.entrmp.delete(1000000)
                else:
                    valval = self.adrmail + '\n' + self.mp
                    if self.EtatCon != '1':
                        if self.value1.get() == 1:
                            try:
                                with open('OM.mrn', 'x') as f:
                                    f.write(self.cryptbin(valval))
                            except:
                                with open('OM.mrn', 'w') as f:
                                    f.write(self.cryptbin(valval))
                        else:
                            try:
                                with open('OM.mrn', 'w') as f:
                                    f.write('')
                            except:
                                with open('OM.mrn', 'x') as f:
                                    f.write('')
                        
                        if self.value2.get() == 1:
                            try:
                                with open('Connexion.dll', 'w') as f:
                                    f.write(self.cryptbin('1'))
                            except :
                                with open('Connexion.dll', 'x') as f:
                                    f.write(self.cryptbin('1'))
                            try:    
                                with open('UtCon.dll', 'w') as f:
                                    f.write(self.cryptbin(self.adrmail+'Space'+self.mp))
                            except:
                                with open('UtCon.dll', 'x') as f:
                                    f.write(self.cryptbin(self.adrmail+'Space'+self.mp))
                        else:
                            try:
                                with open('Connexion.dll', 'w') as f:
                                    f.write(self.cryptbin('0'))
                            except :
                                with open('Connexion.dll', 'x') as f:
                                    f.write(self.cryptbin('0'))
                    self.EnvMail()
                    self.fen.unbind('<Key>')

    def SeDeconnecter(self):
        try:
            self.server.quit()
        except:
            rien = ''
        try:
            self.fram0.destroy()
        except:
            rien = ''
        try:
            self.fram01.destroy()
        except:
            rien = ''
        try:
            self.fram00.destroy()
        except:
            rien = ''
        try:
            self.fram001.destroy()
        except:
            rien = ''
        try:
            self.fram000.destroy()
        except:
            rien = ''
        try:
            self.fram0000.destroy()
        except:
            rien = ''
        try:
            self.fram00000.destroy()
        except:
            rien = ''   
        try:
            self.BoutEnv.destroy()
        except:
            rien = ''
        if self.EtatCon == '1':
            try:
                with open('Connexion.dll', 'x') as f:
                    f.witre(self.cryptbin('0'))
            except :
                with open('Connexion.dll', 'w') as f:
                    f.write(self.cryptbin('0'))
        try:
            with open('OM.mrn', 'r') as f:
                self.Liste = f.read()
        except:
            with open('OM.mrn', 'x') as f:
                f.close()
            self.Liste = ''

        if self.Liste != '':
            self.Liste = self.decryptbin(self.Liste).split('\n')
        
        self.fen.geometry('500x285+400+100')

        self.menubar = Menu(self.fen)
            
        self.menu1 = Menu(self.menubar, tearoff=0)
        self.menu1.add_command(label='%s' % self.Langue['Quitter'], command=self.fen.destroy)
        self.menubar.add_cascade(label='%s' % self.Langue['Fenetre'], menu=self.menu1)

        self.menu2 = Menu(self.menubar, tearoff=0)
        self.menu2.add_command(label='%s' % self.Langue['OptionUnlessSec'], command=self.OptionUnlessSecure)
        self.menu2.add_command(label='%s' % self.Langue['InfoUtil'], command=self.PremiereUtilisation)
        self.menu2.add_command(label='%s' % self.Langue['Reglages'], command=self.Reglages)
        self.menubar.add_cascade(label='OPTIONS', menu=self.menu2)
            
        menu3 = Menu(self.menubar, tearoff=0)
        menu3.add_command(label='%s' % self.Langue['InfoApp'], command=self.Infos)
        menu3.add_separator()
        menu3.add_command(label='%s' % self.Langue['Contacter'], command=self.Contact)
        self.menubar.add_cascade(label='?', menu=menu3)

        self.fen.config(menu=self.menubar)

        self.fram0 = Frame(self.fen, bg='light sea green')
        self.fram0.pack()
            
        Label(self.fram0, text='     %s :' % self.Langue['ID'], font='calibri 12 bold italic', bg='light sea green').pack(side=LEFT, padx=5)
        self.entrut = Entry(self.fram0, font='calibri 12 bold italic', width=30, bg='bisque')
        self.entrut.pack()

        self.fram00 = Frame(self.fen, bg='light sea green')
        self.fram00.pack()
            
        Label(self.fram00, text='%s :'% self.Langue['MP'], font='calibri 12 bold italic', bg='light sea green').pack(side=LEFT, padx=5)
        self.entrmp = Entry(self.fram00, font='calibri 12 bold italic',width=30, bg='bisque', show='*')
        self.entrmp.pack(side=LEFT, pady=5)

        if self.Liste != []:
            try:
                self.entrut.insert(0, self.Liste[0])
                self.entrmp.insert(0, self.Liste[1])
            except:
                rien = ''
            
        self.fram001 = Frame(self.fen, bg='light sea green')
        self.fram001.pack()
        self.value = IntVar()
        self.value1 = IntVar()
        self.value2 = IntVar()
        Checkbutton(self.fram001, text='%s'% self.Langue['AffiMasqMP'], font='normal 8 italic bold', variable=self.value, onvalue=1,command=self.affmasqu, offvalue=0, bg='light sea green').pack(side=LEFT, padx=5)
        Checkbutton(self.fram001, text='%s' % self.Langue['EnregIDMP'], font='normal 8 italic bold', variable=self.value1, onvalue=1, offvalue=0, bg='light sea green').pack(side=LEFT)
        Checkbutton(self.fram001, text='%s' % self.Langue['ConnAuto'], font='normal 8 italic bold', variable=self.value2, onvalue=1, offvalue=0, bg='light sea green').pack(side=LEFT)

        self.fram000 = Frame(self.fen, bg='light sea green')
        self.fram000.pack(fill=X)
        self.lab0 = Label(self.fram000,  text='%s' % self.Langue['ConnecterVous'], font='calibri 11 bold italic',fg='red', bg='light sea green')
        self.lab0.pack(pady=10, side=RIGHT)
            
        self.boutval = Button(self.fen, text='%s' % self.Langue['Valider'], font='calibri 12 italic bold', command=self.Valider, bg='bisque')
        self.boutval.pack(pady=5, side=BOTTOM)
                
    def clavierValider(self, event):
        touche = event.keysym
        if touche == "Return":
            self.Valider()
    
    def affmasqu(self):
        if self.value.get() == 0 :
            self.entrmp.config(show='*')
        else:
            self.entrmp.config(show='')

    def Contact(self):
        showinfo('%s' % self.Langue['TitreMeContacter'], '%s' % self.Langue['TextMeContacter'])
                        
    def OptionUnlessSecure(self):
        showinfo('%s' % self.Langue['TitreUnlessSecu'], '%s' % self.Langue['TextUnlessSecu'])
        webbrowser.open('https://myaccount.google.com/lesssecureapps')

    def Infos(self):
        showinfo('%s' % self.Langue['TitreInfoApp'], '%s' % self.Langue['TextInfoApp'])
                        
    def PremiereUtilisation(self):
        self.fen1 = Toplevel(self.fen)
        self.fen1.grab_set()
        self.fen1.focus_set()
        self.fen1.geometry("800x400+300+50")  
        self.fen1.title('%s' % self.Langue['InfoUtilOneMail'])
        self.fen1.iconbitmap('Images/Icone.ico') 
        self.fen.config(bg='light sea green')
        self.fen1.resizable(width=False, height=False)

        scrollbar = Scrollbar(self.fen1)
        scrollbar.pack(side=RIGHT, fill=Y, anchor='ne')

        scrollbar1 = Scrollbar(self.fen1, orient=HORIZONTAL)
        scrollbar1.pack(side=BOTTOM, fill=X)

        self.Texte = Text(self.fen1, font='calibri 12  bold italic',  wrap='none')
        self.Texte.pack(fill=BOTH)

        scrollbar.configure(command=self.Texte.yview)
        scrollbar1.configure(command=self.Texte.xview)
        self.Texte['yscrollcommand'] = scrollbar.set
        self.Texte['xscrollcommand'] = scrollbar1.set

        with open('Doc.mrn', 'r') as f:
            Tex = self.decryptbin(f.read())
        self.Texte.insert(END, Tex)
        self.Texte.config(state=DISABLED, wrap='word' )
        
    def EnvMail(self):
        self.menu2.add_command(label='%s' % self.Langue['AffichListPieceJointe'], command=self.AfficheListePieceJointe)
        self.menu2.add_command(label='%s' % self.Langue['EngAdrContacte'], command=self.EnregistrerContact)
        self.menu2.add_command(label='%s' % self.Langue['SelectContacte'], command=self.SelectionnerContacte)
        self.menu1.add_command(label='%s' % self.Langue['Deconnecter'], command=self.SeDeconnecter)
        self.fen.config(menu=self.menubar)
        
        self.ListeTaillePolice = [ '12'] #['8', '9', '10','11', '12','13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',\
                                   #'30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50']
        self.ListePolice = ['Calibri']#['Algerian', 'Arial', 'Calibri', 'Garamond', 'Georgia', 'Helvetica', 'Tahoma', 'Times', 'Verdana', 'Sans-serif']
        self.valeurPolice  = self.ListePolice[0]
        self.valeurtaillepolice = self.ListeTaillePolice[0]
        self.valeurgras = ''
        self.valeuritalic = ''
        self.valeursouligner = ''
        self.EnregistrerContact = 0
    
        self.choixsouligner = 11
        self.ListeMail_Ajoute = []
        self.ListePieceJointe_Ajoute = []
        self.NomPieceJointe = []
        self.fen.geometry('700x535+350+100')
        try:
            self.fram0.destroy()
        except:
            rien = ''
        try:
            self.fram00.destroy()
        except:
            rien = ''
        try:
            self.fram001.destroy()
        except:
            rien = ''
        try:
            self.fram000.destroy()
        except:
            rien = ''
        try:    
            self.boutval.destroy()
        except:
            rien = ''
        
        self.fram0 = Frame(self.fen, bg='light sea green')
        self.fram0.pack(anchor='nw')
        Label(self.fram0, text='          Destinataire :', font='calibri 12 bold italic', bg='light sea green').pack(side=LEFT, padx=5)
        self.entredes = Entry(self.fram0, width=60, font='calibri 12 bold italic', bg='bisque')
        self.entredes.pack(side=LEFT, padx=5)
        Button(self.fram0, text='Ajouter', fg='red', font='calibri 10 italic bold', bg='bisque',command=self.Ajdestinataire).pack(side=LEFT)
        self.fram01 = Frame(self.fen, bg='light sea green')
        self.fram01.pack()
        Label(self.fram01, text='Ajouté : ', font='calibri 10 bold italic', fg='red', bg='light sea green').pack(side=LEFT, pady=5)
        self.labo = Frame(self.fram01, bg='light sea green')
        self.labo.pack(side=LEFT, padx=3)
        
        self.fram00 = Frame(self.fen, bg='light sea green')
        self.fram00.pack(anchor='nw')
        Label(self.fram00, text='                     Objet :', font='calibri 12 bold italic', bg='light sea green').pack(side=LEFT, padx=5)
        self.entreobj = Entry(self.fram00, width=60, font='calibri 12 bold italic', bg='bisque')
        self.entreobj.pack(side=LEFT, padx=5)
        
        self.fram000 = Frame(self.fen, bg='light sea green')
        self.fram000.pack(anchor='nw', pady=5)

        self.valcheck = IntVar(value=0)
        self.check = Checkbutton(self.fram000, font='calibri 12 bold italic', bg='light sea green', onvalue=1, offvalue=0, variable=self.valcheck, command=self.optboutajPJ)
        self.check.pack(side=LEFT, padx=5)
        Label(self.fram000, text='Pieces Jointe :', font='calibri 12 bold italic', bg='light sea green').pack(side=LEFT)
        self.frem = Frame(self.fram000, bg='light sea green')
        self.frem.pack(side=LEFT)
        self.Labframfram = Frame(self.fram000, bg='light sea green')
        self.Labframfram.pack(pady=5, side=RIGHT)
        
        self.fram0000 = LabelFrame(self.fen, relief=GROOVE)
        self.fram0000.pack(anchor='nw', padx=60)
        
        self.valbold = IntVar(value=11)
        self.valitalic = IntVar(value=11)
        self.valsouligner = IntVar(value=11)

        fram00001 = Frame(self.fram0000)
        fram00001.pack(side=LEFT)
        self.ChoixPolice = ttk.Combobox(fram00001, values=self.ListePolice, width=10, font='Calibri 12 bold')
        self.ChoixPolice.set('Calibri')
        self.ChoixPolice.config(state='readonly')
        self.ChoixPolice.pack()
        
        fram00002 = Frame(self.fram0000)
        fram00002.pack(side=LEFT)
        self.ChoixTaillePolice = ttk.Combobox(fram00002, values=self.ListeTaillePolice, width=5, font='Calibri 12 bold')
        self.ChoixTaillePolice.set('12')
        self.ChoixTaillePolice.config(state='readonly')
        self.ChoixTaillePolice.pack()
        
        fram00003 = Frame(self.fram0000, bg='light sea green')
        fram00003.pack(side=LEFT)
        Radiobutton(fram00003, text='B',font='times 12 bold', variable=self.valbold, value=1,command=self.bold, indicatoron=0, selectcolor='bisque').pack(side=LEFT)
        Radiobutton(fram00003, text='B',font='times 12 bold', variable=self.valbold, value=11,command=self.bold, indicatoron=0, selectcolor='red').pack(side=LEFT)

        fram00004 = Frame(self.fram0000, bg='light sea green')
        fram00004.pack(side=LEFT)
        Radiobutton(fram00004, text='I',font='times 12 italic', variable=self.valitalic, value=1,command=self.italic, indicatoron=0, selectcolor='bisque', padx=5).pack(side=LEFT)
        Radiobutton(fram00004, text='I',font='times 12 italic', variable=self.valitalic, value=11,command=self.italic, indicatoron=0, selectcolor='red', padx=5).pack(side=LEFT)

        fram00005 = Frame(self.fram0000, bg='light sea green')
        fram00005.pack(side=LEFT)
        Radiobutton(fram00005, text='U',font='times 12 underline', variable=self.valsouligner, value=1,command=self.souligner, indicatoron=0, selectcolor='bisque').pack(side=LEFT)
        Radiobutton(fram00005, text='U',font='times 12 underline', variable=self.valsouligner, value=11,command=self.souligner, indicatoron=0, selectcolor='red').pack(side=LEFT)
       
        self.fram00000 = Frame(self.fen, bg='light sea green')
        self.fram00000.pack()
        scrollbar = Scrollbar(self.fram00000)
        scrollbar.pack(side=RIGHT, fill=Y, anchor='ne')
        self.Message = Text(self.fram00000, font='%s %s %s %s %s' %(self.valeurPolice, self.valeurtaillepolice, self.valeurgras, self.valeuritalic, self.valeursouligner ),\
                            bg='bisque', width=70, height=11)
        self.Message.pack()
        self.Message.pack_propagate(False)

        scrollbar.configure(command=self.Message.yview)
        self.Message['yscrollcommand'] = scrollbar.set
            
        self.BoutEnv = Button(self.fen, text='Envoyer', font='calibri 12 bold italic', fg='red', bg='bisque', padx=2, command=self.Envoyer)
        self.BoutEnv.pack(anchor='nw', padx=100, pady=5)

    def EnregistrerContact(self):
        if self.EnregistrerContact == 0:
            self.EnregistrerContact = 1
            showinfo('ACTIVÉ', 'ENREGISTREMENT DES CONTACTS ACTIVÉ !!!')
        else:
            if askyesno('DÉJA ECTIVÉ', 'CETTE OPTION EST DÉJA ACTIVÉE. VOULEZ VOUS LE DESACTIVER !!!'):
                self.EnregistrerContact = 0
                showinfo('DESACTIVÉE','OPTION DESACTIVÉE !!!')

    def SelectionnerContacte(self):
        self.fen1 = Toplevel(self.fen)
        self.fen1.grab_set()
        self.fen1.focus_set()
        self.fen1.geometry("400x300+350+10")  
        self.fen1.title('One MAILS Selection de Contact')
        self.fen1.iconbitmap('Images\Icone.ico') 
        self.fen1.config(bg='light sea green')
        self.fen1.resizable(height=False, width=False)

        with open('Contact.dll', 'r') as f:
            self.ListeContact = f.read()

        form = Frame(self.fen1, bg='light sea green')
        form.pack()
        scrollbar = Scrollbar(form)
        scrollbar.pack(side=RIGHT, fill=Y, anchor='ne')
        scrollbar1 = Scrollbar(form, orient=HORIZONTAL)
        scrollbar1.pack(side=BOTTOM, fill=X)

        self.Texte = Text(form, font='calibri 12 italic', height=10, width=50, wrap='none')
        self.Texte.pack()
        self.Texte.pack_propagate(False)

        scrollbar.configure(command=self.Texte.yview)
        scrollbar1.configure(command=self.Texte.xview)
        self.Texte['yscrollcommand'] = scrollbar.set
        self.Texte['xscrollcommand'] = scrollbar1.set

        self.ListeContact = self.ListeContact.split('\n')
        try:
            self.ListeContact.remove('')
        except:
            rien = ''
        for i in self.ListeContact:
            self.Texte.insert(END, '%s : %s \n' % (self.ListeContact.index(i), i))

        self.EntryChoixContact = Entry(self.fen1, width=10, bg='bisque', font='calibri 12 bold italic')
        self.EntryChoixContact.pack(pady=10)

        Button(self.fen1, text='%s' % self.Langue['Valider'], font='calibri 12 bold italic', bg='bisque', command=self.ValiderAjoutContact).pack(pady=10)

        self.fen1.bind('<Key>', self.ClavierValiderAjoutContact)
        
    def ValiderAjoutContact(self):
        if self.EntryChoixContact.get() == '':
            showinfo('%s' % self.Langue['TitreChampsVides'],'%s' % self.Langue['TextChampsVides'])
        elif self.EntryChoixContact.get().isdigit() == False:
            showinfo('%s' % self.Langue['TitreNonNumeric'], '%s' % self.Langue['TextNonNumeric'])
        elif int(self.EntryChoixContact.get()) > len(self.ListeContact) - 1 or int(self.EntryChoixContact.get()) < 0:
            showinfo('%s' % self.Langue['TitreValeurNonPrisEnCompte'], '%s' % self.Langue['TextValeurNonPrisEnCompte'])
        else:
            if self.ListeContact[(int(self.EntryChoixContact.get()))] in self.ListeMail_Ajoute:
                showinfo('%s' % self.Langue['TitreEmailDajaAjoute'], '%s' % self.Langue['TextEmailDejaAjoute'])
            else:
                self.ListeMail_Ajoute.append(self.ListeContact[(int(self.EntryChoixContact.get()))])
                Labfram = LabelFrame(self.labo, bg='light sea green')
                Labfram.pack(side=LEFT)
                Label(Labfram, text=self.ListeContact[(int(self.EntryChoixContact.get()))], font='calibri 10 bold italic', fg='green').pack()
            if len(self.ListeMail_Ajoute) == 1:
                self.boutboutbout = Button(self.fram01, text='X*',fg='red', command=self.laabo)
                self.boutboutbout.pack(side=RIGHT)
            self.fen1.destroy()

    def ClavierValiderAjoutContact(self, event):
        touche = event.keysym
        if touche == "Return":
            self.ValiderAjoutContact()

    def Reglages(self):
        self.fen1 = Toplevel(self.fen)
        self.fen1.grab_set()
        self.fen1.focus_set()
        self.fen1.geometry("400x300+350+10")  
        self.fen1.title('One MAILS %s' % self.Langue['Reglages'])
        self.fen1.iconbitmap('Images\Icone.ico') 
        self.fen1.config(bg='light sea green')
        self.fen1.resizable(height=False, width=False)

        Langues = [self.Langue['LangueFrancais'], self.Langue['LangueAnglais']]
        fram = LabelFrame(self.fen1, bg='light sea green')
        fram.pack(padx=10, pady=10)
        Label(fram, text='%s :' % self.Langue['AffichLangue'], font='calibri 12 bold italic', bg='light sea green').pack(side=LEFT, pady=10, padx=5)
        self.ChoixLangues = ttk.Combobox(fram, values=Langues, width=30, font='Calibri 12 bold')
        self.ChoixLangues.set(self.Langue['LangueFrancais'])
        self.ChoixLangues.config(state='readonly')
        self.ChoixLangues.pack(side=LEFT, padx=5)

        Button(self.fen1, text='%s' % self.Langue['Appliquer'], font='calibri 12 bold italic', bg='bisque', command=self.Appliquerreglages).pack(side=BOTTOM, pady=10)

    def Appliquerreglages(self):
        Langues = self.ChoixLangues.get()
        if Langues == 'French' or Langues == 'Français':
            self.Langue = self.Francais
            self.fen1.destroy()
            self.fen.update()
        elif Langues == 'Anglais' or Langues == 'English':
            self.Langue = self.Anglais
            self.fen1.destroy()
            self.fen.update()
        
    def bold(self):
        if self.valbold.get() == 1:
            self.valeurgras = 'bold'
            self.Message.configure(font='%s %s %s %s %s' %(self.valeurPolice, self.valeurtaillepolice, self.valeurgras, self.valeuritalic, self.valeursouligner ))
        else:
            self.valeurgras = ''
            self.Message.configure(font='%s %s %s %s %s' %(self.valeurPolice, self.valeurtaillepolice, self.valeurgras, self.valeuritalic, self.valeursouligner))

    def italic(self):
        if self.valitalic.get() == 1:
            self.valeuritalic = 'italic'
            self.Message.configure(font='%s %s %s %s %s' %(self.valeurPolice, self.valeurtaillepolice, self.valeurgras, self.valeuritalic, self.valeursouligner ))
        else:
            self.valeuritalic = ''
            self.Message.configure(font='%s %s %s %s %s' %(self.valeurPolice, self.valeurtaillepolice, self.valeurgras, self.valeuritalic, self.valeursouligner ))
    
    def souligner(self):
        if self.valsouligner.get() == 1:
            self.valeursouligner = 'underline'
            self.Message.configure(font='%s %s %s %s %s' %(self.valeurPolice, self.valeurtaillepolice, self.valeurgras, self.valeuritalic, self.valeursouligner))
        else:
            self.valeursouligner = ''
            self.Message.configure(font='%s %s %s %s %s' %(self.valeurPolice, self.valeurtaillepolice, self.valeurgras, self.valeuritalic, self.valeursouligner))
            
    def optboutajPJ(self):
        if self.valcheck.get() == 1:
            fr = Frame(self.Labframfram, bg='light sea green')
            fr.pack()
            self.boutajPJ = Button(fr, text='Ajouter', fg='red', font='calibri 10 italic bold', bg='bisque',command=self.AjouterPieceJointe)
            self.boutajPJ.pack(anchor='ne')
        else:
            if self.ListePieceJointe_Ajoute != []:
                if askyesno('PIECE JOINTE','DES FICHIERS ONT ÉTÉ AJOUTÉS SI VOUS CONTINUER IL SERONT ENLEVÉS !!!'):
                    self.Labframfram.destroy()
                    self.Labframfram = Frame(self.fram000, bg='light sea green')
                    self.Labframfram.pack(pady=5, side=RIGHT)
                    self.ListePieceJointe_Ajoute = []
                    self.NomPieceJointe = []
                    try:
                        self.frem.destroy()
                    except:
                        rien = ''
                    else:
                        self.frem = Frame(self.fram000, bg='light sea green')
                        self.frem.pack(side=LEFT)
                else:
                    self.valcheck.set(1)
            else:
                self.Labframfram.destroy()
                self.Labframfram = Frame(self.fram000, bg='light sea green')
                self.Labframfram.pack(pady=5, side=RIGHT)
                   
    def AjouterPieceJointe(self):
        self.cryptfile = askopenfilenames(title='Choisir Fichier', filetypes=[('All Files','.*')])
        self.cryptfile = list(self.cryptfile)
        for i in self.cryptfile:
            if i in self.ListePieceJointe_Ajoute:
                showinfo('DÉJA AJOUTÉ', 'CE FICHIER A ÉTÉ DEJA AJOUTÉ DANS LA LISTE DES PIECES JOINTES !!!')
            else:
                self.ListePieceJointe_Ajoute.append(i)
                self.NomPieceJointe.append(i.split('/')[-1])
        try:
            self.frem.destroy()
        except:
            rien = ''
        else:
            self.frem = Frame(self.fram000, bg='light sea green')
            self.frem.pack(side=LEFT)
            
            for i in self.NomPieceJointe:
                if self.NomPieceJointe.index(i) == 5:
                    break
                fromm = LabelFrame(self.frem, bg='light sea green')
                fromm.pack(side=LEFT, padx=3)
                Label(fromm, text=i, font='calibri 10 bold italic', fg='green').pack()

        if len(self.ListePieceJointe_Ajoute) > 3:
            showinfo('AFFICHAGE PIECE JOINTE','SI VOUS AVEZ AJOUTER PLUSIEURS PIECES JOINTES ET QUE LEURS NOM NE FIGURENT PAS A L\'AFFICHAGE, VEUILLEZ CONSULTER DANS LA BARRE DES MENUS L\'ONGLET OPTIONS DANS "LISTE DES PIECES JOINTES" !!!') 


    def AfficheListePieceJointe(self):
        if self.NomPieceJointe == []:
            showinfo('VIDE','AUCUNE PEICE JOINTE N\'A ÉTÉ AJOUTÉE !!!')
        else:
            self.fen1 = Toplevel(self.fen)
            self.fen1.grab_set()
            self.fen1.focus_set()
            self.fen1.geometry("400x300+350+10")  
            self.fen1.title('One MAILS Pieces Jointes Ajoutées')
            self.fen1.iconbitmap('Images\Icone.ico') 
            self.fen1.config(bg='light sea green')
            self.fen1.resizable(width=False, height=False)
            
            scrollbar = Scrollbar(self.fen1)
            scrollbar.pack(side=RIGHT, fill=Y, anchor='ne')
            scrollbar1 = Scrollbar(self.fen1, orient=HORIZONTAL)
            scrollbar1.pack(side=BOTTOM, fill=X)

            self.Texte = Text(self.fen1, font='calibri 12 italic',  wrap='none')
            self.Texte.pack(fill=BOTH)

            scrollbar.configure(command=self.Texte.yview)
            scrollbar1.configure(command=self.Texte.xview)
            self.Texte['yscrollcommand'] = scrollbar.set
            self.Texte['xscrollcommand'] = scrollbar1.set
            
            for i in self.NomPieceJointe:
                self.Texte.insert(END, i+'\n')
            self.Texte.configure(state=DISABLED)

        
    def Ajdestinataire(self):
        adraj = self.entredes.get()
        if adraj == '':
            showinfo('CHAMP VIDE', 'VEUILLEZ RENSEIGNER L\'ADRESSE MAIL DU DESTINATAIRE ET L\'AJOUTER !!!')
        elif re.match(r'(^[a-z0-9._-]+@[a-z0-9._-]+\.[a-z]{2,3}$)', adraj) is None:
            showinfo('ERREUR ADRESSE MAIL', 'L\'ADRESSE MAIL QUE VOUS AVEZ RENSEIGNÉ N\'EST PAS VALIDE\nVÉRIFIEZ SI IL Y\'A DES CARACTÈRES MAJUSCULE OU LE FORMAT DE VOTRE ADRESSE MAIL !!!')
            self.entredes.delete(0, 1000000)
        elif len(self.ListeMail_Ajoute) == 5:
            showinfo('LIMITE AJOUT', 'NOMBRE DE DESTINATAIRE LIMITÉ A 5 PAR ENVOIE !!!')
        else:
            if adraj in self.ListeMail_Ajoute:
                showinfo('%s' % self.Langue['TitreEmailDajaAjoute'], '%s' % self.Langue['TextEmailDejaAjoute'])
            else:
                self.ListeMail_Ajoute.append(adraj)
                Labfram = LabelFrame(self.labo, bg='light sea green')
                Labfram.pack(side=LEFT)
                Label(Labfram, text=adraj, font='calibri 10 bold italic', fg='green').pack()
                self.entredes.delete(0, 1000000)
            if len(self.ListeMail_Ajoute) == 1:
                self.boutboutbout = Button(self.fram01, text='X*',fg='red', command=self.laabo)
                self.boutboutbout.pack(side=RIGHT)

    def laabo(self):
        self.labo.destroy()
        self.boutboutbout.destroy()
        self.ListeMail_Ajoute = []
        self.labo = Frame(self.fram01, bg='light sea green')
        self.labo.pack(side=LEFT, padx=3)

    def Envoyer(self):
        if self.ListeMail_Ajoute == []:
            showinfo('LISTE DETINATAIRE VIDE','AUCUN DESTINATAIRE A ÉTÉ AJOUTÉ !!!')
        elif  self.Message.get(0.0, END) == '\n' :
            showinfo('CORP DE TEXTE', 'LE MESSAGE EST VIDE VEUILLEZ ECRIRE !!!')
        else:
            for i in self.ListeMail_Ajoute:
                msg = MIMEMultipart()
                msg['From'] = self.adrmail
                msg['To'] = i
                msg['Subject'] =  self.entreobj.get()
                body = self.Message.get(0.0, END)
                msg.attach(MIMEText(body, 'plain'))
                zzz = 0
                for j in self.ListePieceJointe_Ajoute:
                    filename = self.NomPieceJointe[zzz]
                    attachment = open(j, 'rb')
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload((attachment).read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)
                    msg.attach(part)
                    zzz += 1
                    
                text = msg.as_string()
                try:
                    try:
                        self.server.login(self.adrmail, self.mp)
                    except smtplib.SMTPAuthenticationError:
                        showinfo('ERREUR IDENTIFIANT', 'IDENTIFIANT OU MOT DE PASSE INCORRECTE !!!')          
                    self.server.sendmail(self.adrmail, i, text)
                except:
                    showinfo('ERREUR', 'UNE ERREUR S\'EST PRODUITE LORS DE L\'ENVOIE DE VOTRE MESSAGE.\nVEUILLEZ VERIFIER VOTRE CONNEXION INTERNET !!!')
                else:
                    self.labo.destroy()
                    self.labo = Frame(self.fram01, bg='light sea green')
                    self.labo.pack(side=LEFT, padx=3)
                    self.boutboutbout.destroy()
                    try:
                        self.frem.destroy()
                    except:
                        rien = ''
                    else:
                        self.frem = Frame(self.fram000, bg='light sea green')
                        self.frem.pack(side=LEFT)
                    self.Labframfram.destroy()
                    self.Labframfram = Frame(self.fram000, bg='light sea green')
                    self.Labframfram.pack(pady=5, side=RIGHT)
                    self.valcheck.set(0)
                    self.Message.delete(0.0, 100000000000.0)
                    self.entreobj.delete(0, 100000000)
                    showinfo('SUCCES' ,'ENVOYE AVEC SUCCES !!!')
        
            with open('Contact.dll', 'r') as f:
                ContactEnreg = f.read()
            zzz = []
            for i in ContactEnreg.split('\n'):
                zzz.append(i)
    
            for i in self.ListeMail_Ajoute:
                if i not in zzz:
                    with open('Contact.dll','a') as f:
                        f.write( i + '\n')
                        f.close()
                        
            self.ListeMail_Ajoute = []
            self.ListePieceJointe_Ajoute = []
            self.NomPieceJointe  = []
                
    def cryptbin (self, chaine):
        liste = list(chaine)
        IN = []
        BIN = []
        for i in liste:
            if i in self.CODE:
                ind = self.CODE.index(i)
                IN.append(ind)
        for i in IN:
            BIN.append(bin(i))
        return ''.join(BIN)

    def debin(self, chaine):
        chaine = list(chaine)
        chaine.reverse()
        val = 0
        tot = 0
        for i in chaine:
            if i == '1':
                tot += 2 ** val
            val += 1
        return int(tot)

    def decryptbin(self, chaine):
        valeur = []
        liste  = []
        chaine = chaine.split('0b')
        try:
            chaine.remove('')
        except:
            zero = 0
        for i in chaine:
            valeur.append(self.debin(i))
        for i in valeur:
            liste.append(self.CODE[i])
        return ''.join(liste)
            
Fenetre = OneMails()
