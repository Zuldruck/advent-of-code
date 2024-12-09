f = open("input.txt", "r")
disk = [int(d) for d in list(f.read())]

def getLastFilesOfSizeFromDisk(disk, size, diskFinalSize):
    endFile = diskFinalSize - 1 if diskFinalSize % 2 == 0 else diskFinalSize - 1
    files = []
    for i in range(endFile, -1, -2):
        files.append((i // 2, disk[i] if disk[i] <= size else size))
        if disk[i] == size:
            return files, i - 1
        elif disk[i] > size:
            disk[i] -= size
            return files, i + 1
        size -= disk[i]
    return -1

diskFinalSize = len(disk)
finalDiskPos = 0
checksum = 0
for i in range(diskFinalSize):
    if i >= diskFinalSize:
        break
    if i % 2 == 1:
        freeDiskSpace = disk[i]
        lastFiles, newDiskFinalSize = getLastFilesOfSizeFromDisk(disk, freeDiskSpace, diskFinalSize)
        diskFinalSize = newDiskFinalSize
        for lastFile in lastFiles:
            s = sum(pos * lastFile[0] for pos in range(finalDiskPos, finalDiskPos + lastFile[1]))
            checksum += s
            finalDiskPos += lastFile[1]
    else:
        fileId = i // 2
        fileSize = disk[i]
        s = sum(pos * fileId for pos in range(finalDiskPos, finalDiskPos + fileSize))
        checksum += s
        finalDiskPos += fileSize

print(checksum)
