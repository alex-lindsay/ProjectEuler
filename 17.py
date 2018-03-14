def spellNumber(n):
    result = ""
    digits = [ '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', 'XX', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if (n>=1000):
        result = spellNumber(int(n/1000)) + " thousand"
        n = n - (int(n/1000)*1000)

    if (n>=100):
        result = spellNumber(int(n/100)) + " hundred"
        n = n - (int(n/100)*100)
        if n>0:
            result = result + " and "         

    if (n>=20):
        result = result + tens[int(n/10)]
        n = n - (int(n/10)*10)
        if n>0:
            result = result + '-' + digits[n]
        n = 0

    if (n<10):
        result = result + digits[n]
        n = 0

    if (n>0) and (n<20):
        result = result + teens[n-10]
        n = 0

    return result

def main():
    textNumbers = list(map(lambda x: spellNumber(x), range(1,1001)))
    for (index, textItem) in enumerate(textNumbers):
        print(str(index+1), textItem)
        # print(index)

    print(str(sum(map(lambda x: len(x.replace('-','').replace(' ','')), textNumbers))))

main()