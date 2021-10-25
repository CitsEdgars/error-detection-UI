import numpy as np

def get_bits(message, n = 10):
    msg_len = len(message)
    msg_bits = []
    chk_bits = []
    pow_2 = [2**j for j in range(0,n+1)]
    idx = 1
    while(msg_len != 0):
        if(idx == pow_2[0]):
            chk_bits.append(idx)
            pow_2.remove(pow_2[0])
        else:
            msg_bits.append(idx)
            msg_len -= 1
        idx += 1
    return chk_bits, msg_bits

def get_message_bit_mtrx(message):
    message_matrix = []
    for sym in message:    
        sym_ASCII = ord(sym)
        sym_binary = bin(sym_ASCII)[2:]
        message_matrix.append(list(sym_binary))
    return message_matrix

def get_hamming_distance(msg_1, msg_2):
    hamming_distance = 0
    for idx, bit in enumerate(msg_1):
        if (int(bit) != int(msg_2[idx])):
            hamming_distance += 1
    return hamming_distance

def get_hamming_code(message, parity = 0):
    msg_matrix = get_message_bit_mtrx(message)
    hamming_matrix = []
    
    for symbol in msg_matrix:
        chk_bits, msg_bits = get_bits(symbol)

        tot_len = len(chk_bits) + len(msg_bits)
        hamming_code = list(np.zeros(tot_len))

        for counter, idx in enumerate(msg_bits):
            hamming_code[idx-1] = int(symbol[counter])
        
        for counter, idx in enumerate(chk_bits):
            bit_loc = idx - 1
            period = idx*2
            take_start = bit_loc
            take_end = int(take_start + period / 2)
            period_end = take_start + period
            values = hamming_code[take_start+1:take_end]
            
            take_start = period_end
            while(take_start < tot_len):
                take_end = int(take_start + period / 2)
                period_end = take_start + period
                values += hamming_code[take_start:take_end]
                take_start = period_end

            sum = 0
            for value in values:
                sum += value       
            
            hamming_code[idx-1] = sum % 2 + parity
        
        hamming_matrix.append(hamming_code)

    return hamming_matrix

def check_for_errors(message, message_len = 11, parity = 0):
    message_list = []
    parts = int(len(message)/message_len)

    errors = 0
    for part in range(parts):
        curr_msg_part = message[message_len*part:message_len*(part+1)]
        chk_bits, msg_bits = get_bits(curr_msg_part)
        msg_bits = msg_bits[:message_len - len(chk_bits)]   #Quick workaround

        hamming_code = list(np.zeros(message_len))

        for counter, idx in enumerate(msg_bits):
            hamming_code[idx-1] = int(curr_msg_part[msg_bits[counter]-1])
        
        erroneous_bit = 0

        for counter, idx in enumerate(chk_bits):
            bit_loc = idx - 1
            period = idx*2

            take_start = bit_loc
            take_end = int(take_start + period / 2)
            period_end = take_start + period
            values = hamming_code[take_start+1:take_end]
            
            take_start = period_end
            while(take_start < message_len):
                take_end = int(take_start + period / 2)
                period_end = take_start + period
                values += hamming_code[take_start:take_end]
                take_start = period_end

            sum = 0
            for value in values:
                sum += value       
            
            check_bit_val = (sum + parity) % 2
            hamming_code[idx-1] = (sum + parity) % 2

            if(int(curr_msg_part[bit_loc]) != check_bit_val):
                print("Error found!")
                erroneous_bit += bit_loc + 1      

        errors += get_hamming_distance(curr_msg_part, hamming_code)

        if erroneous_bit != 0:
            curr_msg_part[erroneous_bit-1] = (int(curr_msg_part[erroneous_bit-1]) + 1) % 2

        data_bits = []
        for id in msg_bits:
            data_bits.append(curr_msg_part[id-1])
        message_list.append(data_bits)
        
    return message_list, errors