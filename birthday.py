from datetime import datetime
from plyer import notification
import time
import os
import pywhatkit
current_dir = os.getcwd()

# birthdayfile = r'C:\Users\h.coleau\Pictures\birth2\bdayfile.txt'
birthdayfile = current_dir+'\data.txt'
   
def alerteAnniv():
    filename = open(birthdayfile, "r")
    today = time.strftime('%d%m')
    bday = False
    for unAnniversaire in filename:
        if today in unAnniversaire:
            unAnniversaire = unAnniversaire.split(' ')
            
            print('Anniversaire de ' + unAnniversaire[1] + ' ' + unAnniversaire[2]+" le "+unAnniversaire[0])
            bday = True
            if __name__ == "__main__":
                notification.notify(
                    title="Joyeux Anniversaire "+unAnniversaire[2],
                    message='''1 an de plus aujourd'hui ça se fête !''',
                    app_name = 'notif anniversaire',
                    app_icon=current_dir+'\\anniv.ico',
                    
                    timeout=8
                )
                
                # if bday == True :
                #     pywhatkit.sendwhatmsg(unAnniversaire[3], "Bon Anniversaire !",0,0) 
                    
if __name__ == '__main__':
    alerteAnniv()