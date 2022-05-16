#GPS_Receiver_Types contains all valid receiver types, with a weird format
#receivers will contain all valid receiver types in a string list format
with open("GPS_Receiver_Types","r") as f:
  lines    = f.readlines()
  newLines = []
  for line in lines:
    #if the line contains a receiver and not 
    #a comment, append it to the list, well formatted
    if line[0] != "#":
      newLines.append(f"\"{line[0:21].strip()}\",")
  #the last receiver will have a comma, so we must remove it
  lastReceiver=newLines[-1][0:len(newLines[-1])-1]
  newLines.pop()
  newLines.append(lastReceiver)
  with open("receivers","w") as f2:
    f2.writelines(newLines)