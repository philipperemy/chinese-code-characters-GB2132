import sys


def gb2312_to_character(l):
    return bytes([int(l[:2], 16), int(l[2:], 16)]).decode('gb2312')


if __name__ == '__main__':
    if sys.version_info < (3, 0):
        sys.stdout.write("Sorry, requires Python 3.x, not Python 2.x\n")
        sys.exit(1)
    if len(sys.argv) != 2:
        sys.stdout.write('Please specify a GB2312 code. Example is B1A1.\n')
        sys.exit(1)
    print(gb2312_to_character(sys.argv[1]))
