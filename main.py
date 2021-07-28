from PIL import Image, ImageFilter
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)
import sys
import os.path
from os import path
def main():
   print("BLUR\nCONTOUR\nDETAIL\nEDGE_ENHANCE\nEDGE_ENHANCE_MORE\nEMBOSS\nFIND_EDGES\nSMOOTH\nSMOOTH_MORE\nSHARPEN")

   img = get_file()

   image = get_filter(img)

   imagename = getname()

   print(imagename)
   
   image.save(imagename) 

   image.show()

   print("Image filtered")

def getname():
   name = ""
   j = 1
   i = 0
   while j < 2:
      
      i = i + 1
      name = "image" + str(i) + ".jpg"
      if path.exists(name):
         continue
      j = 2
   return name

def get_filter(img):

   filt = input("Enter filter: ")

   filt = filt.lower()
   image = img
   if filt == "blur":
      image = img.filter(ImageFilter.BLUR)
   elif filt == "contour":
      image = img.filter(ImageFilter.CONTOUR)
   elif filt == "detail":
      image = img.filter(ImageFilter.DETAIL)
   elif filt == "edge_enhanced":
      image = img.filter(ImageFilter.EDGE_ENHANCE)
   elif filt == "edge_enhanced_more":
      image = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
   elif filt == "emboss":
      image = img.filter(ImageFilter.EMBOSS)
   elif filt == "find_edges":
      image = img.filter(ImageFilter.FIND_EDGES)
   elif filt == "smooth":
      image = img.filter(ImageFilter.SMOOTH)
   elif filt == "smooth_more":
      image = img.filter(ImageFilter.SMOOTH_MORE)
   elif filt == "sharpen":
      image = img.filter(ImageFilter.SHARPEN)
   else:
      print("Filter does not exist")
      
      return get_filter(img)

   return image

def get_file():
   imgloc = input("Enter image location: ")
   img = ""
   try:
      img = Image.open(imgloc.upper())
   except:
      print("File does not exist")
      get_file()

   return img

main()