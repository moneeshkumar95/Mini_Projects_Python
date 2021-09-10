def numToWords(n):
    under_20 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    above_100 = {100: 'hundred', 1000: 'thousand', 1000000: 'million', 1000000000: 'billion'}

    if n < 20:
        return under_20[n]

    if n < 100:
        return tens[(n // 10) - 2] + ('' if n % 10 == 0 else '-' + under_20[n % 10])

    value_range = max([key for key in above_100.keys() if key <= n])

    return numToWords((n // value_range)) + ' ' + above_100[value_range] + ('' if n % value_range == 0 else ' ' + numToWords(n % value_range))

num = int(input("enter the number: "))
print(numToWords(num),'dollars')