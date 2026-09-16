Numbers = [10,7,20,13,6]

def largest(nums):
    return max(nums)

def Total(nums):
    return sum(nums)


def is_palindrome(word):
    cleaned = word.lower()
    return cleaned == cleaned[::-1]

print(largest(Numbers))           
print(Total(Numbers))              
print(is_palindrome("Dad"))        
print(is_palindrome("Kayak"))      

