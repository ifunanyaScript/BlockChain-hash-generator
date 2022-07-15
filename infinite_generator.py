# Import the cryptographic function for generating the hash.
from hashlib import sha256

import time

def hash_generator(text):
    return sha256(text.encode("ascii")).hexdigest()

def mining_loop(block_number, transactions, previous_hash, pre_zeros_required):
    nonce = 1
    while True:
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = hash_generator(text)
        if new_hash.startswith("0"*pre_zeros_required):
            print(f"Success! You have mined 6.25 bitcoins with nonce: {nonce}")
            return new_hash 
        else:
            nonce += 1


if __name__ == "__main__":
    pre_zeros_required = 5
    transactions = """
    Choco->Razzee->78,
    Ifunanya->Script->456
    """
    start_time = time.time()
    print(f"Mining started!")
    new_block_hash =  mining_loop(7, transactions, "000000067hjg990m1l3sv458m00lkrilkf66nmb0kl9a367klmno341v67uk0m07", pre_zeros_required)
    total_time = str((time.time() - start_time))
    print(f"Mining took {total_time:.3f} seconds")
    print(new_block_hash)

# ifunanyaScript