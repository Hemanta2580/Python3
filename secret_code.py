import random
import string

# encoding of the  word
def encode_word(word):
    if len(word)<3:
        word1=word[::-1]
        return word1
    else:
        word1=word[1:]
        word2=word1+word[0]
        # print(word2)
        ran= ''.join(random.choices(string.ascii_letters, k=3))
        ran2=''.join(random.choices(string.ascii_letters, k=3))
        word3=ran+word2+ran2
        return word3
    # print(word3)
    # print(len(word3))

# decoding of the string
def decode_word(word):
    if len(word)<3:
        return (word[::-1])
    else:
        n=len(word)
        word1=word[3:-4]

        word2=word[n-4]+word1
        return word2



# main Function
if __name__=='__main__':
    try:
        print("press 1  to  encode of a word and press 2 to decode a word ")
        choice=int(input())
        if choice==1:
            word = input("please tell the word ")
            x = encode_word(word)
            print("the encoded word is:",x)
        elif(choice==2):
            word=input("enter the word to decode ")
            y = decode_word(word)
            print("the decoded word is ",y)

    except:
        print("invalid input")




