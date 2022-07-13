from hashlib import sha256

def hash_generator(text):
    return sha256(text.encode("ascii")).hexdigest()

def mining_loop(block_number, transactions, previous_hash, pre_zeros_required):
    nonce = 1
    text = str(block_number) + transactions + previous_hash + str(nonce)
    new_hash = hash_generator(text)
    return new_hash


if __name__ == "__main__":
    pre_zeros_required = 7
    transactions = """
    Choco->Razzee->78,
    Ifunanya->Script->456
    """
    new_block_hash =  mining_loop(7, transactions, "0000000trj7892nm1l3sv458m00lkrfecf66nmb0kl9a367klmno341v67uk0m07", pre_zeros_required)
    print(new_block_hash)
