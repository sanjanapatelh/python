class CallDetails:
    def __init__ (self,callfrom,callto,time,typeof):
        self.callfrom=callfrom
        self.callto=callto
        self.time=time
        self.typeof=typeof
    def printDetails(self):
        print("CallFrom:",self.callfrom)
        print("CallTo:",self.callto)
        print("Time:",self.time)
        print("Type:",self.typeof)
        print()

class util:
    def parse_customer(self,li):
        l=[]
        for i in range(len(li)):
            a=li[i].split(",")
            b=CallDetails(a[0],a[1],a[2],a[3])
            b.printDetails()
            l.append(b)
call1='9874563210,963258741,23,STD'
call2='741852963,852963741,2365,LOCAL'
        
list_of_call=[call1,call2]
l=util()
l.parse_customer(list_of_call)
