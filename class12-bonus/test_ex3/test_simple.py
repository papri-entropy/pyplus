#!/usr/bin/env python

def my_add(x, y):
    return x + y

def my_mul(x, y):
    return x * y

def test_my_add():
    assert my_add(10, 12) == 22

def test_my_mul():
    assert my_mul(4, 5) == 20
