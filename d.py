class student:
    def __init__(self,name,cource):
        self.name = name 
        self.cource = cource 
    @staticmethod
    def greet ():
        print("welcome to acb collage")  

student1 = student("rajat","bca")
student1.greet()
