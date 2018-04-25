def converting(source_num, source_hex, target_hex):
    str_36 = '0123456789abcdefghijklmnopqrstuvwxyz'
    dict_36 = {}
    for i in range(len(str_36)):
        dict_36[str_36[i]] = i
    str_b = str_36[:target_hex]
    result = ''
    source_str = str(source_num).lower()
    decimal_num = 0
    for i in range(len(source_str)):
        decimal_num += dict_36[source_str[-i-1]] * (source_hex ** i)
    quotient_int = decimal_num
    while quotient_int >= target_hex:
        remainder = quotient_int % target_hex
        quotient_int = quotient_int // target_hex
        result = str_b[remainder] + result
        if quotient_int < target_hex:
            result = str_b[quotient_int] + result
    return result
