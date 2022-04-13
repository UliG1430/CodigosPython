frase=str(input("INGRESE UNA PALABRA O FRASE: "))
alphabets = [ ch for ch in frase if ( ord(ch) >= ord('a') and ord(ch) <= ord('z') )]
if len(set(alphabets))==len(alphabets): 
         print ('Yes') 
else:
        print('No')
