import re

file = input("filename: ")
change_duration = input("time change (0:-1.0): ") #in example (0:5:0)

MADE_BY = 'ilesik'
ADD_TO_FILE_NAME = " (edited_by_ilesik)"



def time_parser(string):
    return int(string.split(':')[0]),int(string.split(':')[1].split('.')[0]),int(string.split('.')[1])

def at_least_two(number):
    number = str(number)
    if len(number)-2 < 0:
        return "0"*(abs(len(number)-2))+number 
    return number

minutes,seconds,milliseconds = time_parser(change_duration)
print(minutes,seconds, milliseconds)


f = open(file)

new_text = ""
for line in f.readlines():
    t_n = re.findall("\[[0-9][0-9]+\:[0-9][0-9]\.[0-9][0-9]\]",line)
    if not len(t_n):
        by = re.findall("\[by\:\ [A-Za-z0-9]+\]*",line)
        if len(by):
            line = line.replace(by[0],f"[by: {MADE_BY}]")
        new_text += line



        continue
    t_n = t_n[0]
    minutes_edited,seconds_edited,milliseconds_edited =time_parser(t_n[1:-1:])


    new_minutes = minutes_edited+minutes
    new_seconds = seconds_edited+seconds
    new_milliseconds = milliseconds_edited+milliseconds

    if new_milliseconds < 0:
        new_milliseconds = 100 + new_milliseconds
        new_seconds -= 1

    if new_seconds < 0:
        new_seconds = 60 + new_seconds
        new_minutes -= 1
    
    if new_minutes<0:
        new_minutes = 0
        new_seconds =0
        new_milliseconds = 0


    to_replace =f"[{at_least_two(new_minutes)}:{at_least_two(new_seconds)}.{at_least_two(new_milliseconds)}]"


    print("was",t_n,' new',to_replace, "  text:", line.replace(t_n,''))
    new_text +=  line.replace(t_n,to_replace)

f.close()
f_name = '.'.join(file.split('.')[:-1:])+ADD_TO_FILE_NAME+"."+file.split('.')[-1]
f = open(f_name,'w')
f.write(new_text)
f.close()

print(f"DONE: file saved as \"{f_name}\"")



