# -*- coding: utf-8 -*-
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("sheetscred.json",scope)
client = gspread.authorize(creds)
sheet_high = client.open("spreadsheet123").sheet1
sheet_ment = client.open("spreadsheet1234").sheet1
sheet_ment.insert_row(["hello","boomer"])
print("Success!")
careers = {1: 'CS' , 2: 'MDL' , 3: 'BIO' , 4: 'CHEM', 5: 'ENG'}

categories_mentors = []
categories_hs = []
#input of 1 = student
#input of 2 = mentor

#input of 1.1 = create
#input of 1.2 = update
#input of 1.2.1 = 

def create_attributes_hs(username, name, age, email, PhoneNumber, DesiredCareer, Bio):
  #Username: String 
  #Name: String
  #Age: Int
  #Email: String
  #Phone #: Int
  #Desired Career: String
  #Bio: String
  sheet_high.insert_row([username, name, age, email, PhoneNumber, DesiredCareer, Bio])
  

def update_attribututes_hs(category, value, username, sheet1_2):
  #category = number of column minus open
  #value =new value to change to
  #username = username to find out where they are on sheet
  #sheet1_2 = 1 or 2 for mentor or highschool
  counter = 1
  if sheet1_2 == 1:
    correct_sheet = sheet_high
  else:
    correct_sheet = sheet_ment
  #row,column(y,x)
  
  while correct_sheet.cell(counter,1) != username:
    counter+= 1
  
  #counter -= 1  
  user_list= sheet_high.row_values(counter)
  sheet_high.delete_row(counter)
  user_list[category] = value
  sheet_high.insert_row(user_list)

def create_attributes_m(username, name, Age, Email, Phone, Position, Bio):

  sheet_ment.insert_row([username, name, Age, Email, Phone, Position, Bio])





'''
Mentors: Career Postion, Name, Age, Email, Phone, BIO, Photo
High Schoolers: Name, Age, Email, Phone #, Desired Career
'''








  

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#access data
'''
  print(sheet.get_all_records())#returns all

  print(sheet.row_values(2))#returns whole row
 
  print(sheet.cell(2,2))#row,column(y,x)
  #print(sheet.col_values(2))#returns whole column

  #insert data
  #for num in range(20):
      #sheet.insert_row([1324,132133,144,3413,213213,3465],2)   

 for num in range(1): 
    sheet.insert_row([random.randint(100,1000),random.randint(100,1000),random.randint(100,1000),random.randint(100,1000),random.randint(100,1000),random.randint(100,1000)],2)

    #two arguments, first a list with each value going to the corresponding column index, then the second value being row number
    #if the row number already has values, then everything below it will be pushed down

  #delete row
'''