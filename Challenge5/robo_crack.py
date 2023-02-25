from randcrack import RandCrack

# initialise randcrack
rc = RandCrack()

# open the secret file and get its length + contents
with open("secret.enc", "rb") as secfile:
    for line in secfile:
        l = len(line)
        s = list(line)

# open the numbers file
with open('robo_numbers_list.txt', 'r') as nfile:
    # for each phone number in the file:
    # remove '-', make it an integer, and reverse the addition done in the encode function
    for line in nfile:
        rc.submit(int(line.strip().replace("-", "")) - (1 << 31))

# predict the key
key = [rc.predict_getrandbits(8) for i in range(l)]

# reverse the bitwise xor done in the encode function
secret = [a ^ b for a, b in zip(key, s)]

# convert the ascii values to characters
flag = ''.join(list(map(chr, secret)))
print(flag)

