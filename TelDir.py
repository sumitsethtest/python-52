""" telephone directory with data base 
it create text file for name and phone number and update it every time when the code is run"""
def add():# add data
    ap = open("dataBase.txt",'a')
    ap.write(input("enter name ")+"\t")
    ap.write(input("enter mobile number ")+"\n")
    print("data is saved")
    ap.close()
def find(name):# search data
    """enter name as string to find """
    rp= open("dataBase.txt",'r')
    while(True):
        data=rp.readline()
        temp = data.split()
        if (len(data) == 0):
            print("data not found")
            break
        if(temp[0]==name):
            print("data found ",data)
            break
    rp.close()
while(True):# main function
    otp=int(input("enter option as per choice\n1\t add\n2\tfind\n3\texit\n"))
    if(otp==1):
        add()
    elif(otp==2):
        find(input("enter name "))
    elif(otp==3):
        break
    else:
        print("worng choice")