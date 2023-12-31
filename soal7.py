def shiftAlph(raw):
    alph = "abcdefghijklmnopqrstuvwxyzabcde"
    raw = raw.lower()
    newString = ""
    for i in raw:
        if i in alph:
            indexNew = alph.index(i)
            new = alph[indexNew+5]
            newString += new
        else:
            newString += i
    print(newString)

shiftAlph("xfqfr bfmdz")
shiftAlph("gjxtp lzj rfz ifkyfw jxi snm")
shiftAlph("gwt, gjxtp qz rfz rfpfs in bfwlty lfp?")
shiftAlph("fpz xfdfsl pfrz, rfz lfp ofin ufhfwpz")
shiftAlph("dfsl pnwnr xynhpjw otrtp pz pnhp ifwn lwzu")
