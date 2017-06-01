import serial
import csv
arduino = serial.Serial('/dev/cu.usbmodem1421', 9600, timeout=.1)
while True:
    num = 1
    i=0
    var = ""
    for num in range(0,4):
        num+=1
        data = arduino.readline()[:-2] 
        var=var+data
        i+=1
        if var!="" and i==4 and len(var)>=11:
            print var
            with open('cardatabase2.csv') as CSVfile:
                readCSV = csv.reader(CSVfile, delimiter=',')
                for x in readCSV:
                    if x[2]==var:
                        print "your current balance is "+x[4]
                        print "an amount of 50 will be deducted from your account"

    
