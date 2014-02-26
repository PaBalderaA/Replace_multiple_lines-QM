import os
from unipath import Path

BASE_PATH = Path(os.path.abspath(__file__)).ancestor(2)
DATA_PATH = BASE_PATH.child('test_data')
filenames = os.listdir(str(DATA_PATH))

for filename in filenames:

    try:
        path = DATA_PATH + '/' + filename
        print path
        #f = open(path, 'rw')
        #f.write()
        #f.close()
    except:
        print 'Error'
