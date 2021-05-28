#!/usr/#!/usr/bin/env python
#coding=utf-8

__author__ = 'Karl Boulais'

from argparse import ArgumentParser


from server import Server
from view import View

def argParse():
    p = ArgumentParser()

    return p


def main():
    v = View()
    s = Server()
    s.main()

    v.interractiveMode(s)


if __name__ == "__main__":
   main()