class Multiton:
    __instances = {}
    __max_instances = 5

    def __new__(cls, key):
        if key not in cls.__instances and len(cls.__instances) < cls.__max_instances:
            cls.__instances[key] = super().__new__(cls)
        return cls.__instances.get(key)

    @classmethod
    def set_max_instances(cls, max_instances):
        cls.__max_instances = max_instances

x1 = Multiton('armen1')
x2 = Multiton('armen2')
x3 = Multiton('armen3')
x4 = Multiton('armen4')  # None
