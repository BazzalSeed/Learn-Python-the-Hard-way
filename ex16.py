"""Reading/writing Files."""
# from sys import argv


# def main():
#     """Main function."""
#     try:
#         script, filename = argv
#     except:
#         print "wrong number of arguments passed in"
#         return
#     with open(filename, 'w') as file:
#         file.write(raw_input("what you want to say and saved?"))

def main():
    """main function."""
    with open("test") as inputfile:
        indata = inputfile.read()
    with open("outputtest", 'w') as outputfile:
        outputfile.write(indata)

if __name__ == '__main__':
    main()
