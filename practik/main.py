from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, contract_address

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3 .middleware_onion.inject(geth_poa_middleware, layer=0)

contract= w3.eth.contract(address=contract_address,abi=abi)

print("Адрес контакта:", contract.address)

# Получение и вывод баланса для каждого аккаунта
accounts = w3.eth.accounts
for account in accounts:
    balance = w3.eth.get_balance(account)
    print(f"Аккаунт: {account}, Баланс: {balance}")

