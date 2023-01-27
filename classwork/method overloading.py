class sample:
    def common(self):
        n=int(input("enter no"))
        print("number",n)
    def common(self,a,b):
        self.a=a
        self.b=b

        if self.a>self.b:
            print(self.a,"is greater")
        else:
            print(self.b,"is greater")
s=sample()
s.common()
