# -*- coding: utf-8 -*-
import Queue
import threading
import time
import os
import array
import math
import json
# Third party libraries
import sha3
import matplotlib.pyplot as plt

# Return hex digest string of given data


def keccak256(inputVal):
    return sha3.keccak_256(inputVal).hexdigest()


def keccak256Hex(hexString):
    if len(hexString) % 2 == 0:
        hexData = hexString.decode('hex')
    else:
        hexData = ('0' + hexString).decode('hex')
    return sha3.keccak_256(hexData).hexdigest()


# Convert hex data to bytes array
def hexToBinArray(hexString):
    if len(hexString) % 2 == 0:
        hexData = hexString.decode('hex')
    else:
        hexData = ('0' + hexString).decode('hex')
    return list(array.array('B', hexData))

# Convert bytes array to hex string


def binaryArrayToHex(inputVal):
    length = len(inputVal)
    result = ''
    for c in range(0, length):
        if(inputVal[c] < 16):
            result += '0' + format(inputVal[c], 'x')
        else:
            result += format(inputVal[c], 'x')
    return result

# XOR two arrays to each other


def arrayXor(a, b):
    ac = len(a)
    bc = len(b)
    maxLen = max(ac, bc)
    result = [0] * maxLen
    ac -= 1
    bc -= 1
    for c in range(1, maxLen + 1):
        i = maxLen - c
        if ac >= 0 and bc >= 0:
            result[i] = a[ac] ^ b[bc]  # a XOR b
        else:
            if ac >= 0:
                result[i] = a[ac]
            if bc >= 0:
                result[i] = b[bc]
        ac -= 1
        bc -= 1
    return result

# XOR two hex strings


def hexXor(a, b):
    return binaryArrayToHex(arrayXor(hexToBinArray(a), hexToBinArray(b)))

# Create fingerprint from given verifiable


def createFingerPrint(verifiableValue):
    tmp = hexToBinArray(verifiableValue)
    tmpLen = len(tmp)
    halfTmpLen = tmpLen / 2
    result = [0] * halfTmpLen
    for c in range(0, halfTmpLen):
        result[c] = tmp[c] ^ tmp[halfTmpLen + c]
    return binaryArrayToHex(result)

# Get 128 bits on the left


def get128BitsLeft(inputVal):
    return inputVal[:32]

# Get 128 bit on the right


def get128BitsRight(inputVal):
    return inputVal[-32:]

# Check file existing


def isExistingFile(filename):
    return os.path.isfile(filename)

# Count efficient bits (1 bit)  in one byte


def counEfficientBits(inputVal):
    efficientBits = 0
    while inputVal > 0:
        inputVal = inputVal & (inputVal - 1)
        efficientBits += 1
    return efficientBits

# Count zero bits (0 bit) in one byte


def counZeroBits(inputVal):
    return 8 - counEfficientBits(inputVal)

# Count same bits


def countSameBits(a, b):
    tmp = hexToBinArray(hexXor(a, b))
    tmpLen = len(tmp)
    same = 0
    for c in range(0, tmpLen):
        same += counZeroBits(tmp[c])
    return same

# Verify Proof of Work


def verifyPoW(f, e, x):
    m = keccak256(bytearray(hexToBinArray(f + x)))
    return countSameBits(get128BitsLeft(m), f) == e


# n!
def factorial(n):
    f = 1
    for c in range(1, n + 1):
        f = f * c
    return f

# n!/(n-k)!k! Optimized combination


def combination(n, k):
    maxVal = max(k, n - k)
    minVal = min(k, n - k)
    f = 1
    for i in range(maxVal + 1, n + 1):
        f *= i
    return f / factorial(minVal)

# Get current timestamp


def getTime():
    return int(time.time())

# Dump json to file


def jsonDump(filename, object):
    try:
        fHandle = open(filename, 'w')
        fHandle.write(json.dumps(object))
        fHandle.close()
        return True
    except:
        return False

# Read json from file


def jsonRead(filename):
    try:
        fHandle = open(filename, 'r')
        jsonData = json.loads(fHandle.read())
        fHandle.close()
        return jsonData
    except:
        return False

