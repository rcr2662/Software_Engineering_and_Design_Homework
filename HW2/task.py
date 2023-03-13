import testCustomEncrypt
def main():
    file = open("database.txt", "r")
    while(True):
        line = file.readline()
        split_line = line.split()
        userID = split_line[0]
        password = split_line[1]
        

