import random

characters='''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+[]\}{|;':",./<>?'''
characters_letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
characters_numbers='1234567890'
characters_special='''!@#$%^&*()-=_+[]\}{|;':",./<>?'''

def composition(total_length):
    '''
    This function determines how many of which
    type of character make up the password
    input: length of password
    output: dict of numbers for the count of each of the
    three types 
    '''
    dictionary={'letters':0,'numbers':0,'special':0}
    character_type_choice=['letters','numbers','special']
    for x in range(0,total_length-3):
        choice1=random.choice(character_type_choice)
        if choice1=='letters':
            dictionary['letters']+=1
        elif choice1=='numbers':
            dictionary['numbers']+=1
        elif choice1=='special':
            dictionary['special']+=1
    dictionary['letters']+=1
    dictionary['numbers']+=1
    dictionary['special']+=1
    #print(dictionary)
    return dictionary


while True:
    
    password_len=int(input('What length password do you need::'))
    no_of_passwords=int(input('how many passwords do you need::'))
    for i in range(0,no_of_passwords):
        dictionary1=composition(password_len)
        #print(dictionary1)
        final_password=''
        print(i+1)
        #for j in range(0,password_len):
        password_letters=random.choices(characters_letters,k=dictionary1['letters'])
        password_numbers=random.choices(characters_numbers,k=dictionary1['numbers'])
        password_special=random.choices(characters_special,k=dictionary1['special'])
        password=(password_letters+password_numbers+password_special)
        random.shuffle(password)
        #print(password)
        for j in (password):
            final_password+=j
        print('Here is your password::',(final_password))
    choice=input("Do you want to continue?\n(y/n)::")
    if choice=='n':
        break
    else:
        continue