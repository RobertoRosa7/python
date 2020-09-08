# -*- coding: utf-8 -*-

import openpyxl
import os
import PyPDF2

os.chdir('/home/mendoza/Documentos/udemy/python/read_excel')


def debug(**Kwargs):
  for index, value in Kwargs.items():
    print('%s -> %s' %(index, value))


def debug_type(**Kwargs):
  for index, value in Kwargs.items():
    type('%s -> %s' %(index, value))


def excel_read():
  """
  Reading Excel Documents
  """

  workbook = openpyxl.load_workbook('excel_document.xlsx')
  sheet = workbook.get_sheet_by_name('Sheet1')
  # all_sheets = workbook.get_sheet_names()

  # cell = sheet['A1']
  print(str(sheet['A1'].value))

  debug(A1=str(sheet['A1'].value), B1=str(sheet['B1'].value),C1=str(sheet['C1'].value))

  # Loop
  for i in range(1, 8):
    print(i, sheet.cell(row=i, column=2).value)


def excel_edit():
  """
  Editing Excel Document
  """

  wb = openpyxl.Workbook()
  sheet1 = wb.get_sheet_by_name('Sheet')
  sheet1['A1'] = 24
  sheet1['B1'] = 'Hello'
  wb.save('excel_document2.xlsx')
  sheet2 = wb.create_sheet()
  sheet2.title = 'My new sheet name'
  wb.create_sheet(index=0, title='My first sheet renamed')
  debug(st=wb.get_sheet_names())
  wb.save('excel_document2.xlsx')


def pdf_read():
  """
    Read PDF File
    Download: http://autbor.com/meetingminutes1.pdf
  """

  pdf_file = open('meetingminutes1.pdf', 'rb')
  reader = PyPDF2.PdfFileReader(pdf_file)
  # reader.numPages
  # page = reader.getPage(0)
  # debug(pages=reader.numPages, text=page.extractText())

  for page_num in range(reader.numPages):
    debug(pages=reader.getPage(page_num).extractText())

  pdf_file.close()

pdf_read()