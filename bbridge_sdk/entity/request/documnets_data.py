class DocumentsData(object):
    def __init__(self, documents, count):
        """
        :type documents: list[list[str]]
        :type count: int
        """
        self.__count = count
        self.__documents = documents

    @property
    def documents(self):
        return self.__documents

    @property
    def count(self):
        return self.__count
