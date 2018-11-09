def count_vowels(newyork):
    vowels=('a','e','i','o','u')
    count=0
    found=''
    for letter in newyork:
        if letter in vowels:
            count=count+1
            if letter not in found:
                found=found+letter
    return (found, count)
           
print(count_vowels("drink water"))
