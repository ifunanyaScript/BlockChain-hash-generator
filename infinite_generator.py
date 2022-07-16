# Import the cryptographic function for generating the hash.
from hashlib import sha256
# Import time to calculate how long the mining process takes.
import time

# The hash_generator function will be used in the mining loop.
def hash_generator(text):
    return sha256(text.encode("ascii")).hexdigest()

def mining_loop(block_number, transactions, previous_hash, pre_zeros_required):
    """ This function will run until we get the right nonce that generates
        a valid hash. 
        As we loop, there is a +1 increment to the nonce whenever the generated
        hash is invalid, and this loop continues infinitely until we get a 
        valid hash.
    """
    nonce = 1
    while True:
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = hash_generator(text)
        if new_hash.startswith("0"*pre_zeros_required):
            print(f"Success! You have mined 6.25 bitcoins with nonce: {nonce}")
            return new_hash 
        else:
            nonce += 1

# Program run
if __name__ == "__main__":
    # The transaction/data contains some other info, I just kept it concise because I'm running this on my PC. 
    transactions = """
    Choco->Razzee->78,
    Ifunanya->Script->456
    Git->Hub->845,
    Thor->Loki->650
    Ham->Burger->900,
    Me->Myself->1100
    """
    block_number = 745134
    pre_zeros_required = 19

    # Remember to calculate time, as you mine.
    start_time = time.time()
    print(f"Mining started!")
    new_block_hash =  mining_loop(block_number, transactions, "00000000000000000000020b9c435410024003a396ae353de19ca13e3f611bf4", pre_zeros_required)
    total_time = float((time.time() - start_time))
    print(f"Mining took {total_time:.3f} seconds")
    print(new_block_hash)

# ifunanyaScript