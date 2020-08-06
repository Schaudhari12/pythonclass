def sayGoodbye(name):
    print(f"Goodbye {name}")
# call the method
sayGoodbye('Sanika')
def getFarewell():
    return "goodbye"
# call the method
message = getFarewell()
print(message)
def getFarewell(name):
    return f"Goodbye {name}"
#call the method
message = getFarewell('Mitali')
print(message)
def getFarewell(name,message):
    return f"goodbye {name}, you said {message}"
#call the method
message = getFarewell('Sanika', 'how are you?')
def getGreetings(name, message):
    return f"Bye {name}, {message}"
message = getGreetings('Sanika', 'have a good day!')
print(message)