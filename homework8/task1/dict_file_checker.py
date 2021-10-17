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
        for key, value in new_dict.items():
            if key not in self.__dict__:
                self.__dict__[key] = value

    def __getattr__(self, item: str):
        if item not in self.__dict__:
            raise AttributeError("Wrong attribute")
        return item

    def __getitem__(self, item):
        return self.__dict__[item]
