class KeyValueStorage:
    def __init__(self, path: str):
        new_dict = {}
        with open(path) as file:
            text_from_file = file.read().split()
        for i in text_from_file:
            i = i.split('=')
            try:
                i[1] = int(i[1])
            except ValueError:
                pass
            new_dict[i[0]] = i[1]
        self.__dict__ = new_dict

    def __getattr__(self, item):
        if item not in self.__dict__:
            raise ValueError("Wrong attribute")

    def __getitem__(self, item):
        return self.__dict__[item]
