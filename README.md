
# **Caesar Cipher Program**

This Python program provides a simple implementation of the Caesar Cipher, a basic encryption technique where each letter in the plaintext is shifted by a certain number of positions down the alphabet.

## **Features**

- **Encrypt a Message**: Convert your plaintext message into cipher text by shifting each letter by a specified number of positions.
- **Decrypt a Message**: Convert your cipher text back into plaintext by reversing the shift.
- **User Interaction**: The program allows users to continuously encrypt or decrypt messages until they choose to exit.

## **How to Use**

1. **Choose an Operation**:
   - Type `'encrypt'` for encryption.
   - Type `'decrypt'` for decryption.

2. **Enter Your Message**:
   - Provide the message you want to encrypt or decrypt. The program automatically converts it to lowercase to simplify processing.

3. **Enter the Shift Key**:
   - Specify a number for the shift key, which determines how many positions each letter will be shifted in the alphabet.

4. **View the Result**:
   - The program outputs the encrypted or decrypted message based on your choice.

5. **Continue or Exit**:
   - After viewing the result, you can choose to continue encrypting/decrypting more messages or exit the program.

## **Example Usage**

```
Type 'encrypt' for Encryption or Type 'decrypt' for Decryption: encrypt
Enter your message: hello
Type shift key: 3
khoor

If you want to continue type 'yes' else type 'no': yes

Type 'encrypt' for Encryption or Type 'decrypt' for Decryption: decrypt
Enter your message: khoor
Type shift key: 3
hello

If you want to continue type 'yes' else type 'no': no
Have a nice day. Goodbye!
