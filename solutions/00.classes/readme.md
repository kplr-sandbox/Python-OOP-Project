import dis

def myfunc():
    a = ['0','1','2']
    string = 'hello'
    print(string)
    return len(a)


dis.dis(myfunc)