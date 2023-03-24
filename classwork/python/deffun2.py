def deffun(a,b,c=30,d=40):
    print("a=",a,"b=",b,"c=",c,"d=",d)
deffun(10,20)



def test(a=30,b=40,c=50,d=60):
    print("a=",a,"b=",b,"c=",c,"d=",d)
test(a=200,b=300)



"""
arbitary argument
"""
def arbit(a,b,c,*d):
    print("a=",a,"b=",b,"c=",c,"d=",d)
arbit(10,20,30,40,50,60,70)



def arbt2(a,b,c,*d,**e):
    print("a=",a,"b=",b,"c=",c,"d=",list(d),"e=",e)
arbt2(20,30,40,50,60,70,80,x=43,y=34,z=33)
