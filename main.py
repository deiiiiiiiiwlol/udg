import csv

a = 0#switch zum zaehlen der "ueberschrifften"
b = 0#variable zum abstand zaehlen
c = 0#checkt ob space_final bereits inhalt hat
f = 0#check zum ueberpruefen ob die Datensaetze in einer reihe sind oder nicht
space = []#abstand 1
space2 = []#abstand 2
space_current = [0]#zum rechnen des abstandes
space_current2 = [0]#zum rechnen des abstandes
space_final = []#der finale abstand
counter = 0
kasten = 0
text2 = ""

with open('artikel.csv', 'r', encoding='utf-8-sig') as file:#oeffnet die datei
  csv_reader = csv.reader(file)
  for line in csv_reader:
     text = ''.join(line)#erste zeile wird in einen string uebertragen
     text = text.replace(';', '|')
     f+= 1
     counter = 0
     for char in text: #zaehlt den best moelichen abstand, damit es in einer Tabelle zentriert ist
         text3 = text[0]
         text = text.replace(text[0], '', 1)
         counter+= 1
         if text3 == "|" and a == 0:
             kasten += 1
         if text3 == "|" and f == 1:
           space += [counter]
           space_current += [0]
           space_current2 += [0]
           counter = 0
         elif text3 == "|":
           space2+= [counter] 
           counter = 0
     a = 1
     f = 0
     lange = len(space)
     lange2 = len(space2)
     if lange == kasten and lange2 == kasten:
      for i in range(kasten-1):
        space_current[b] =space[b] - space2[b]
        if space_current[b] >= 0 :
          space_current[b]= space[b]
          if c == 1:
            space_current2[b] = space_final[b] - space_current[b]
            if space_current2[b] < 0:
               space_final[b] = space_current[b]
          else: 
            space_final += [space_current[b]]
        else:
           space_current[b] = space2[b]
           if c == 1:
            space_current2[b] = space_final[b] - space_current[b]
            if space_current2[b] < 0:
              space_final[b] = space_current[b]
           else:  
             space_final += [space_current[b]]
        b += 1
        if b == kasten-1:
         c = 1 #space 1 und 2 muss gelerrt werden,else für was wenn schon final da ist???
         space.clear()
         space2.clear()
         space_current.clear()
         space_current2.clear()
         b = 0
     else:
       if lange == kasten:
         f = 2
        
       else:
         f = 0
f = 0
counter = 1
for k in range(kasten-1):
  space_final[k] //= 2
print(space_final)
# with open('artikel.csv', 'r', encoding='utf-8-sig') as file:
#   csv_reader = csv.reader(file)
#   for line in csv_reader:
#      text = ''.join(line)
#      text = text.replace(';', '|')
     
#      for i in range(kasten):
#        for k in range(space_final[counter-1]):
#          text2 +=" "
#        if f == 1:
#            counter+= 1
#            text2+= "|"
#            for k in range(space_final[counter-1]):
#             text2+= " "
#             f = 0     
#        for char in text:
#         if f == 0:
#          text3 = text[0] 
#          text = text.replace(text[0], '', 1)
#          if text3 != "|":
#           text2+= text3
#          if text3 == "|" and f == 0:
#            f = 1 
#            break