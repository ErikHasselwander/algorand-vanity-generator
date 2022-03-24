from algosdk import account, mnemonic

def main(words, progress = True):
    t = 0
    while True:
        t += 1
        if t % 250000 == 0 and progress:
            print(t)
        private_key, address = account.generate_account()
        # if True:
        for word in words:
            if address[:len(word)] == word:
                print("My address: {}".format(address))
                print("My private key: {}".format(private_key))
                print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))
                return private_key, address


loops = 2
words = ["you", "can", "put", "MULTIPLE", "WORDS", "HERE"]
if __name__ == "__main__":
    words = [word.upper() for word in words]
    for _ in range(loops):
        main(words)