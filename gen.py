#!/usr/bin/python
# -*- coding: utf-8 -*-
# © 2014 WTFPL – Do What the Fuck You Want to Public License.
# Author: Richard Marko <rmarko@fedoraproject.org>

import argparse
import itertools

weights = [6, 3, 7, 9, 10, 5, 8, 4, 2, 1]


def weighted_sum(num):
    ' Calculate a weighted sum of the `num` input '

    return sum(map(lambda (x, y): x * int(y),
                   zip(weights, str(num))))


def is_mod11(num):
    ' Check if `num` input fits modulo 11 '
    return (weighted_sum(num) % 11) == 0


def candidates(parts):
    '''
    Permutate `parts` and check if their concatenation results in possible
    account number (more than 8 characters, less than 10, fits mod11)
    '''

    out = set()

    for perm in itertools.permutations(parts):
        c = ''
        for part in perm:
            c += part
            if len(c) >= 8:
                break

        if len(c) > 10:
            continue

        if is_mod11(c):
            out.add(c)

    return sorted(list(out), key=len)


if __name__ == '__main__':
    # self-test
    assert is_mod11('777133742')

    parts = ['1337', '42', '777', '13', '555']
    assert len(candidates(parts)) == 5

    # cmdline
    p = argparse.ArgumentParser()
    p.add_argument('--check', action='store_true', default=False,
                   help='only check if input number fits mod11')

    p.add_argument('inputs',
                   metavar='N', type=int, nargs='+',
                   help='number to check or list of parts to work with')

    args = p.parse_args()
    if args.check:
        for n in args.inputs:
            res = 'invalid'
            if is_mod11(n):
                res = 'valid'
            print('{0} is {1}'.format(n, res))

    else:  # gen. candidates
        res = candidates(map(str, args.inputs))
        for part in res:
            print(part)
