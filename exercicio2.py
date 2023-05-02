#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui







# Teste a sua função aqui (caso ache necessário)


# def is_anagram(string1, string2):
print("digite a primeira palavra")
string1=input()
print("digite a segunda palavra")
string2=input()


def is_anagram(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()

    if sorted(string1) == sorted(string2):
        return True

    else:
        return False


if (is_anagram(string1,string2)==True):
    print("É um anagrama")
else:
   print("não é um anagrama") 

        














