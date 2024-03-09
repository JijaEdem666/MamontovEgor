from CommonUtils import CommonUtils
class SlugConverter:
    def __init__(self):
        self.__file_name = ""
        self.__slug_list = []
        self.file_name = input("Введите имя файла:")
        self.__run(int(input("Какое кол-во имён хотите ввести:")))

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, filename):
        self.__file_name = filename

    def __run(self, count):
        for i in range(count):
            CommonUtils.create_slug(self.file_name, input("Введите имя человека: "))