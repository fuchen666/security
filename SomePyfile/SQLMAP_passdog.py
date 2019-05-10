#!/usr/bin/env python
#coding=utf-8

"""

developers (sven)


"""

import random       # 随机数

import string



from lib.core.enums import PRIORITY



__priority__ = PRIORITY.LOW



def tamper(payload, **kwargs):

    

    retVal = ""



    if payload:

        for i in range(len(payload)):

            if payload[i].isspace():

                retVal += "/*0a**/" 

            elif payload[i] == '#' or payload[i:i + 3] == '-- ':

                retVal += payload[i:]

                break

            else:

                retVal += payload[i]



    return retVal
