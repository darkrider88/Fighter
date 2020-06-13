#!/usr/bin/python
import sys, getopt
import hashlib

def main(argv):
    dict_file = '' #file location
    password = '' #just the hash
    try:
        opts, args = getopt.getopt(argv,"hd:p:")
    except getopt.GetoptError:
        print('fighter.py -d <Dictionary> -p <pass hash>')
        sys.exit(1)
    
    for opt, arg in opts:
        if opt == '-h':
           print('fighter.py -d <Dictionary> -p <pass hash>')
           sys.exit(2)
        if opt == '-d':
            dict_file = arg
        if opt == '-p':
            password = arg

    #opening dictionary file
    try:
        f = open(dict_file,'r')
    except IOError:
        print('Invalid file')
        sys.exit()

    print("[*]Trying to crack the password!")
    print('[*]Please wait...')
    
    for lines in f:
        lines = lines.replace('\n','')
        hash_pass = hashlib.md5()
        hash_pass.update(lines)
        x = hash_pass.hexdigest()
        if x == password:
            print('[*]Password found: {}'.format(lines))
        
        if not lines:
            sys.exit()

    f.close()

if __name__ == "__main__":
    main(sys.argv[1:])