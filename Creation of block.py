import hashlib
import datetime
class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index        = index
        self.timestamp    = str(datetime.datetime.now())
        self.transactions = transactions       # Certificate data
        self.previous_hash = previous_hash
        self.nonce        = 0
        self.hash         = self.calculate_hash()
    def calculate_hash(self):
        """Creates SHA-256 hash from block contents"""
        block_data = (
            str(self.index) +
            self.timestamp +
            str(self.transactions) +
            self.previous_hash +
            str(self.nonce)
        )
        return hashlib.sha256(block_data.encode()).hexdigest()
    def mine_block(self, difficulty=2):
        """Proof of Work: keeps hashing until hash starts with '00...'"""
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block {self.index} mined! Hash: {self.hash}")
    def display(self):
        print("\n" + "="*60)
        print(f"  Block Index     : {self.index}")
        print(f"  Timestamp       : {self.timestamp}")
        print(f"  Transactions    : {self.transactions}")
        print(f"  Previous Hash   : {self.previous_hash}")
        print(f"  Nonce           : {self.nonce}")
        print(f"  Current Hash    : {self.hash}")
        print("="*60)
class Blockchain:
    def __init__(self):
        self.chain = []
        self.difficulty = 2
        # Create the Genesis Block (first block)
        self.create_genesis_block()
    def create_genesis_block(self):
        genesis = Block(0, "Genesis Block - University Certificate System", "0")
        genesis.mine_block(self.difficulty)
        self.chain.append(genesis)
        print("Genesis Block created successfully!")
    def get_last_block(self):
        return self.chain[-1]
    def add_block(self, transactions):
        previous_hash = self.get_last_block().hash
        new_block = Block(len(self.chain), transactions, previous_hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        print(f"Block {new_block.index} added to the blockchain.")
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current  = self.chain[i]
            previous = self.chain[i - 1]
            # Re-check hash integrity
            if current.hash != current.calculate_hash():
                print(f"Block {i} has been tampered!")
                return False
            if current.previous_hash != previous.hash:
                print(f"Block {i} is not linked properly!")
                return False
        return True
    def display_chain(self):
        print("\n\n========== BLOCKCHAIN DISPLAY ==========")
        for block in self.chain:
            block.display()
    def verify_chain(self):
        if self.is_chain_valid():
            print("\n✅ Blockchain is VALID - All blocks verified!")
        else:
            print("\n❌ Blockchain is INVALID - Tampering detected!")
if __name__ == "__main__":
    print("=" * 60)
    print("   UNIVERSITY CERTIFICATE VERIFICATION BLOCKCHAIN")
    print("=" * 60)
    university_chain = Blockchain()
    university_chain.add_block({
        "student": "Alice Johnson",
        "degree":  "B.Tech Computer Science",
        "year":    "2024",
        "grade":   "First Class"
    })
    university_chain.add_block({
        "student": "Bob Smith",
        "degree":  "M.Tech Data Science",
        "year":    "2024",
        "grade":   "Distinction"
    })
    university_chain.add_block({
        "student": "Carol Davis",
        "degree":  "BCA",
        "year":    "2024",
        "grade":   "Second Class"
    })
    university_chain.display_chain()
    university_chain.verify_chain()

# -------------------- RUN COMMAND --------------------
# cd path\to\your\folder
# python blockchain.py


# -------------------- EXPECTED OUTPUT --------------------
# UNIVERSITY CERTIFICATE VERIFICATION BLOCKCHAIN
# Genesis Block created successfully!
# Block 0 mined! Hash: 00a3f...
# Block 1 added to the blockchain.
# Block 1 mined! Hash: 00b7c...
# ...

# ========== BLOCKCHAIN DISPLAY ==========
# ============================================================
#   Block Index     : 0
#   Timestamp       : 2024-xx-xx xx:xx:xx
#   Transactions    : Genesis Block - University Certificate System
#   Previous Hash   : 0
#   Current Hash    : 00a3f...
# ============================================================
# ...

# ✅ Blockchain is VALID - All blocks verified!
