import os, sys
import win32print

printer = win32print.OpenPrinter("Generic / Text Only")

job = win32print.StartDocPrinter(printer, 1, ("test of new data", None, "RAW"))

win32print.StartPagePrinter(printer)
win32print.WritePrinter(printer, b"\x1bp\x00\x32\xFA")
win32print.EndPagePrinter(printer)
