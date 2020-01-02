max_sequence_length = int(input().strip())

length2number = [1, 2, 4, 7]  # pre-calculated values for length <= 3

end2quantity = {  # initial state is for length = 3
    "000": 1, 
    "001": 1, 
    "010": 1,
    "011": 1,
    "100": 1, 
    "101": 1, 
    "110": 1,
    # 3 ones in a row are forbidden
}

for i in range(4, max_sequence_length + 1):
    next_end2quantity = {
        "000": end2quantity["000"] + end2quantity["100"], 
        "001": end2quantity["000"] + end2quantity["100"], 
        "010": end2quantity["001"] + end2quantity["101"],
        "011": end2quantity["001"] + end2quantity["101"],
        "100": end2quantity["010"] + end2quantity["110"], 
        "101": end2quantity["010"] + end2quantity["110"], 
        "110": end2quantity["011"],
    }
    end2quantity = next_end2quantity
    length2number.append(sum(end2quantity.values()))

print(length2number[max_sequence_length])
