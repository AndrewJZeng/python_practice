import os, sys

def main(srcfile, desfile, n_space):
    with open(srcfile) as readfh:
        with open(desfile, 'w') as writefh:
            content = readfh.readlines()

            for x in content:
                line = x[n_space:]
                writefh.write(line)
                



if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'Usage: %s srctxt despy space_number' % sys.argv[0]
    else:
        main(sys.argv[1], sys.argv[2], int(sys.argv[3]))