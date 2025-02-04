#12345*TKHSYIOiutk#67890*TKHSYIOiutk

import re

LONGEST_KEY = 1

def lookup(key):
    assert len(key) <= LONGEST_KEY
    stroke = key[0]

    if stroke == "*-" or stroke == "-*" or stroke == "*-*" or stroke == "#":
        raise KeyError

    regex = re.compile(r"(1?2?3?4?5?)(\*?)(T?K?H?S?)(Y?I?O?)(i?u?t?k?)(\-?#?)(6?7?8?9?0?)(\*?)(T?K?H?S?)(Y?I?O?)(i?u?t?k?)")
    regex_groups = re.search(regex, stroke)

    OnetoFive = regex_groups.group(1)
    LeftAsterisk = regex_groups.group(2)
    LeftConsonant = regex_groups.group(3)
    LeftVowel = regex_groups.group(4)
    LeftParticle = regex_groups.group(5)
    MiddleHyphen = regex_groups.group(6)
    SixtoZero = regex_groups.group(7)
    RightAsterisk = regex_groups.group(8)
    RightConsonant = regex_groups.group(9)
    RightVowel = regex_groups.group(10)
    RightParticle = regex_groups.group(11)

    print("LeftAsterisk\tLeftConsonant\tLeftVowel\tLeftParticle")
    print(LeftAsterisk + "\t\t" + LeftConsonant + "\t\t" + LeftVowel + "\t\t" + LeftParticle)

    print("RightAsterisk\tRightConsonant\tRightVowel\tRightParticle")
    print(RightAsterisk + "\t\t" + RightConsonant + "\t\t" + RightVowel + "\t\t" + RightParticle)

    #頻出順→『n,t,k,s,r,m,h,d,g,w,z,b,j,p』

    Consonants =    ["","t","k","h","s","m","r","n","d","b","g","z","p","w","v","x"]
    listconsonant = ["","T","K","H","S","TH","KS","TS","TK","HS","TKHS","KH","TKH","KHS","THS","TKS"]

    Vowels =    ["a","i","o","u","ya","e","yo","yu"]
    listvowel = ["","I","O","IO","Y","YI","YO","YIO"]

    def Make(Conso,Vowel):

        output = ""
        
        if not Conso and not Vowel:
            output = ""
        else:
            output = Consonants[listconsonant.index(Conso)] + Vowels[listvowel.index(Vowel)]

            if output == "wu":
                output = "a"
            elif output == "wya":
                output = "uxi"
            elif output == "wyu":
                output = "uxe"
            elif output == "wyo":
                output = "uxo"
            elif output == "dya":
                output = "dhi"
            elif output == "dyu":
                output = "dhu"

        print(output)
        return output

    resultL = Make(LeftConsonant,LeftVowel)
    resultR = ""
    result = ""

    if resultL:#ひだりに入力がある時だけ右の音を出す
           resultR = Make(RightConsonant,RightVowel)
            
    listParticle =  ["","i","u","t","k","it","uk","iu","tk","iutk"]
    Particles =     ["","i","u","tu","ku","ti","ki","xn","xtu","-"]

    if LeftParticle not in listParticle:
        LeftParticle = "iutk"
    if RightParticle not in listParticle:
        RightParticle = "iutk"

    #LeftParticleになにかあって左の指の入力もあるとき
    if LeftParticle and resultL:
        resultL += Particles[listParticle.index(LeftParticle)]
    #RightParticleになにかあって右の指の入力もあるとき
    if RightParticle and resultR:
        resultR += Particles[listParticle.index(RightParticle)]

    if  not resultL and not resultR and (LeftParticle or RightParticle):
        raise KeyError
    elif not resultL and resultR:
        #左略語
        raise KeyError
    elif LeftParticle and not resultL or RightParticle and not resultR:
        #略語
        raise KeyError
    else:
        result = resultL + resultR
        
    if (OnetoFive or SixtoZero) and not resultL and not LeftParticle and not RightParticle:
            result = OnetoFive + SixtoZero

    print(result)
    return "{^" + result + "^}"
