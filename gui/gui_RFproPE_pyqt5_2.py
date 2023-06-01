# ---------------------------------------------------------------------------

# ------------------------------- logger setup start ------------------------
import logging

logfile = "test.log"
logFormatter = logging.Formatter(
    "%(asctime)s %(filename)s at line %(lineno)s, "
    "logger='%(name)s'@%(levelname)s:  %(message)s"
)

logFileHandler = logging.FileHandler(logfile, "w")
logFileHandler.setLevel(logging.DEBUG)
logFileHandler.setFormatter(logFormatter)

logStreamHandler = logging.StreamHandler()
logStreamHandler.setLevel(logging.DEBUG)
logStreamHandler.setFormatter(logFormatter)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# logger.addHandler(logFileHandler)
logger.addHandler(logStreamHandler)


# ------------------------------- logger setup end --------------------------
def print_hi(f):
    """Wrapper for print"""

    def inner(args):
        print("before")
        result = f("Hi " + args)
        print("after")
        return result

    return inner


@print_hi
def print_name(name):
    print(name)


print_name("'your name here'")

# class OrderedDict:
#     """An ordered dictionary test"""
#     def __init__(self, dictionary=None):
#         self.__keys = []
#         self.__dict = ()
#         if dictionary is not None:
#             if isinstance(dictionary, OrderedDict):
#                 self.__dict = dictionary.__dict.copy()
#                 self.__keys = dictionary.__keys[:]
#             else:
#                 self.__dict = dict(dictionary).copy()
#                 self.__keys = sorted(self.__dict.keys())


# def addition(a, b):
#     return a + b

# a=dict(a=1, b=2)
# if "a" in a:
#     print("ok")
# else:
#     print("Nok")

# ---------------------------------------------------------------------------


# # ---------------------------------------------------------------------------
# class Length(object):
#     """This class holds lengths.

#     A length is an amount and a unit. Internally all lengths are held as
#     meters, but lengths can be created using any common standard unit,
#     and can be retrieved converted to any of the supported units.
#     """

#     convert = dict(
#         mi=621.371e-6,
#         miles=621.371e-6,
#         mile=621.371e-6,
#         yd=1.094,
#         yards=1.094,
#         yard=1.094,
#         ft=3.281,
#         feet=3.281,
#         foot=3.281,
#         inches=39.37,
#         inch=39.37,
#         mm=1000,
#         millimeter=1000,
#         millimeters=1000,
#         millimetre=1000,
#         millimetres=1000,
#         cm=100,
#         centimeter=100,
#         centimeters=100,
#         centimetre=100,
#         centimetres=100,
#         m=1.0,
#         meter=1.0,
#         meters=1.0,
#         metre=1.0,
#         metres=1.0,
#         km=0.001,
#         kilometer=0.001,
#         kilometers=0.001,
#         kilometre=0.001,
#         kilometres=0.001,
#     )
#     convert["in"] = 39.37
#     numbers = frozenset("-+0123456789.eE")

#     def __repr__(self):
#         return "Length('%.6fm')" % self.__amount

#     def __str__(self):
#         return "%.3f" % self.__amount

#     def __init__(self, length=None):
#         if length is None:
#             self.__amount = 0.0
#         else:
#             digits = ""
#             for i, char in enumerate(length):
#                 if char in Length.numbers:
#                     digits += char
#                 else:
#                     self.__amount = float(digits)
#                     unit = length[i:].strip().lower()
#                     break
#             else:
#                 logger.exception(
#                     f"'{length}', please provide an amount+unit, e.g. '10km'"
#                 )
#                 return
#             self.__amount /= Length.convert[unit]

#         if self.__amount:
#             logger.debug(str(digits) + str(unit))

#     def set(self, length):
#         self.__init__(length)

#     def to(self, unit):
#         return self.__amount * Length.convert[unit]

#     def copy(self):
#         other = Length()
#         other.__amount = self.__amount
#         return other

#     @staticmethod
#     def units():
#         return Length.convert.keys()


