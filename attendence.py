import argparse
from datetime import datetime

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
	help="detector name")

args = vars(ap.parse_args())

def markAttendence(name):
    with open('Attendence.csv', '+r') as f:
        myDateList = f.readlines()
        nameList = []
        for line in myDateList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name}, {dtstring}')
            
markAttendence(args["name"])