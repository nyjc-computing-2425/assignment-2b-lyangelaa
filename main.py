num = input('Enter a number (decimal only): ')
# type your code here
num = num.strip()
dot = str(num).find(".")
dp = len(num)-dot-1
# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
