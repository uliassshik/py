"""
Моя первая программа
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# И
# Импорт пакетов

import math
import numpy
import matplotlib.pyplot as mpp

# Эта программа рисует график функции, заданной выражением ниже
# Главная функция

if __name__=='__main__':
    arguments = numpy.arange(0, 200, 0.1)
    mpp.plot(
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments]
    )
    mpp.show()
