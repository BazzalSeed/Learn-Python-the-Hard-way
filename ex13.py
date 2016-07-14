"""ex11,Parameters,unpacking,variables."""
from sys import argv


def main():
    """main function."""
    try:
        first, second, third = argv
    except:
        print "not correct number of arguments"
        return
    print "first is %s, second is %s, third is %s" % (first, second, third)

if __name__ == '__main__':
    main()
