import numpy as np
import pandas as pd
import datetime 

def steps(file):
    check = "NA"
    sum = 0
    for i in file:
        if check in i:
            pass
        else:
            fields = i.split(",")
            field = fields[0].translate({ord('"'):None})
            try:
                sum += int(field)
            except Exception:
                sum+=0
    
    return sum

def average_steps(file):
    sum = steps(file)
    count = 0
    for i in file:
        count += 1
    
    return sum/count

def median_steps(file):
    check = "NA"
    step_list = []
    for i in file:
        if check in i:
            pass
        else:
            fields = i.split(",")
            try:
                field = int(fields[0].translate({ord('"'):None}))
                step_list.append(field)
            except:
                pass
    step_list.sort()
    return step_list[(len(step_list)//2)-1]
    
        
        
def missing_values(file):
    check = "NA"
    count = 0
    for i in file:
        if check in i:
            count += 1
        else:
            pass
        
    return count

def fill_missing(file):
    check = "NA"
    steps =[]
    date = []
    interval = []
    
    for i in file:
        fields = i.split(",")
        
        if check in fields[0]:
            fields[0] = 0
        else:
            pass
        try:
            steps.append(fields[0])
            date.append(fields[1].translate({ord('"'):None}))
            interval.append(fields[2].translate({ord('"'):None}))
        except:
            pass
    
    
    steps.pop()
        
    mydict = {
        "steps": steps,
        "date": date,
        "interval": interval,
    }
    
    
    df = pd.DataFrame(mydict)
    df.to_csv("NewData.csv", index=None)
    
    return df
    
def converted_to_csv():
    excel_file = pd.read_excel("Data.xls")
    excel_file.to_csv("Data.csv" , index = None, header = False)

def weekday_weekend(file):
    steps =[]
    date = []
    interval = []
    weekend = []
    weekday = []
    
    for i in file:
        fields = i.split(",")
        try:
            steps.append(fields[0])
            date.append(fields[1].translate({ord('"'):None}))
            interval.append(fields[2].translate({ord('"'):None}))
        except:
            pass
    
    steps.pop()
    
    for x in date:
        fields = x.split("-")
        weeknumber = datetime.date(int(fields[0]), int(fields[1]), int(fields[2])).weekday()
        
        if weeknumber < 5:
            weekday.append(True)
            weekend.append(False)
        else:
            weekend.append(True)
            weekday.append(False)
            
    mydict = {
        "steps": steps,
        "date": date,
        "interval": interval,
        "weekday": weekday,
        "weekend": weekend
    }
    
    df = pd.DataFrame(mydict)
    
    return(df)
        
    
    
    

if __name__ == "__main__":
    converted_to_csv()
    with open("Data.csv" , "r") as data:
        info = data.read().split("\n")
    
    print("Number of Steps\n" , steps(info))
    print("Average Steps\n" , average_steps(info))
    print("Median Steps\n" , median_steps(info))
    print("Missing Values\n", missing_values(info))
    print("New Dataset with filled missing information\n", fill_missing(info))
    print("New Dataset with 2 new columns\n", weekday_weekend(info))
    