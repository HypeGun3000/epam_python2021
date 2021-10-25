class KeyValueStorage:
    def __init__(self, path: str):
        with open(path) as file:
            text_from_file = file.read().split()
        for i in text_from_file:
            i = i.split('=')
            if i[0] not in self.__dict__:
                try:
                    self.__dict__[i[0]] = int(i[1])
                except ValueError:
                    self.__dict__[i[0]] = i[1]

    def __getattr__(self, item: str) -> str:
        if item not in self.__dict__:
            raise AttributeError("Wrong attribute")
        return self.__dict__[item]

    def __getitem__(self, item: str):
        return self.__dict__[item]
