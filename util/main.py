import os
from unipath import Path


BASE_PATH = Path(os.path.abspath(__file__)).ancestor(2)
DATA_PATH = BASE_PATH.child('test_data')
NEW_DATA_PATH = BASE_PATH.child('test_new_data')


def read_file(filepath):
    try:
        f = open(filepath, 'rU')
        text = f.read()
        f.close()
        return text
    except:
        print 'Error'

text_to_append = BASE_PATH.child('util').child('to_replace.txt')
text_to_append = read_file(text_to_append)
common = "0  1"

filenames = os.listdir(DATA_PATH)
for filename in filenames:
    flag = 0
    try:
        test = DATA_PATH + '/' + filename
        newtest = NEW_DATA_PATH + '/' + filename
        with open(test) as old, open(newtest, 'w') as new:
            for line in old:
                if common in line:
                    flag = 1
                    new.write(line)
                else:
                    if flag == 1:
                        new.write(text_to_append)
                        break
                    else:
                        new.write(line)
    except:
        print 'Error'
