'''
def prim_checker(x):
    is_prime = True
    for i in range (2,x):
        if x % i ==0 :
            is_prime = False
    if is_prime == True:
        print('this number is is prime')
    else : 
        print('this number is NOT  prime ')


prim_checker(int(input('please enter a number to check : ')))
'''
def coding (name , shift):
    final=[]
    letters = list(name)
    alphabet_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for v in range (0 ,(len(letters))):
        for i in range(0,len(alphabet_list)):
            if letters[v] == alphabet_list[i]:
                break
        shift 
        name = alphabet_list[i+shift]
        final.append(name)
        word= ''.join(final)
    print(word)    

def decoding(name , shift):
    final=[]
    letters = list(name)
    alphabet_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for v in range (0 ,(len(letters))):
        for i in range(0,len(alphabet_list)):
            if letters[v] == alphabet_list[i]:
                break
        shift 
        name = alphabet_list[i-shift]
        final.append(name)
        word= ''.join(final)
    print(word)    



print('hello to Caesar Cipher')
is_play = True
while is_play == True:
    answer=int(input('press 1 to code or 2 to decode or 3 to exit: '))
    if answer==1:
        coding(input('enter the word you want to code: ') , int(input('enter the number you wanna shifte to : ')))
    elif answer==2:    
        decoding(input('enter the word you want to decode: ') , int(input('enter the number you shifted to : ')))
    elif answer ==3 :
        is_play == False
        print('thank you for using our Caesar Cipher')
        break
    else:
        print('please enter a valid answer (1/2/3)')