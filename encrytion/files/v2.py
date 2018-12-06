from random import randint

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
    print(lines)
    file.close()
    return lines

def encryption_key():
    beta = []
    while len(beta) < 27:
        num = randint(0,26)
        if num not in beta:
            beta.append(num)
    print(beta)
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
            print(count)
            new_line += alpha[beta[count]]
        new_line += '\n'
        new_lines.append(new_line)
        new_line = ''
    print(new_lines)
    file = open(dirrect,'w')
    count = 0
    while count < len(new_lines):
        file.write(new_lines[count])
        count += 1
    file.write(str(beta))
    file.close()

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
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    new_line = ''
    new_lines = []
    lines.pop()
    for line in lines:
        for letter in line:
            count = 0
            while letter != alpha[beta[count]]:
                count += 1
            print(count)
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

def main():
    dirrect = dirrectory()
    print('encrypt or decrypt?')
    com = input('')
    if com.lower() == 'encrypt':
        encrypt(dirrect)
    elif com.lower() == 'decrypt':
        decrypt(dirrect)
    else:
        print('Sorry please enter encrypt or decrypt')
        main()

def dirrectory():
    print('Enter dirrectory to file:')
    dirrect = input('')
    return dirrect

main()
