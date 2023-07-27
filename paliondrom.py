text = input("На вход подайте строку, все символы, которой находятся в нижнем регистре и без пробелов      ")
text2 = list(text)
if text2 == text2[::-1]:
    print('True')
    
else:
    
    print('False')
   
