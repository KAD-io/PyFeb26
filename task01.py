def test02_task01(test_str='1234567890abcde'):
    print(f'first symbol: {test_str[0]}')
    print(f'first symbol: {test_str[-1]}')
    print(f'symbol number 3 from the beginning: {test_str[2]}')
    print(f'symbol number 3 from the end: {test_str[-3]}')
    print(f'len: {len(test_str)}')
    print(f'in the reverse order: {test_str[::-1]}')
    print(f'first 8 symbols: {test_str[0:8]}')
    
    
test02_task01()
