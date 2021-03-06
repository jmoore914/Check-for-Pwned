import hashlib
from urllib.request import Request, urlopen
import csv


def checkPW(pw):
    m = hashlib.sha1()

    m.update(bytes(pw, 'utf-8'))
    shaPass = m.hexdigest()
    shortPass = shaPass[0:5]
    req = Request('https://api.pwnedpasswords.com/range/' +
                  shortPass, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req).read().decode()
    if (shaPass[5:].upper() in response):
        return True
    else:
        return False


def checkCSV(pathToCSV, accountCol, pwCol, headerRow):
    compromisedSites = ''
    with open(pathToCSV) as csvfile:
        csvReader = csv.reader(csvfile, delimiter=",")
        firstLine = next(csvReader, None)
        if accountCol + 1 > len(firstLine):
            raise ValueError(
                'Account column greater than number of columns in CSV.')
        if pwCol + 1 > len(firstLine):
            raise ValueError(
                'Password column greater than number of columns in CSV.')
        if not headerRow:
            if checkPW(firstLine[pwCol]):
                compromisedSites += ', ' + firstLine[accountCol]
        for row in csvReader:
            if checkPW(row[pwCol]):
                compromisedSites += ', ' + row[accountCol]
    if len(compromisedSites) > 0:
        return "Compromised accounts: \n" + compromisedSites[2:]
    else:
        return "All passwords fine!"
