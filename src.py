#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 23:10:10 2018

@author: tuna
"""

import time


def time_statistics(fun):
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = fun(*args, **kwargs)
        t1 = time.time()
        print("Total time running %s: %s seconds" % (fun.__name__, str(t1 - t0)))
        return result

    return function_timer


def retry(retries=3):
    def _retry(fun):
        def wrapper(*args, **kwargs):
            for _ in range(retries):
                try:
                    return fun(*args, **kwargs)
                except Exception as e:
                    print("@", fun.__name__, "->", e)

        return wrapper

    return _retry