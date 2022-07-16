# Import the cryptographic function for generating the hash.
from hashlib import sha256
# Import time to calculate how long the mining process takes.
import time

# We define a variable which holds the maximum nonce value.
MAXIMUM_NONCE = 10000000000

# The hash_generator function will be used in the mining loop.
def hash_generator(text):
    return sha256(text.encode("ascii")).hexdigest()

# This function takes the required parameters and loops within the maximum nonce until it gets a valid
# hash, if it reaches the maximum nonce without getting a valid hash, then an error will be raised. 
def mining_loop(block_number, transactions, previous_hash, pre_zeros_required):
    for nonce in range(MAXIMUM_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = hash_generator(text)
        # We check if the new hash is valid before returning it. If it isn't the loop continues.
        if new_hash.startswith("0"*pre_zeros_required):
            print(f"Voilà! You have mined 6.25 bitcoins with nonce: {nonce}") 
            return new_hash
    raise BaseException(f"Hash could not be generated after reaching the limit of {MAXIMUM_NONCE} times")

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
    
    # Remember to calculate time as you mine.
    start_time = time.time()
    print(f"Mining started!")
    new_block_hash =  mining_loop(block_number, transactions, "00000000000000000000020b9c435410024003a396ae353de19ca13e3f611bf4", pre_zeros_required)
    total_time = float((time.time() - start_time))
    print(f"Mining took {total_time:.3f} seconds")
    print(new_block_hash)

# ifunanyaScript