import array

startCameraID = input("What's the camera id of your starting picture? ")
# assign Variables
cameraID = []
xCoordinates = []
yCoordinates = []
output = []

#open input/output files with read and overwrite
inputFile = open("input.txt", "r")
outputFile = open("output.txt", "w")

#remove unnecessary junk from input
with inputFile as f:
    lines = [line.rstrip() for line in f]
tracked_lines = lines[10:-7]

#split input into multiple arrays: CameraID, xCoordinates, yCoordinates
for i in tracked_lines:
    i = i.replace("\t"," ")
    i = i.split()
    xCoordinates.append(i[1])
    yCoordinates.append(i[2])
    cameraID.append(len(xCoordinates) -1)


#Write lines into final output file
for x in cameraID:
    outputFile.write('<location camera_id="'+str(cameraID[x] + int(startCameraID))+'" pinned="true" x="'+(xCoordinates[x])+'" y="'+(yCoordinates[x])+'"/>\n')

outputFile.close()
print("All done, you can now copy over your lines to the markers.xml")
