#igs14_2196.atx contains all valid antennas, with a weird format.
#antennas will contain all valid antennas in a string list format
with open("in/antennas/igs14_2196.atx","r") as f:
  lines             = f.readlines()
  newLines          = []
  antennaInNextLine = False
  for line in lines:
    #if the line contains an antenna, append it to the list, well formatted
    if antennaInNextLine:
      newLines.append(f"\"{line[0:20].strip()}\",")
      antennaInNextLine = False
    #if the line contains START OF ANTENNA, then the next line contains an antenna
    if "START OF ANTENNA" in line:
      antennaInNextLine = True
  #the last antenna will have a comma, so we must remove it
  lastAntenna = newLines[-1][0:len(newLines[-1])-1]
  newLines.pop()
  newLines.append(lastAntenna)
  with open("out/antennas/antennas","w") as f2:
    f2.writelines(newLines)