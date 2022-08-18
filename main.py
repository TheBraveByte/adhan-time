import  tkinter as tk
from tkinter.constants import E
from openpyxl import load_workbook
import datetime as dt
import calendar
from hijri_converter import convert
import time
from PIL import ImageTk, Image

start= time.time()
root= tk.Tk()
root.title('Adhann Prayer time')
root.geometry('455x700')
root.configure(background="#DEEECA")
root.resizable(False,False)
dataX= load_workbook('data.xlsx')
data =dataX.active

weekday_list=[]
gregorian_date=[]
new_hijri_date=[]

# Setting the window frame for the application
window_label=tk.LabelFrame(root)
frameB=tk.Frame(root, bg = "#255D62", height = 20)
frameB.pack()
frameC=tk.Frame(root,bg= "#558B7E", width = 450, height = 20)
frameC.pack()
frameD= tk.Frame(root, bg="#A7C4BC" ,width = 450, height = 30)
frameD.pack()
frameE=tk.Frame(root, bg = "#DEEECA", width = 450, height = 20)
frameE.pack()
prayer_weekday= data['A']
weekday_list = [x.value for x in prayer_weekday]

#current_time_label=tk.Label(frameB, fg='white', bg = "black", font=('Arial',28, 'bold')).grid(row=0,column=1,padx=10, pady=10)

def todays_date():
  current_day = dt.date.today()
  week_day=calendar.day_name[current_day.weekday()][:3].upper()
  date_now = current_day.strftime(f"{week_day}  %dTH, %B %Y").upper()
  return  date_now

    
# Getting the each five daily prayer time from the XLSX data spreadsheet
def prayer_start_time():

  fajar_start_time =[ str(f_time.value)[:5]+" AM" for  f_time in  data['C'][1:]]
        
  zuhr_start_time =[str(z_time.value)[:5]+" PM" for z_time in data['E'][1:]]
        
  asar_start_time = [str(as_time.value)[:5]+" PM" for as_time in data['F'][1:]]
        
  maghrib_start_time = [str(m_time.value)[:5]+" PM" for  m_time in data['G'][1:]]
        
  isha_start_time = [str(isha_time.value)[:5]+" PM" for isha_time in data['H'][1:]]

  start_time_list=[fajar_start_time, zuhr_start_time, asar_start_time, maghrib_start_time, isha_start_time]
  return start_time_list
      
# Getting the Prayer time on Jumaat day  
def jamaat_prayer_time():
  fajar_prayer_time =[str(fp_time.value)[:5]+" AM" for fp_time in data['I'][1:] ]
        
  zuhr_prayer_time = [ str(zp_time.value)[:5]+" PM" for zp_time in data['J'][1:]]
        
  asar_prayer_time = [str(asp_time.value)[:5]+" PM" for asp_time in data['K'][1:]]
        
  maghrib_prayer_time = [str(mp_time.value)[:5]+" PM"  for  mp_time in data['L'][1:]]
        
  isha_prayer_time = [str(ishaP_time.value)[:5]+" PM" for ishaP_time in data['M'][1:]]

  jamaat_prayer_time= [fajar_prayer_time, zuhr_prayer_time,asar_prayer_time, maghrib_prayer_time,isha_prayer_time]
  return jamaat_prayer_time
 
 
# Matching up the appropriate prayer date with respect to the XSLX data sheet
def set_prayerDays_date():

  prayer_date = data['B']
 
  date_list = [y.value for y in prayer_date]
  date = list(zip(weekday_list, date_list))
  del date[0]

  return date


# Checking to match the current gregorian date and the gregorian  date on the data sheet 
def gregorian_calendar_date():
  #gregorian_date=[]
  for date_count in range(len(set_prayerDays_date())):
    #gregorian_date fr
    date2 = set_prayerDays_date()[date_count][1]
    gregorian_date.append(dt.date.strftime(date2, f"{weekday_list[date_count+1]}  %dth, %B %Y").upper())

  return gregorian_date

gregorian_calendar_date()      
 
 
# Converting the gregorian date to hijri calendar date  
def hijri_date_conversion():
  #new_hijri_date=[]
  for date_count in range(len(set_prayerDays_date())):
    date2=set_prayerDays_date()[date_count][1]
    change_dates = convert.Gregorian.fromisoformat(str(date2)[:10]).to_hijri()
    hijri_dates = f"{change_dates.day} {change_dates.month_name(language='ar')} {change_dates.year}"
    new_hijri_date.append(hijri_dates)
  return new_hijri_date
