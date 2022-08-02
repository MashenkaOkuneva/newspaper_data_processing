# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 14:23:51 2019

@author: mOkuneva
"""

def worker_bigr_trigr(obj):
    obj.tagger()
    obj.bigr()
    obj.trigr()
    return obj.bigr, obj.trigr