from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = 'C:\\Python36\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = 'C:\\Python36\\tcl\\tk8.6'

base = 'Win32GUI' #None    

executables = [Executable('One Mails.py', base=base, icon='Images\Icone.ico')]

packages = ['idna', 'tkinter', 'tkinter.ttk', 'tkinter.messagebox',\
            'tkinter.filedialog', 'smtplib', 'email.mime.multipart', 'email.mime.text',\
            'email.mime.base', 'email', 're', 'webbrowser', 'random']
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = 'One MAILS',
    options = options,
    version = '1.0',
    description = 'ENvoi d\'eamil avec compte gmail simplifier',
    executables = executables
)
