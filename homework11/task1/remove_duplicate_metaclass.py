class SimplifiedEnum(type):
    def __new__(cls, name, bases, attrs):
        list_of_attrs = []
        for i, j in attrs.items():
            if i.startswith(f'_{name}'):
                for attr in j:
                    list_of_attrs.append(attr)
        for i in list_of_attrs:
            attrs[i] = i

        return super().__new__(cls, name, bases, attrs)