# Pout = Length("47.654321km")
# logger.debug(repr(Pout))
# logger.debug(str(Pout))
# # logger.debug(str(Pout.to("meters")) + "m")
# # Pin = Pout.copy()
# # logger.debug(Pin)
# # logger.debug(list(Pin.units()))

# # ---------------------------------------------------------------------------


# # ---------------------------------------------------------------------------
# import logging

# """
# https://www.youtube.com/watch?v=jxmzY9soFXg

# DEBUG: Detailed information, typically of interest only when diagnosing
# problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative
# of some problem in the near future (e.g. ‘disk space low’).
# The software is still working as expected.
# !--- WARNING is the default logging setting                          ---!
# !--- meaning logging will log WARNING and above (ERROR and CRITICAL) ---!

# ERROR: Due to a more serious problem, the software has not been able to
# perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable
# to continue running.# debug
# """
# # print(logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL)
# logfile = "test.log"
# logFormatter = logging.Formatter(
#     "%(filename)s at line %(lineno)s, logger='%(name)s'@%(levelname)s:  %(message)s"
# )

# logFileHandler = logging.FileHandler(logfile, "w")
# logFileHandler.setLevel(logging.DEBUG)
# logFileHandler.setFormatter(logFormatter)

# logStreamHandler = logging.StreamHandler()
# logStreamHandler.setLevel(logging.ERROR)
# logStreamHandler.setFormatter(logFormatter)


# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logFileHandler)
# logger.addHandler(logStreamHandler)


# # logging.basicConfig(
# #     filename="test.log",
# #     level=logging.DEBUG,
# #     format="%(asctime)s:%(levelname)s:%(message)s",
# # )


# def add(x, y):
#     """Add Function"""
#     return x + y


# def subtract(x, y):
#     """Subtract Function"""
#     return x - y


# def multiply(x, y):
#     """Multiply Function"""
#     return x * y


# def divide(x, y):
#     """Divide Function"""
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         logger.exception("Tried to divide by zero")
#     else:
#         return result


# if __name__ == "__main__":
#     num_1 = 60
#     num_2 = 10

#     add_result = add(num_1, num_2)
#     logger.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))

#     sub_result = subtract(num_1, num_2)
#     logger.info("Sub: {} - {} = {}".format(num_1, num_2, sub_result))

#     mul_result = multiply(num_1, num_2)
#     logger.warning("Mul: {} * {} = {}".format(num_1, num_2, mul_result))

#     div_result = divide(num_1, num_2)
#     logger.error("Div: {} / {} = {}".format(num_1, num_2, div_result))

#     add_result = add(num_1, num_2)
#     logger.critical("Add: {} + {} = {}".format(num_1, num_2, add_result))

# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# class Baloon:
#     unique_colors = set()

#     def __init__(self, color):
#         self.color = color
#         Baloon.unique_colors.add(color)

#     # @staticmethod
#     def uniqueColors(self):
#         return Baloon.unique_colors


# b = Baloon("Blue")
# c = Baloon("Red")
# print(*b.unique_colors)
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# class Rectangle:
#     """
#     This class represents chairs
#     width, height
#     """

#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def _width(self):
#         return self.__width

#     def _setWidth(self, width):
#         self.__width = width

#     def _height(self):
#         return self.__height

#     def _setHeight(self, height):
#         self.__height = height

#     def _area(self):
#         return self.width * self.height

#     def cmp(self, a, b):
#         print("cmp test")
#         return a - b
#         # return (int(a) > int(b)) - (int(a) < int(b))

#     def __cmp__(self, other):
#         print("__cmp__ test")
#         if self.width != other.width:
#             return self.cmp(self.width, other.width)
#         return self.cmp(self.height, other.height)

#     def __repr__(self):
#         s = (
#             f"Rectangle of width={self.width} and height={self.height} "
#             + f"has an area={self.area}"
#         )
#         return s

