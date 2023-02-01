def reverse(value):
    
    if len(value) == 1:
        return value
    new_value = reverse(value[1:]) + value[0]
    return new_value


if __name__ == '__main__':
    result = reverse('anbu')
    print(result)