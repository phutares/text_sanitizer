import re
import sys
from collections import Counter
import sqlite3 # tentitive package
import configparser

class Logger():
    def __init__(self,fileName):
        self.console = sys.stdout
        self.file = open(fileName, 'w')

    def write(self, message):
        self.console.write(message)
        self.file.write(message)

    def flush(self):
        self.console.flush()
        self.file.flush()

class InitialOne():
    def initial_source():
        if len(sys.argv) > 1:
            source = sys.argv[1]
        else:
            config = configparser.ConfigParser()
            config.read('config.ini')
            source = config['DEFAULT']['source']

        if ".txt" in source:
            sourceInput = open(source, "r").read()
        elif ".db" in source:
            con = sqlite3.connect(source)
            cur = con.cursor()
            tableList = [a for a in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")] # example
            sourceInput = ' '.join(tableList)
        return sourceInput 
    
class Sanitizer():
    def sanitizer(string):
        return re.sub("tab","____",sourceInput.lower())

class Calculator():
    def char_with_freq(string):
        print("\nSanitized text:",string)
        d = Counter(string)
        print("\nFreq of alphabet:", end = " ")
        for i in d:
            print(i+str(d[i]), end = " ")

if __name__ == '__main__':
    if len(sys.argv) > 2:
        myLogger = Logger(sys.argv[2])
        sys.stdout = myLogger
    else:
        config = configparser.ConfigParser()
        config.read('config.ini')
        source = config['DEFAULT']['target']
        myLogger = Logger(source)
        sys.stdout = myLogger
    
    sourceInput = InitialOne.initial_source()
    sanitizedTxt = Sanitizer.sanitizer(sourceInput)
    Calculator.char_with_freq(sanitizedTxt)

