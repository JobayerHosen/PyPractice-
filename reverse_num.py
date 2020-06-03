n = 9646324351
def reverse(x: int) -> int:
    num = x
    if num < -pow(2,31) or num > pow(2,31)-1:
        return 0
    is_negative = num < 0
    if is_negative: num = -num
    reverse = 0
    while num > 0:
        reverse = reverse*10 + num%10
        num = num//10
    if is_negative: reverse = -reverse
    return reverse

r = reverse(n)