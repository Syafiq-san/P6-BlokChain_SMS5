import hashlib
import json
from datetime import datetime, timezone
from typing import Any


class Block:
    def __init__(
        self,
        index: int,
        data: Any,
        previous_hash: str,
        timestamp: str | None = None,
    ) -> None:
        self.index = index
        self.timestamp = timestamp or datetime.now(timezone.utc).isoformat(
            timespec="seconds"
        )
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        block_contents = {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
        }
        encoded_contents = json.dumps(
            block_contents,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        ).encode("utf-8")
        return hashlib.sha256(encoded_contents).hexdigest()

    def mine(self, difficulty: int) -> None:
        target_prefix = "0" * difficulty
        while not self.hash.startswith(target_prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    def __init__(self, difficulty: int = 4) -> None:
        if difficulty < 0:
            raise ValueError("Difficulty tidak boleh bernilai negatif.")
        self.difficulty = difficulty
        self.chain = [self._create_genesis_block()]

    def _create_genesis_block(self) -> Block:
        genesis_block = Block(
            index=0,
            data={"message": "Genesis Block"},
            previous_hash="0" * 64,
        )
        genesis_block.mine(self.difficulty)
        return genesis_block

    def get_latest_block(self) -> Block:
        return self.chain[-1]

    def add_block(self, data: Any) -> Block:
        new_block = Block(
            index=len(self.chain),
            data=data,
            previous_hash=self.get_latest_block().hash,
        )
        new_block.mine(self.difficulty)
        self.chain.append(new_block)
        return new_block

    def is_chain_valid(self) -> bool:
        target_prefix = "0" * self.difficulty

        if not self.chain:
            return False

        genesis_block = self.chain[0]
        if genesis_block.index != 0 or genesis_block.previous_hash != "0" * 64:
            return False

        for index, block in enumerate(self.chain):
            if block.index != index:
                return False
            if block.hash != block.calculate_hash():
                return False
            if not block.hash.startswith(target_prefix):
                return False
            if index > 0 and block.previous_hash != self.chain[index - 1].hash:
                return False

        return True


def run_demo() -> None:
    blockchain = Blockchain(difficulty=4)
    transactions = [
        {"from": "Andi", "to": "Budi", "amount": 10},
        {"from": "Citra", "to": "Dewi", "amount": 5},
        {"from": "Budi", "to": "Citra", "amount": 2},
    ]

    for transaction in transactions:
        blockchain.add_block(transaction)

    print("=== Blockchain Sederhana ===")
    print(f"Difficulty: {blockchain.difficulty} (nol di depan hash)")
    for block in blockchain.chain:
        print(f"\nBlok #{block.index}")
        print(f"  Timestamp     : {block.timestamp}")
        print(f"  Data          : {json.dumps(block.data, ensure_ascii=False)}")
        print(f"  Previous hash : {block.previous_hash}")
        print(f"  Hash          : {block.hash}")
        print(f"  Nonce         : {block.nonce}")

    print(f"\nJumlah blok transaksi: {len(blockchain.chain) - 1}")
    print(f"Valid sebelum data diubah: {blockchain.is_chain_valid()}")

    blockchain.chain[1].data["amount"] = 999
    print(f"Valid setelah data blok #1 diubah: {blockchain.is_chain_valid()}")


if __name__ == "__main__":
    run_demo()