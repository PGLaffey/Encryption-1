from random import randint
import time

class program():
    def reader(dirrect):
        file = open(dirrect,'r')
        lines = []
        lines.append(file.readlines())
        lines = lines[0]
        count = 0
        while count < len(lines):
            lines[count] = lines[count].strip('\n')
            lines[count] = lines[count].lower()
            count += 1
        file.close()
        return lines

    def encryption_key():
        beta = []
        while len(beta) < 40:
            num = randint(0,39)
            if num not in beta:
                beta.append(num)
        return beta

    def encrypt(dirrect, initial=False):
        lines = program.reader(dirrect)
        beta = program.encryption_key()
        alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','[',']','1','2','3','4','5','6','7','8','9','0',',']
        new_line = ''
        new_lines = []
        for line in lines:
            for letter in line:
                count = 0
                while letter != alpha[count]:
                    count += 1
                new_line += alpha[beta[count]]
            new_line += '\n'
            new_lines.append(new_line)
            new_line = ''
        file = open(dirrect,'w')
        count = 0
        while count < len(new_lines):
            file.write(new_lines[count])
            count += 1
        file.write(str(beta))
        file.close()
        if initial == False:
            program.typer("File successfully encrypted.")
            program.finish(dirrect)

    def decrypt(dirrect, initial=False):
        lines = program.reader(dirrect)
        beta = lines[len(lines)-1]
        if beta.startswith('['):
            beta = beta.strip('[')
            beta = beta.strip(']')
            beta = beta.replace(',','')
            beta = list(beta)
            count = 0
            delta = []
            while count < len(beta):
                if beta[count] != ' ':
                    beta[count] = int(beta[count])
                count += 1
            if beta[1] == ' ':
                delta.append(beta[0])
                count = 1
            else:
                delta.append((beta[0]*10)+beta[1])
                count = 2
            while count < len(beta)-1:
                if beta[count] != ' ':
                    if beta[count+1] != ' ':
                        beta[count] = beta[count] * 10
                        beta[count+1] = beta[count+1] + beta[count]
                    elif beta[count+1] == ' ':
                        delta.append(beta[count])
                count += 1
            delta.append(beta[len(beta)-1])
            beta = delta
            alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','[',']','1','2','3','4','5','6','7','8','9','0',',']
            new_line = ''
            new_lines = []
            lines.pop()
            for line in lines:
                for letter in line:
                    count = 0
                    while letter != alpha[beta[count]]:
                        count += 1
                    new_line += alpha[count]
                new_line += '\n'
                new_lines.append(new_line)
                new_line = ''
            file = open(dirrect,'w')
            count = 0
            while count < len(new_lines):
                file.write(new_lines[count])
                count += 1
            file.close()
            if initial == False:
                program.typer("File successfully decrypted.")
                program.finish(dirrect)
        else:
            program.typer("Sorry that file is not encrypted")
            program.main(dirrect)

    def read(dirrect):
        lines = program.reader(dirrect)
        count = 0
        print('')
        while count < len(lines):
            program.typer(lines[count])
            time.sleep(0.2)
            count += 1
        print('')
        program.finish(dirrect)

    def typer(to_print):
        count = 0
        printing = list(to_print)        
        while count < len(to_print):
            print(printing[count],end="")
            time.sleep(speed)
            count = count + 1
        print('')

    def main(dirrect):
        if dirrect != None:
            program.typer('encrypt, decrypt, read or change the settings?')
            com = input('')
            count = 2
            if com.lower() == 'encrypt':
                while count > 0:
                    program.encrypt(dirrect,True)
                    count -= 1
                program.encrypt(dirrect)                
            elif com.lower() == 'decrypt':
                while count > 0:
                    program.decrypt(dirrect,True)
                    count -= 1
                program.decrypt(dirrect)                
            elif com.lower() == 'read':
                program.read(dirrect)
            elif com.lower() == 'settings':
                settings.options(dirrect)
            else:
                program.typer('Sorry please enter "encrypt", "decrypt", "read" or "settings"')
                program.main(dirrect) 
        else:
            dirrect = program.dirrectory()
            program.main(dirrect)

    def dirrectory():
        program.typer('Enter dirrectory to file:')
        dirrect = input('')
        try:
            file = open(dirrect,'r')
            program.typer('File sucessfully loaded')
            file.close()
            return dirrect
        except:        
            program.typer('Error reading file\nError 401: File not found')
            return None

    def finish(dirrect):
        if keep_file == False:
            program.typer("Would you like to encrypt, decrypt or read again?")
            ans = input('')
            if ans[:1].lower() == 'y':
                program.typer("Would you like to use the same file?")
                ans = input('')
                if ans[:1].lower() == 'y':
                    program.main(dirrect)
                elif ans[:1].lower() == 'n':
                    prgoram.main(None)
                else:
                    program.finish(dirrect)
            elif ans[:1].lower() == 'n':
                program.typer("Thanks for coming!")
            else:
                program.typer("Error: Answer not valid. (y/n)")
                program.finish(dirrect)
        elif keep_file == True:
            program.main(dirrect)