# Increase one


def increase(hexString, plusPoint=0):
    temp = hexToBinArray(hexString)
    size = len(temp)
    if(plusPoint == 0):
        plusPoint = size - 1
    if(temp[plusPoint] + 1 == 255) and (plusPoint > 0):
        temp[plusPoint] = 0
        return increase(binaryArrayToHex(temp), plusPoint - 1)
    else:
        temp[plusPoint] = temp[plusPoint] + 1
        return binaryArrayToHex(temp)

# Estimate probability


def estimateProbability():
    e = []
    probability = []
    allPr = float(math.pow(2, 128))
    for i in range(128 + 1):
        prC = float(combination(128, i)) / allPr
        e.append(i)
        probability.append(prC)
    return [e, probability]


# Randomize Proof of Work

def randomizeFPoW(f, e, timeout, myClock):
    found = False
    tries = 0
    while (not found) and (myClock.getTicktock() < timeout):
        tries += 1
        tmpX = os.urandom(32).encode('hex')
        m = keccak256Hex(f + tmpX)
        if countSameBits(get128BitsLeft(m), f) == e:
            found = True
    if found == True:
        return [tmpX, tries]
    else:
        return ['', tries]

# Increase Proof of Work


def increaseFPoW(f, e, i, timeout, myClock):
    found = False
    tries = 0
    while (not found) and (myClock.getTicktock() < timeout):
        tries += 1
        tmpX = continueHexData[i].getValue()
        m = keccak256Hex(f + tmpX)
        if countSameBits(get128BitsLeft(m), f) == e:
            found = True
    if found == True:
        return [tmpX, tries]
    else:
        return ['', tries]

# Stop clock


class clock():
    myClock = 0
    last = 0

    def __init__(self):
        self.myClock = getTime()

    def getTicktock(self):
        cur = (getTime() - self.myClock)
        # if not(cur == self.last):
        # print self.last
        self.last = cur
        return cur

    def reset(self):
        self.myClock = getTime()

# Continue data


class continueData():

    def __init__(self, initVal, length=64):
        initStr = str(initVal)
        self.value = initStr + ('0' * (length))

    def reset(self):
        self.value = '0000000000000000000000000000000000000000000000000000000000000000'

    def getValue(self):
        self.value = increase(self.value)
        return self.value

# Get Eratimeout dependence to theta


def getEraTimeout(theta, blockIndex):
    global ethereumBlockchain
    global blockchainSize
    return ethereumBlockchain[blockIndex + theta]['time'] - ethereumBlockchain[blockIndex]['time']

# Flexible Proof-of-Work worker


def FPoWWorker(dataQueue, f, e, i, eraTimeout, myClock, randomize):
    global sharedData
    while True:
        element = dataQueue.get()
        if(randomize):
            (tmpX, tries) = randomizeFPoW(f, e, eraTimeout, myClock)
        else:
            (tmpX, tries) = increaseFPoW(f, e, i, eraTimeout, myClock)
        if(not tmpX == ''):
            sharedData.append([tmpX, tries])
        dataQueue.task_done()

# Multi-thread simulator


def multiThreadFPoW(f, e, eraTimeout, samples, randomize, threads):
    myQueue = Queue.Queue()
    global continueHexData
    global sharedData
    myClock = clock()

    for c in range(samples):
        myQueue.put({'times': c})

    for d in range(threads + 1):
        continueHexData.append(continueData(d))

    for i in range(threads):
        t = threading.Thread(target=FPoWWorker, args=(
            myQueue, f, e, i, eraTimeout, myClock, randomize))
        t.daemon = True
        t.start()

    myQueue.join()

# Reset global all variables


def resetGlobalVariable():
    global continueHexData
    global sharedData
    continueHexData = []
    sharedData = []

# Setup experiment


def FPoWExperiment(blockNumber=0, e=64, eraTimeout=10, randomize=False, samples=100, threads=4):
    x = ethereumBlockchain[blockNumber]['id']
    v = keccak256Hex(x)
    f = createFingerPrint(v)
    resetGlobalVariable()
    multiThreadFPoW(f, e, eraTimeout, samples, randomize, threads)

