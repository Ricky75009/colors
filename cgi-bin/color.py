#!/usr/bin/env python3

import cgi
import os
path="/Users/macbook/Desktop/Roman/Scolaire/CODE/Projects/8- SE_foundation/color_checker/color.txt"

form = cgi.FieldStorage()

v_color= form.getvalue("color")

file_data = open(path, 'r')
colors_in_list= file_data.read()


if v_color in colors_in_list:

	print('''<!DOCTYPE html>
   <html lang="en">
   <head>
    <title>color</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <!-- import the webpage's stylesheet -->
    <link rel="stylesheet" href="/style.css">
    
    <!-- import the webpage's javascript file -->
    <script src="/script.js" defer></script>
   </head>  
  

   <body style="background-color:%s">
    <h1 styler=>%s is a color!</h1>
    
   </body>
   </html>'''%(v_color,v_color ))

else:
  print('''<!DOCTYPE html>
   <html lang="en">
   <head>
    <title>No color</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <!-- import the webpage's stylesheet -->
    <link rel="stylesheet" href="/style.css">
    
    <!-- import the webpage's javascript file -->
    <script src="/script.js" defer></script>
   </head>  
   <style>

   <body>
    <h1>%s is not a color!</h1>
    
   </body>
   </html>'''% v_color)