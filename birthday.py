from datetime import datetime
from plyer import notification
import time
#import pywhatkit
birthdayfile = r'C:\Users\h.coleau\Pictures\birth2\bdayfile.txt'
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
                    app_icon=r"C:\Users\h.coleau\Pictures\birth2\anniv.ico",
                    timeout=8
                )
                
                # if bday == True :
                #     pywhatkit.sendwhatmsg(unAnniversaire[3], "Bon Anniversaire !", 10, 15) 
                    
if __name__ == '__main__':
    alerteAnniv()