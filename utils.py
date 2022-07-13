from hashlib import sha256

def hash_generator(text):
    return sha256(sha256(text.encode("ascii")).hexdigest())

def mining_loop():
    pass

if __name__ == "__main__":
    transactions = """
    Choco->Razzee->78,
    Ifunanya->Script->456
    """
    new_block_hash =  mining_loop()
