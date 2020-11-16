import csv

file = open('demo.csv','w',newline='') # newline 能控制换不换行

w = csv.writer(file)
w.writerow(['name','age','score'])

file.close()