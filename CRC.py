import numpy as np

def get_message_bit_mtrx(message):
    message_matrix = []
    for sym in message:    
        sym_ASCII = ord(sym)
        sym_binary = bin(sym_ASCII).replace('b','') # Jo pirmie 2 simboli ir 0b vai 1b
        message_matrix.append(sym_binary)
    return message_matrix

def get_CRC_code(message, gen_pol = []):
    binary_repr = get_message_bit_mtrx(message)
    msg_len = len(binary_repr)
    rem_len = len(gen_pol) - 1
    msg_powers = []
    coeff_offset = 0
    for symbol in reversed(binary_repr):
        if len(symbol) < 8:
            symbol = '0' + symbol
        for idx, i in enumerate(reversed(symbol)):
            if i == '1':
                msg_powers.append(coeff_offset + idx + rem_len)
        coeff_offset +=8

    poly_repr = np.zeros(msg_len * 8 + rem_len)
    for idx, i in enumerate(poly_repr):
        if (idx in msg_powers):
            poly_repr[idx] = 1

    CRC_code = ''
    for symbol in binary_repr:
        if len(symbol) < 8:
            symbol = '0' + symbol
        CRC_code += symbol
    
    poly_repr = list(reversed(poly_repr))
    remainder = get_remainder(poly_repr, gen_pol)
    CRC_code = CRC_code + ''.join(str(int(e)) for e in remainder)

    return list(CRC_code)


def get_remainder(msg_p, gen_p, parity = 0):
    result = np.polydiv(msg_p, gen_p)
    rem = result[1]
    for idx,coeff in enumerate(rem):
        if coeff < 0: rem[idx] = -coeff
        rem[idx] = (rem[idx] + parity) % 2
    return rem

def check_for_errors(received, gen_poly):
    msg_poly_repr = list(map(int, received))
    msg_p = np.poly1d(msg_poly_repr)
    gen_p = np.poly1d(gen_poly)
    rem = get_remainder(msg_p, gen_p)
    data = []
    char_count = int((len(msg_poly_repr) - len(gen_poly) + 1) / 8)

    if sum(rem.c) == 0: 
        errors = 0
        for i in range(char_count):
            data.append(msg_poly_repr[i*8:(i+1)*8])
    else: 
        errors = 1
        for i in range(char_count):
            data.append(msg_poly_repr[i*8:(i+1)*8])

    return data, errors
