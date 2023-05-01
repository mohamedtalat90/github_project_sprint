#this is the old string
string = "abracadabra"
#this is printing the string
print("this is the old string: "+ string)

#this is defining the function that will modify the string
def function(string, position, character):
    return string[:position]+character+string[position+1:]



print("this is the new modified string: ")
#printing and calling the function and adding the arguments to it
print(function(string,5,"k"))