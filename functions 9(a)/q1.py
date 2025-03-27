# fun(),disp(),msg()
def fun():
    print("in fun")
def disp():
    print("in display")
def msg():
    print("in message")
    
lst=[fun,disp,msg]  # function ke baad () it means function call thase fun(),disp(),msg()   
for ele in lst:
    ele()
