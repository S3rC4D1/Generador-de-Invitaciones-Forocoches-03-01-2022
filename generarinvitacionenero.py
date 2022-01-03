import webbrowser
import pyperclip

print('Introduce código :')
invitacion = input()
invitacionminusculas=invitacion.lower()
    
caracteres= "1"
    
for x in range(len(caracteres)):
 cadenaminusculas = invitacionminusculas.replace(caracteres[x],"")
    
pyperclip.copy(str(''.join(cadenaminusculas)))

webbrowser.open("https://www.forocoches.com/codigo/", new=2, autoraise=True)
