from tkinter import filedialog
import config
class CommonUtils:

    @staticmethod
    def load_txt():
        file_name = filedialog.askopenfilename()
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            index = 0
            date = []
            open_ = []
            high = []
            low = []
            close = []
            for line in lines:
                if (index == 0):
                    index += 1
                else:
                    linesplit = line.split(',')
                    date.append('20' + linesplit[0][0:2] + '-' + linesplit[0][2:4] + '-' + linesplit[0][4:6])
                    open_.append(float(linesplit[2]))
                    high.append(float(linesplit[3]))
                    low.append(float(linesplit[4]))
                    close.append(float(linesplit[5]))
        result_dict = {'date': date, 'open': open_, 'high': high, 'low': low, 'close': close}
        config.res_dict = result_dict
        print(config.res_dict)
        config.mainApp.button_show.config(command=config.mainApp.show)