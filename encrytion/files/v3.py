from random import randint
import time

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
    while len(beta) < 27:
        num = randint(0,26)
        if num not in beta:
            beta.append(num)
    return beta

def encrypt(dirrect):
    lines = reader(dirrect)
    beta = encryption_key()
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
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
    print(beta)
    typer("File successfully encrypted.")
    finish(dirrect)

def decrypt(dirrect):
    lines = reader(dirrect)
    beta = lines[len(lines)-1]
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
    count = 1
    delta.append(beta[0])
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
    print(beta)
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
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
    typer("File successfully decrypted.")
    finish(dirrect)

def read(dirrect):
    lines = reader(dirrect)
    count = 0
    print('')
    while count < len(lines):
        typer(lines[count])
        time.sleep(0.2)
        count += 1
    print('')
    main(dirrect)

def typer(to_print):
    count = 0
    printing = list(to_print)        
    while count < len(to_print):
        print(printing[count],end="")
        time.sleep(0.01)
        count = count + 1
    print('')

def main(dirrect):
    if dirrect != None:
        typer('encrypt, decrypt or read?')
        com = input('')
        if com.lower() == 'encrypt':
            encrypt(dirrect)
        elif com.lower() == 'decrypt':
            decrypt(dirrect)
        elif com.lower() == 'read':
            read(dirrect)
        else:
            typer('Sorry please enter encrypt, decrypt or read')
            main(dirrect) 
    else:
        dirrect = dirrectory()
        main(dirrect)

def dirrectory():
    typer('Enter dirrectory to file:')
    dirrect = input('')
    try:
        file = open(dirrect,'r')
        typer('File sucessfully loaded')
        file.close()
        return dirrect
    except:        
        typer('Error reading file\nError 401: File not found')
        return None

def finish(dirrect):
    typer("Would you like to encrypt, decrypt or read again?")
    ans = input('')
    if ans[:1].lower() == 'y':
        typer("Would you like to use the same file?")
        ans = input('')
        if ans[:1].lower() == 'y':
            main(dirrect)
        elif ans[:1].lower() == 'n':
            main(None)
        else:
            finish(dirrect)
    elif ans[:1].lower() == 'n':
        typer("Thanks for coming!")
    else:
        typer("Error: Answer not valid. (y/n)")
        finish(dirrect)

main(None)


#Make read function for on screen printing and login so only people with
#permission can access files. You know the username and password (command)
