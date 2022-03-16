f=open("test.txt","w")
try:
    #무언가를 수행한다
    pass
finally :
    f.close()
    
try:
    f = open("sss.txt","r")
except FileNotFoundError as e:
    print(e)

# class Bird :
#     def fly(self) :
#         raise NotImplementedError
    
# class Eagle(Bird) :
#     pass

# eagle = Eagle()
class MyError(Exception) :
    pass
def say_nick(nick) :
    if nick == "바보" :
        raise MyError()
    
    print(nick)
    
say_nick("바보")


