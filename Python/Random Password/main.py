from random import shuffle
characterSet="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 - ! \" # $ % & \' ( ) * + , . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~ ".split(" ")
length=0
while length == 0:
    legnth_input=int(input(f"Length of your password (minimum 8, no maximum but larger numbers will take longer based on device specs) \nAnswer: "))
    if legnth_input < 8:
        print("Length has to be greater than 8")
    else:
        length = legnth_input
passwordList=[]
for i in range(1, length + 1):
    #print(characterSet)
    shuffle(characterSet)
    #print(characterSet)
    passwordList.append(characterSet[0])
    #print(passwordList)
password = "".join(passwordList)
print(f"Your random password: {password}")