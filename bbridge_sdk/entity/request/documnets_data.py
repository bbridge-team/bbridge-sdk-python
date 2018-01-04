class DocumentsData(object):
    def __init__(self, documents):
        """
        :type documents: list[list[str]]
        """
        self.__documents = documents

    @property
    def documents(self):
        return self.__documents
