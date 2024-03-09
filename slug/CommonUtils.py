class CommonUtils:
    @staticmethod
    def translit_to_eng(s):
        azb = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "
        dictionary = dict()
        for i in azb:
            if i == 'а':
                dictionary[i] = 'a'
            elif i == 'б':
                dictionary[i] = 'b'
            elif i == 'в':
                dictionary[i] = 'v'
            elif i == 'г':
                dictionary[i] = 'g'
            elif i == 'д':
                dictionary[i] = 'd'
            elif i == 'е':
                dictionary[i] = 'e'
            elif i == 'ё':
                dictionary[i] = 'yo'
            elif i == 'ж':
                dictionary[i] = 'zh'
            elif i == 'з':
                dictionary[i] = 'z'
            elif i == 'и':
                dictionary[i] = 'i'
            elif i == 'й':
                dictionary[i] = 'j'
            elif i == 'к':
                dictionary[i] = 'k'
            elif i == 'л':
                dictionary[i] = 'l'
            elif i == 'м':
                dictionary[i] = 'm'
            elif i == 'н':
                dictionary[i] = 'n'
            elif i == 'о':
                dictionary[i] = 'o'
            elif i == 'п':
                dictionary[i] = 'p'
            elif i == 'р':
                dictionary[i] = 'r'
            elif i == 'с':
                dictionary[i] = 's'
            elif i == 'т':
                dictionary[i] = 't'
            elif i == 'у':
                dictionary[i] = 'u'
            elif i == 'ф':
                dictionary[i] = 'f'
            elif i == 'х':
                dictionary[i] = 'h'
            elif i == 'ц':
                dictionary[i] = 'c'
            elif i == 'ч':
                dictionary[i] = 'ch'
            elif i == 'ш':
                dictionary[i] = 'sh'
            elif i == 'щ':
                dictionary[i] = 'shch'
            elif i == 'ы':
                dictionary[i] = 'y'
            elif i == 'э':
                dictionary[i] = 'e'
            elif i == 'ю':
                dictionary[i] = 'yu'
            elif i == 'я':
                dictionary[i] = 'ya'
            elif i == ' ':
                dictionary[i] = '-'
            else:
                dictionary[i] = ''
        res = ''
        s = s.lower()
        for i in s:
            res += dictionary[i]
        return res

    @staticmethod
    def create_slug(fname, name):
        translit_name = CommonUtils.translit_to_eng(name)
        print(translit_name)
        CommonUtils.save_slug(fname, translit_name)

    @staticmethod
    def save_slug(fname, name):
        f = open(fname, "a")
        f.write(name + '\n')
        f.close()