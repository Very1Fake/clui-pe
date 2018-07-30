# Command Line User Interface  LightPixel  copyright 2018
# Version 0.0.1pa1

import os

class UI():
    def __init__(self):
        self.rows, self.columns = os.popen('stty size', 'r').read().split()
        self.rows = int(self.rows)
        self.columns = int(self.columns)
        self.windows = {}

    def getOptions(self, options):
        temp = {}

        # Main sector check
        if not 'main' in options:
            temp['main'] = {}
        else:
            ## Border symbol
            temp['main'] = options['main']

        return temp

    def getClearWindow(self, name, options={}):
        options = self.getOptions(options)
        windows = []

        temp = options['main']['symbol'] + name

        for i in range(self.columns - len(temp)):
            temp = ''
            windows.append(temp)

        for i in range(self.rows - 2):
            temp = ''
            temp = options['main']['symbol']
            for i in range(self.columns - 2):
                temp += " "
            temp += options['main']['symbol']
            windows.append(temp)

        for i in range(self.columns - len(temp)):
            temp += options['main']['symbol']
            windows.append(temp)
