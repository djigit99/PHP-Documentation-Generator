from .controller import Controller
from os.path import isfile, isdir, dirname, abspath, exists
from os import sep, makedirs, umask
import argparse
import logging


class Flags(object):
    pass


def main():
    with open('php_doc_gen.log', 'w') as f:
        pass
    logging.basicConfig(filename='php_doc_gen.log', level=logging.INFO)
    parser = argparse.ArgumentParser(description='PHP Documentation Generator')
    parser.add_argument("p", type=str, help="Path to directory or file being documented")
    parser.add_argument("-t", required=False, type=str, help="Path to directory where to store documentation files(default: current directory)")
    parser.add_argument("-r", required=False, action='store_true', help="recursive mode")
    parser.parse_args(namespace=Flags)

    if isfile(Flags.p):
        if not Flags.t:
            Flags.t = dirname(Flags.p)
        elif not isdir(Flags.t):
            print('target directory not found, please enter the correct path')
            exit(1)
        else:
            pass
        Controller(Flags.p, Flags.t)
    elif isdir(Flags.p):
        if not Flags.t:
            Flags.t = Flags.p
        else:
            pass
        Flags.p = abspath(Flags.p)
        Flags.t = abspath(Flags.t)
        print(Flags.p)
        if Flags.p.endswith(sep):
            Flags.p = Flags.p[:-1]
        if Flags.t.endswith(sep):
            Flags.t = Flags.t[:-1]
        if not exists(Flags.t):
            try:
                original_umask = umask(0)
                makedirs(Flags.t, 0o777, True)
            finally:
                umask(original_umask)
        if Flags.r:
            Controller(Flags.p, Flags.t, True, True)
        else:
            Controller(Flags.p, Flags.t, True)
    else:
        print('file or directory not found, please enter the correct path')
        exit(1)


if __name__ == '__main__':
    main()
