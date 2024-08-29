#Take the all the alphabets in english in the form of list
alphabet=['a','b','c','d','e','f','g','h','i','j',
          'k','l','m','n','o','p','q','r','s','t',
          'u','v','w','x','y','z']

#Function to take the message and shitf number and give the encrypted or decrypted message based on your choice
def Ceaser_Cipher(choice,message,shift):
    result=""
    for i in message:
        if i not in alphabet:
            cipher+=i 
        else:
            ind=alphabet.index(i)
            if choice=='encrypt':
                new_p=(ind+shift)%26
            elif choice=='decrypt':
                new_p=(ind-shift)%26
            result+=alphabet[new_p]
    print(result)
        

flag=True
while flag:
    choice=input("Type 'encrypt' for Encryption or Type 'decrypt' for Decryption:")
    message=input("Enter your message:").lower()
    shift=int(input("Type shift key:"))
    Ceaser_Cipher(choice,message,shift)
    con=input("If you want to continue type 'yes' else type 'no':")
    if con=='no':
        flag=False 
        print("Have a nice day Good bye..")
    
