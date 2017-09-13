def str_to_chinese(l):
    p1 = l[:2]
    p2 = l[2:]
    return bytes([int(p1, 16), int(p2, 16)]).decode('gb2312')


def main():
    for code in open('hello.txt').readlines():
        code = code.strip()
        print(code, str_to_chinese(code))


# str_to_chinese('B0A1') => '啊'
# http://www.nlpr.ia.ac.cn/databases/handwriting/Online_database.html, Look for "Tag Code (GB)"

if __name__ == '__main__':
    main()
