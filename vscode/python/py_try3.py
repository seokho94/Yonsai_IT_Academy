try :
    a = [1,2]
    print(a[3])
    print(4/0)
except ZeroDivisionError as e :
    print(e)
except IndexError as e:
    print(e)
    
try :
    b =[1,2]
    print(b[3])
    print(4/0)
except (ZeroDivisionError, IndexError) as e :
    print(e)