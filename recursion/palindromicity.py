def check_palindrome(input_str):
    str_len = len(input_str)
    
    # Base Case -1
    if str_len == 1:
        return True

    # Base Case - 2
    # To handle palindromes of even length
    if str_len == 2:
        if input_str[0] == input_str[1]:
            return True

    # Recursive Case
    if input_str[0] == input_str[-1]:   
        result = True and check_palindrome(input_str[1:-1])
        return result
    else:
        return False


if __name__ == '__main__':
    result = check_palindrome('maddax')
    print(result)