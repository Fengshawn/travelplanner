"""
@author:ZRM
@file:get_pdf.py
@time:2020/02/25
"""
import pdfkit

config = pdfkit.configuration(wkhtmltopdf='D:\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')


def get_file():
    temp = pdfkit.from_string('You choose to go china honkong  zhejiang1', "1231t1.pdf", configuration=config)