class settings():
    def default():
        global speed, keep_file
        speed = 0.05
        keep_file = False
        
    def options(dirrect):
        program.typer("Settings;")
        program.typer("Type Speed - change the speed in which the computer types.")
        program.typer("Keep File - The computer will continue to use the same file until reset or setting changed.")
        program.typer("Leave - Leaves settings and resumes encryption program.")
        print(' ')
        program.typer("Would you like to change 'Type Speed' or 'Keep File' setting?")
        ans = input()
        if 'speed' in ans.lower():
            settings.typespeed(dirrect)
        elif 'file' in ans.lower():
            settings.keepfile(dirrect)
        elif 'leave' in ans.lower():
            program.main(dirrect)
        else:
            program.typer("Sorry I dont recognize that setting.")
            settings.options(dirrect)

    def typespeed(dirrect):
        global speed
        program.typer("Please enter your desired type speed in seconds (Default 0.1):")
        ans = input()
        try:
            speed = float(ans)
            program.typer("Type speed set to " + str(speed))
            settings.options(dirrect)
        except:
            program.typer("Sorry, you must enter a number of seconds")
            settings.typespeed(dirrect)

    def keepfile(dirrect):
        global keep_file
        program.typer("Would you like the computer to use the same file dirrectory for the duration of the program? (Default, no)")
        ans = input()
        try:
            ans = float(ans)
            program.typer("Answer not valid. Please enter a string.")
            settings.keepfile(dirrect)
        except:
            if 'yes' in ans.lower():
                keep_file = True
                program.typer("Keep file setting set to 'True'.")
                settings.options(dirrect)
            elif 'no' in ans.lower():
                keep_file = False
                program.typer("Keep file setting set to 'False'.")
                settings.options(dirrect)
            else:
                program.typer("Sorry, I dont understand. Please enter yes or no.")
                settings.keepfile(dirrect)

class __init__():
    def init():
        settings.default()
        __init__.login()


    def login():
        import tkinter
        master = tkinter.Tk()
        username_entry = tkinter.Entry(master,show=" ")
        password_entry = tkinter.Entry(master,show="*")
        tkinter.Label(master, text="Username").grid(row=0,column=0,pady=10,padx=5)
        tkinter.Label(master, text="Password").grid(row=1,column=0,pady=10,padx=5)
        username_entry.grid(row=0,column=1)
        password_entry.grid(row=1,column=1)
        master.bind("<Return>",lambda event,username_entry=username_entry,password_entry=password_entry,master=master:__init__.logon(username_entry,password_entry,master))
        master.title("Log In")

    def logon(username_entry, password_entry, master):
        username = username_entry.get()
        password = password_entry.get()
        try:
            file = open('files/login.tt')
            file.close()
            __init__.user_decrypt()
            lines = program.reader('files/login.txt')
            if username.lower() == lines[0] and password.lower() == lines[1]:
                __init__.user_encrypt()
                master.destroy()
                program.typer("Welcome User.")
                program.main(None)
            else:
                __init__.user_encrypt()
                program.typer("Incorrect username or password")
        except FileNotFoundError: #Temp fix to bug that gets around login
            program.typer('Error: Base Login file not found, reverting to system defaults.')
            if username.lower() == 'pglaffey' and password.lower() == 'p#trifi8d':
                master.destroy()
                program.typer("Welcome User.")
                program.main(None)
            else:
                program.typer("Incorrect username or password")
            
    def user_decrypt():     
        count = 0
        while count < 3:
            program.decrypt('files/login.txt',True)
            count += 1

    def user_encrypt():     
        count = 0
        while count < 3:
            program.encrypt('files/login.txt',True)
            count += 1

__init__.init()


#Make read function for on screen printing and login so only people with
#permission can access files. You know the username and password (command)
