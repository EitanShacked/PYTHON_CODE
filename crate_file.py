#os.makedir
print("                                                           (file_creator)   ")
print("##############################################################")
print("#programing by: eitan shacked, alex shacked")
print("#stop - stop the program")


list1 = []
stop = "stop"
fpf = "/users/es/file1.txt"

while True:
    inp = input("#plase write, some thing: ")
    if stop == inp:
        print("exit")
        break
    else:
        list1.append(inp)
fl = open(fpf, "a+")
for i in list1:
    fl.write(i + "\n")
fl.close()

fl2 = open(fpf)
lines = fl2.readlines()
for l in lines:
    print(l[:-1])