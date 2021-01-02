"""
                                        MORSE CODE CONVERTER AND TRANSLATOR
                                                                 - SAHAI JORDI ALAN A
"""

from tkinter import *

root = Tk()
root.title('Morse Code Converter/Translator')
root.resizable(0, 0)
root.geometry("371x125")

MorseCode={'A':'.-', 'B':'-...', 
          'C':'-.-.', 'D':'-..', 'E':'.', 
          'F':'..-.', 'G':'--.', 'H':'....', 
          'I':'..', 'J':'.---', 'K':'-.-', 
          'L':'.-..', 'M':'--', 'N':'-.', 
          'O':'---', 'P':'.--.', 'Q':'--.-', 
          'R':'.-.', 'S':'...', 'T':'-', 
          'U':'..-', 'V':'...-', 'W':'.--', 
          'X':'-..-', 'Y':'-.--', 'Z':'--..', 
          '1':'.----', '2':'..---', '3':'...--', 
          '4':'....-', '5':'.....', '6':'-....', 
          '7':'--...', '8':'---..', '9':'----.', 
          '0':'-----', ', ':'--..--', '.':'.-.-.-', 
          '?':'..--..', '/':'-..-.', '-':'-....-', 
          '(':'-.--.', ')':'-.--.-', ';':'-.-.-.',
          ':':'---...', "'":'.----.', '"':'.-..-.',
          '=':'-...-', '+':'.-.-.', 'x':'-..-',
          '@':'.--.-.', 'Á':'.--.-', 'Ä':'._._',
          'É':'..-..', 'Ñ':'--.--', 'Ö':'---.',
          'Ü':'..--'}

def clear():
     InputEntry1.delete(0,"end")
     DisplayEntry1.delete(0,"end")

def MorseConvertor(Word1):

     Morse1=""

     for i in Word1:
          if i==" ":
               Morse1+="/"
          elif i in MorseCode:
               Morse1+=(" "+MorseCode[i])
          else:
               print("Invalid Character.")

     DisplayEntry1.delete(0,"end")
     DisplayEntry1.insert(0,Morse1)

def MorseTranslator(Morse2):

     Word2=""

     Morse2=Morse2.replace("/"," / ")

     MorseList=Morse2.split(" ")

     for i in MorseList:
          for char,sign in MorseCode.items():
               if i==sign:
                    Word2+=char
               elif i=="/":
                    Word2+=" "
                    break

     DisplayEntry1.delete(0,"end")
     DisplayEntry1.insert(0,Word2)


Input1=Label(root,text="Input : ")
Input1.grid(row=0,column=0)

InputEntry1=Entry(root, width=50)
InputEntry1.grid(row=0,column=1,columnspan=3,sticky=W+E)
InputEntry1.insert(0,"Insert Input Here")

MorseConvertorButton=Button(root, text="Convert To Morse Code", command=lambda: MorseConvertor((InputEntry1.get()).upper()))
MorseConvertorButton.grid(row=1,column=2,sticky=W)

MorseTranslatorButton=Button(root, text="Translate Into Characters", command=lambda: MorseTranslator(InputEntry1.get()))
MorseTranslatorButton.grid(row=1,column=3,sticky=E)

ClearButton=Button(root, text="Clear", command=clear)
ClearButton.grid(row=3,column=2,sticky=E)

Display1=Label(root,text="Output : ")
Display1.grid(row=2,column=0)

DisplayEntry1=Entry(root, width=30)
DisplayEntry1.grid(row=2,column=1,columnspan=3,sticky=W+E)

Name=Label(root,text="Project Done By SAHAI JORDI ALAN A")
Name.grid(row=4,column=2,columnspan=2,sticky=E)

root.mainloop()

"""

Project done by Sahai Jordi Alan

Gui created with tkinter
Gridded everything
Algorithm was self made 
Run-time is very low
Project was given as a challenge

Version History

0.1
     -Morse Convertor

0.2
     -Morse Translator

0.3
     -Supports Special Character

0.4
     -Supports more special character

0.5
     -Added a clear button

"""