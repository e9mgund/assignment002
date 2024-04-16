dictionary = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19,"twenty":20}
print(dictionary.keys())
print(dictionary.values())

for i in dictionary:
    print(f'{i} + two : {dictionary[i]+2}')