#WAP to get filepath from command line, read the contents of file and print

import sys

def read_file(filepath):
    try:
        f = open(filepath,'r')
        data = f.read()
        f.close()
        print(data)
        return data
    except FileNotFoundError:
        print("invalid args")
    except Exception as e:
        print("Unknown error: " + str(e))



if __name__=="__main__":

    args = sys.argv[1:]
    if not len(args) == 1:
        print("Invalid command args")
        sys.exit(0)

    path = args[0]
    resp = read_file(path)
    print(resp)

