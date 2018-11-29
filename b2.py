import csv

with open("demofile.txt", "a") as f:
    f.write("Now the file has one more line!")


#with open(r'blacklist.csv', 'a') as f:
#    writer = csv.writer(f)
#    writer.writerow("hello")
