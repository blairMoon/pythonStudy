num1 = int(input())
num2 = int(input())

def divmod_num(num1,num2):
    moc = num1 // num2
    namozi = num1 % num2
    return moc, namozi

print(divmod_num(num1,num2))    