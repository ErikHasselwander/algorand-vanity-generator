from algosdk import account, mnemonic
import time
import sys

def main(words, progress = True):
    tp = printer()
    t = 0
    ctime = time.time()
    while True:
        t += 1
        if t % 100000 == 0 and progress:
            tp.print(f'{t} addresses checked with {round(t / (time.time() - ctime) / 1000,3)} kH/s')
        private_key, address = account.generate_account()
        # if True:
        for word in words:
            if address[:len(word)] == word:
                print()
                print("My address: {}".format(address))
                print("My private key: {}".format(private_key))
                print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))
                print()
                return private_key, address


loops = 2
words = ["you", "can", "put", "MULTIPLE", "WORDS", "HERE"]


class printer:
    def __init__(self, first = True):
        self.last = ""
        self.first = first
    
    def print(self, text, newline = False):
        if (newline or not self.last == text) and not self.first:
            pass
        self.first = False
        self.last = text
        sys.stdout.write("\r%s" %(text))
        sys.stdout.flush()
    
    def reset(self):
        self.first = True

if __name__ == "__main__":
    words = [word.upper() for word in words]
    for _ in range(loops):
        main(words)
