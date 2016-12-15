def PatternToNumber(Pattern):
    if Pattern is None or len(Pattern) == 0: 
        print ("There's no symbol or nucleotides in this pattern")
        return 0
    Symbol = Pattern[-1:]
    print symbol + " this is the last 'object'"
    Prefix = 