#     width = property(fget=_width, fset=_setWidth)
#     height = property(fget=_height, fset=_setHeight)
#     area = property(fget=_area)


# r1 = Rectangle(5, 2)
# r2 = Rectangle(8, 4)
# r1.width += 1
# print(r1)
# print(r2)
# ---------------------------------------------------------------------------


# def getWidth(self):
#     return self.width

# def setWidth(self, width):
#     self.width = width

# def getHeight(self):
#     return self.height

# def setHeight(self, height):
#     self.width = height

# def area(self):
#     return self.width * self.height


# rect = Rectangle(50, 10)
# print(f"Area:{rect.area}, Height:{rect.height}, Width:{rect.width}")
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# filehandle = open("./gui/gui_settings.py", "r")
# try:
#     print(*filehandle.read().split(" "))
#     # for line in filehandle():
#     #     print(line)
# finally:
#     filehandle.close()
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# x = 1
# assert x > 1, "x=" + str(x) + ", not > 1"
# x += 1
# assert x > 1
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# from gui_settings import RED, BLACK
# import logging

# from gui_settings import *
# from PyQt5.QtCore import *
# import sys


# class Accident(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def print_exception(self):
#         print("User defined exception:", self.msg)


# try:
#     raise Accident("oops")
# except Accident as e:
#     e.print_exception()
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# values = [10, 5, 8, 3, 0, 2, 6, 7, "Hello"]

# for value in values:
#     try:
#         print(10 / int(value))
#     except (ValueError, ZeroDivisionError) as e:
#         pass
#         print("`" + str(value) + "` caused an error: " + str(e))
#     except Exception as e:
#         logging.exception(e)
#     else:
#         print("no exception occurred. Value:", value)
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# def action(button):
#     print("Pressed button:", button)
#
#
# if sys.version_info[:2] < (3, 5):
#
#     def partial(func, arg):
#         def callme():
#             return func(arg)
#
#         return callme
#
# else:
#     from functools import partial
#
#
# btn1 = partial(action, BLACK)
# btn2 = partial(action, RED)
#
# btn1()
# btn2()
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# import sys
#
# pythonCurrentVersion = sys.version_info[:2]
# pythonRequiredVersion = (3, 12)
# if height <= pythonRequiredVersion:
#     print(
#         "Your Python version is v" +
#         str(pythonCurrentVersion[0]) + "." + str(pythonCurrentVersion[1]),
#         "which is < v" +
#         str(pythonRequiredVersion[0]) + "." + str(pythonRequiredVersion[1]),
#     )
#     print("Please upgrade")
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# """Returns a list of loats
#
# frange(start, stop, inc)    # start=arg0, stop=arg1, inc=arg2
# frange(start, stop)         # start=arg0, stop=arg1, inc=1.0
# frange(stop)                # start=0.0, stop=arg0, inc=1.0
# """

# date = QDate.currentDate().toString("dddd, MMM dd, yyyy")
# if date:
#     print(date)
# else:
#     pass

# myLUT = dict(a=(1, 2), b=(2, 3), c=(3, 4), d=(4, 5))
# for key in sorted(myLUT, reverse=True):
#     print(f"{key} = {myLUT[key]}")
# print(f"{key}={myLUT[key][0]}-{myLUT[key][1]}")

# x = [x for x in range(10) if not (x % 2) ]
# print(x)

# x = list((x for x in range(10)) if True else 11)
# print(x)

# fives = (x for x in range(50) if x % 5 == 0)
# print(*fives)


# def frange(arg0, arg1=None, arg2=None):
#     start = 0.0
#     inc = 1.0
#     if arg2 is not None:
#         start = arg0
#         stop = arg1
#         inc = arg2
#     elif arg1 is not None:
#         start = arg0
#         stop = arg1
#     else:
#         stop = arg0
#
#     result = []
#     while start < (stop - (inc / 2.0)):
#         result.append(start)
#         start += inc
#     return result
#
#
# print(frange(0, 10))
# print(frange(5))
# ---------------------------------------------------------------------------
