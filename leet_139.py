
def WordBreak(words : str, wordDict: list[str]):
    rdata = words 
    res = [] 

    for word in wordDict:
        if word in rdata:
            rdata = rdata.replace(word, "", 1)
            res.append(True)
    print(f'Rdata : {rdata}')
    return res 



s = "applepenapple"

wordDict = ["apple","pen"]

print(WordBreak(s, wordDict))