hijri_date_conversion()

current_time_label = tk.Label(frameB, bg = "#255D62", fg='white', font=('MerriWeather-BoldItalic',28))


# Setting up the current day and time
def current_time():
  hour = time.strftime("%H")
  minutes = time.strftime("%M")
  second = time.strftime("%S")
  current_time_label.config(text=hour + ':' + minutes + ':' + second)
  current_time_label.after(1000, current_time)
  countdown = hour + ':' + minutes + ':' + second
  return countdown

current_time_label.grid(row=0,column=1,padx=10, pady=10)
current_time()


row_index=0
for dates in range(len(gregorian_calendar_date())):
  if todays_date() == gregorian_calendar_date()[dates]:
    row_index=dates
    gregorian_date_label= tk.Label(frameB,  bg = "#255D62",fg='black',font=('MerriWeather', 9, 'bold'), text=f"{gregorian_calendar_date()[row_index]}")
    gregorian_date_label.grid(row=0,column=0,padx=10, pady=10)
    hijri_date_label =tk.Label(frameB, fg='black',  bg = "#255D62",font=('MerriWeather', 9, 'bold'), text=f"0{hijri_date_conversion()[row_index]}")
    hijri_date_label.grid(row=0,column=2,padx=10, pady=10)

print(row_index)




def pack_window():
  root.mainloop()


#  * the first frame will contain the updated dates and time in both gregorian #data and islamic dates as well
 # * the second frame will contain 3 constant heading in a row, 5 constant values #in the 0 column but the column 1 & 2 will changes with 
 #   respect to the CSV data available
 # * the third frame will contain 4 constant value and constant time for only 3 except 1 
 # * the fourth frame will contain  the social media logo ,username and the name of the mosque and  logo of the mosque


  #**********************************************************************************************************************
#FFEACA
#334257
#476072
#548CA8

#Design to label the five daily prayer, prayer time for a the current date
def display_windows():
  
  prayers=tk.Label(frameC,fg="white",bg="#558B7E", text="PRAYERS",font=('Arial',14, 'bold')).grid(row=1,column =0,padx=10, pady=5)

  prayer_begins=tk.Label(frameC,fg="white",bg="#558B7E", text="BEGINNING",font=('Arial',14, 'bold')).grid(row=1,column =1,padx=10)
  
  jamaat=tk.Label(frameC, fg="white", bg="#558B7E", text="PRAYERS" ,font=('Arial',14, 'bold')).grid(row=1,column =2, padx=10, pady=5)

  fajar =tk.Label(frameC, fg ="white",bg="#558B7E",text="فجر \n\nFAJR",font=('Dancing_Script',11,)).grid(row=2,column =0,padx=10, pady=5)
      
  zuhr=tk.Label(frameC,fg="white",bg="#558B7E", text="ظهر\n\nZUHR",font=('Dancing_Script',11)).grid(row=3,column =0,padx=5, pady=10)
  
  asar=tk.Label(frameC,fg="white",bg="#558B7E", text="عصر\n\nASR",font=('Dancing_Script',11)).grid(row=4,column =0,padx=5, pady=10)
  
  maghrib=tk.Label(frameC,fg="white",bg="#558B7E", text="مغرب\n\nMAGHRIB",font=('Dancing_Script',11)).grid(row=5,column =0,padx=5, pady=10)
    
  isha=tk.Label(frameC,fg="white",bg="#558B7E", text="عشاء\n\nISHA",font=('Dancing_Script',11)).grid(row=6,column =0,padx=5, pady=10)


display_windows()
sunrise_time =[str(sr_time.value)[:5] for sr_time in data['D'][1:]]
arabic_translate_time=[['جمعة','سحور','شروق','زوال'],['jummah','Imsak','Sunrise','Zawal'],['13:20','3:09',f'{sunrise_time[row_index+1]}', '12:57']]

def weekly_prayer(arabic_translate_time):
  schedule =arabic_translate_time
  for x in range(len(schedule)):
    for y in range(len(schedule[0])):
      tk.Label(frameD, bg="#A7C4BC",fg="white", text=f"{schedule[x][y]}",font=('Dancing Script',11)).grid(row=7+x, column=y, padx=27, pady = 10)

weekly_prayer(arabic_translate_time)

