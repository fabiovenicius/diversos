from distutils.core import setup
import py2exe

setup(windows=[{"script" : "pessoa.pyw"}], options={"py2exe" : {"includes" : ["sip"]}})