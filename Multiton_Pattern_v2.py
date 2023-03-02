class Multiton:
     __instances = []
     __max_instances = 3
     __count = -1

     def __new__(cls):
         cls.__count += 1
         if len(cls.__instances) < cls.__max_instances:
             cls.__instances.append(super().__new__(cls))
         return cls.__instances[cls.__count % cls.__max_instances]


     @classmethod
     def set_max_instances(cls, max_instances):
         cls.__max_instances = max_instances

clas1 = Multiton()
clas2 = Multiton()
clas3 = Multiton()
clas4 = Multiton()
clas5 = Multiton()
clas6 = Multiton()
clas7 = Multiton()
clas8 = Multiton()
clas9 = Multiton()

print(clas1 is clas4 ) # True
print(clas1 is clas3 ) # False