# Label design for the footer of the application
def foot_frame():
  social_media_icon = ImageTk.PhotoImage(Image.open("social.jpg"), width = 13, height = 15)
  tk.Label(frameE, bg = "#DEEECA", image=social_media_icon).grid(row = 10, column = 0,padx=10, pady=10)
  tk.Label(frameE,fg="black", bg = "#DEEECA", text="مسجد سلام\nMasjid Salaam",font=('Arial',15)).grid(row = 10, column = 1, columnspan=2,padx=10, pady=10)
  tk.Label(frameE, bg = "#DEEECA", image=social_media_icon).grid(row = 10, column = 3,padx=10, pady=10)

foot_frame()



# Checking for current real time with respect to the time in the data sheet
if current_time() == "00:00:00":
  for x in range(len(prayer_start_time())):
    prayer_begin = tk.Label(frameC,fg="white",bg="#558B7E", text=f"{prayer_start_time()[x][row_index+1]}", font=('Arial',15)).grid(row=2, column=1,padx=10, pady=10)

    prayer_jamaat=tk.Label(frameC, fg="white", bg="#558B7E", text=f"{jamaat_prayer_time[x][row_index+1]}", font=('Arial',15)).grid(row=2, column=2,padx=10, pady=10)
    
else:
  for x in range(len(prayer_start_time())):
    prayer_begin = tk.Label(frameC,fg="white", bg="#558B7E",text=f"{prayer_start_time()[x][row_index]}", font=('Arial',15)).grid(row=2+x, column=1,padx=10, pady=10)

    prayer_jamaat=tk.Label(frameC,fg="white", bg="#558B7E", text=f"{jamaat_prayer_time()[x][row_index]}", font=('Arial',15)).grid(row=2+x, column=2,padx=10, pady=10)
  

def NewWindow():
    root2 = tk.Tk()
    root2.title("Adhann Prayer Time")
    root2.geometry('455x705')
    root2.resizable(False,False)
    root2.configure(background="#DEEECA")
    window_label=tk.LabelFrame(root2)
    tk.Label(root2,text = "\n\nMAGHRIB\n AND \n ISHA \n WILL BE \n COMBINE", font=('Arial',50),bg="#DEEECA",fg="green").pack()


# a delay ffor the display window
root.after(10000, NewWindow)


# Display the third page of the application
def third_Page():
  root_3= tk.Tk()
  root_3.title("Adhann Prayer Time")
  root_3.geometry("455x705")
  root_3.resizable(False,False)
  root_3.configure(background="#DEEECA")
  window_label=tk.LabelFrame(root)
  tk.Label(root_3,text="قال رسول الله \nما نقصت صدقة من مال", bg="#DEEECA", padx=140, pady=70,font=('Arial',25)).pack()#.grid(row=0, column=1)
  tk.Label(root_3,text='The Messenger of Allah\n (S.A.W) said: \n"Charity does not\n decrease wealth."',bg="#DEEECA",font=('Arial',25)).pack()
  tk.Label(root_3,text="\n\n**************************************",font=('Arial',10),bg="#DEEECA").pack()
  tk.Label(root_3,text="(Please donate generously)",font=('Tahoma',12,'italic'),bg="#DEEECA").pack()
  tk.Label(root_3,text="\n\n\n\nMasjid Salaam\nAccount\t:   01267001" + "  Sort Code : \n30-00-83",font=('Tahoma',12,'italic'),bg="#DEEECA").pack()


third_Page()




# function for the application to display the last page 
def last_page():
  begin_prayer=prayer_start_time()
  start_prayer=jamaat_prayer_time()
  
  root_4=tk.Tk()
  root_4.title("Adhann Prayer Time")
  root_4.resizable(False,False)
  root_4.configure(background="#DEEECA")
  clock_frame =tk.Frame(root_4,bg= "#558B7E", width = 450, height = 20)
  caution_frame =tk.Frame(root_4,bg= "#558B7E", width = 450, height = 20)
  No_PHONE_FRAME= ImageTk.PhotoImage(Image.open("No Phone Usage1.jpg"), width = 13, height = 15)
  tk.Label(caution_frame, bg = "#DEEECA", image=No_PHONE_FRAME).grid(row = 10, column = 1,padx=10, pady=10)
  tk.Label(clock_frame)
  tk.Label(frameE,fg="black", bg = "#DEEECA", text="مسجد سلام\nMasjid Salaam",font=('Arial',15)).grid(row = 10, column = 1, columnspan=2,padx=10, pady=10)
  tk.Label(frameE, bg = "#DEEECA", image=No_PHONE_FRAME).grid(row = 10, column = 3,padx=10, pady=10)


pack_window()