# Experiment probability


def experimentProbability(blockNumber=0, duration=26, eraTimeout=10, randomize=False, samples=100, threads=4):
    retVal = [0] * 129
    detailData = [None] * 129
    print 'Start experiment from e=' + `64 - duration` + ' to e=' + `64 + duration`
    for e in range(64 - duration, 64 + duration):
        FPoWExperiment(blockNumber=blockNumber, e=e, eraTimeout=eraTimeout,
                       randomize=randomize, samples=samples, threads=threads)
        exp = sharedData
        lenExp = len(exp)
        sumVal = 0.0
        print '[DONE] Experiment e =', e, 'Era timeout =', eraTimeout, 'Samples =', samples, 'Solution=', lenExp, ' Threads =', threads
        for i in range(lenExp):
            if(not exp[i][1] == 0):
                sumVal += float(exp[i][1])
        if(not sumVal == 0):
            retVal[e] = float(lenExp)/float(sumVal)
        detailData[e] = exp
        resetGlobalVariable()
    return [retVal, detailData]

# Calculate sigma


def calculateSigma(expectedValue, collectedData):
    squareSigma = 0.0
    for realValue in collectedData:
        squareSigma += pow(realValue - expectedValue, 2)
    squareSigma = squareSigma / len(collectedData)
    return math.sqrt(squareSigma)



# Define Ethereum blockchain data
ethereumBlockchain = jsonRead('./BlockchainData/EthereumBlock.dat')
blockchainSize = len(ethereumBlockchain)
continueHexData = []
sharedData = []


def MainProc():
    if(not isExistingFile('./data/bruteforce-estimate-and-experiment.dat')):
        exportData = estimateProbability()
        lenEstimate = len(exportData[0])
        (probabilities, experimentData) = experimentProbability(blockNumber=0,
                                                                duration=20, eraTimeout=1200, randomize=False, samples=1000, threads=24)
        exportData.append(probabilities)
        exportData.append(experimentData)
        jsonDump('./data/bruteforce-estimate-and-experiment.dat', exportData)
    else:
        exportData = jsonRead('./data/bruteforce-estimate-and-experiment.dat')

    # Bruterforce experiment
    plt.title('[Brute-force] Probability of solution\'s images dependence to e')
    label = ['Estimate', 'Experiment']
    lines = []
    for i in [1, 2]:
        lines.append(None)
        lines[i - 1], = plt.plot(exportData[0],
                                 exportData[i], label=label[i - 1])

    plt.legend(bbox_to_anchor=(1, 1), handles=lines)
    plt.savefig("./plot/bruteforce-estimate-and-experiment.svg")
    plt.cla()

    if(not isExistingFile('./data/randomize-estimate-and-experiment.dat')):
        exportData = estimateProbability()
        lenEstimate = len(exportData[0])
        (probabilities, experimentData) = experimentProbability(blockNumber=0,
                                                                duration=20, eraTimeout=1200, randomize=True, samples=1000, threads=24)
        exportData.append(probabilities)
        exportData.append(experimentData)
        jsonDump('./data/randomize-estimate-and-experiment.dat', exportData)
    else:
        exportData = jsonRead('./data/randomize-estimate-and-experiment.dat')

    # Bruterforce experiment
    plt.title('[Randomize] Probability of solution\'s images dependence to e')
    label = ['Estimate', 'Experiment']
    lines = []
    for i in [1, 2]:
        lines.append(None)
        lines[i - 1], = plt.plot(exportData[0],
                                 exportData[i], label=label[i - 1])

    plt.legend(bbox_to_anchor=(1, 1), handles=lines)
    plt.savefig("./plot/randomize-estimate-and-experiment.svg")
    plt.cla()


MainProc()

# FPoWExperiment(blockNumber=0, e=64, eraTimeout=10,
#               randomize=False, samples=1000, threads=12)
# for i in sharedData:
#    print i[0]
# 38->90