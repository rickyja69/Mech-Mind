string = input()

def is_pallindrome(string):
    n = len(string)
    if n==1:
        return True
    for i in range(n//2):
        if string[i] != string[-i-1]:
            return False
    return True

def ans(string):
    for x in range(1,len(string)-2):
        if is_pallindrome(string[:x]):
            for y in range(x+1,len(string)):
                if is_pallindrome(string[x:y]) and is_pallindrome(string[y:]):
                    print(string[:x])
                    print(string[x:y])
                    print(string[y:])
                    return
    print("not possible")

ans(string)