f = open("input.txt", "r")
disk = [int(d) for d in list(f.read())]

finalDiskPos = 0
checksum = 0
files = [] # [(fileId, fileSize, startDiskPos)]
diskFragmentation = []

s = 0
for i in range(len(disk)):
    if i % 2 == 0:
        diskFragmentation += [i // 2] * disk[i]
        files.append((i // 2, disk[i], s))
    else:
        diskFragmentation += [-1] * disk[i]
    s += disk[i]

firstEmptySpace = 0
for i in range(len(files) -1, -1, -1):
    size = files[i][1]
    fileId = files[i][0]
    startDiskPos = files[i][2]
    firstEmptySpaceForSize = -1
    onlyFiles = True
    for x in range(firstEmptySpace, startDiskPos - size + 1):
        if diskFragmentation[x] == -1 and onlyFiles:
            onlyFiles = False
            firstEmptySpace = x
        if all(diskFragmentation[x + y] == -1 for y in range(size)):
            firstEmptySpaceForSize = x
            break
    if firstEmptySpaceForSize == -1:
        continue
    for j in range(size):
        diskFragmentation[firstEmptySpaceForSize + j] = fileId
    for j in range(startDiskPos, startDiskPos + size):
        diskFragmentation[j] = -1

checksum = sum(pos * diskFragmentation[pos] for pos in range(len(diskFragmentation)) if diskFragmentation[pos] != -1)

print(checksum)
