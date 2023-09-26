# range

# def my_range(stop, start=0, step=1):
#     temp = start
#     while temp < stop:
#         yield temp
#         temp += step
#     else:
#         raise StopIteration
#
#
# x = my_range(stop=3, step=-1)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

# is_palindrome

def is_palindrome(text):
    return True if text == text[::-1] else False


print(is_palindrome('kajak'))
print(is_palindrome('kajako'))

x = lambda text: True if text == text[::-1] else False

print(x('kayak'))
print(x('kayako'))
