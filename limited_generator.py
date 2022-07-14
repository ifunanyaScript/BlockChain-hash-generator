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
    for nonce in range(NONCES):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = hash_generator(text)
        if new_hash.startswith("0"*pre_zeros_required):
            print(f"Success! You have mined 6.25 bitcoins with nonce: {nonce}") 
            return new_hash
    raise BaseException(f"Hash could not be generated after reaching the limit of {NONCES} times")


if __name__ == "__main__":
    pre_zeros_required = 6
    transactions = """
    Choco->Razzee->78,
    Ifunanya->Script->456
    """
    start_time = time.time()
    print(f"Mining started!")
    new_block_hash =  mining_loop(7, transactions, "000000067hjg990m1l3sv458m00lkrilkf66nmb0kl9a367klmno341v67uk0m07", pre_zeros_required)
    total_time = str((time.time() - start_time))
    print(f"Mining took {total_time} seconds")
    print(new_block_hash)
