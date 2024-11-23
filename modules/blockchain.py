from web3 import Web3
import json
import datetime

class BlockchainLogger:
    def __init__(self, blockchain_url, contract_address, abi_path):
        self.web3 = Web3(Web3.HTTPProvider(blockchain_url))
        self.contract_address = contract_address
        self.contract = self._load_contract(abi_path)

    def _load_contract(self, abi_path):
        with open(abi_path, 'r') as file:
            contract_abi = json.load(file)
        return self.web3.eth.contract(
            address=self.contract_address,
            abi=contract_abi
        )

    def log_security_event(self, event_type, details):
        """
        Log security events to blockchain
        """
        timestamp = datetime.datetime.now().isoformat()
        try:
            tx_hash = self.contract.functions.logSecurityEvent(
                event_type,
                details,
                timestamp
            ).transact()
            return tx_hash
        except Exception as e:
            print(f"Error logging to blockchain: {e}")
            return None 