from stellar_sdk import Keypair, Network, Server, TransactionBuilder
import requests

# Configure StellarSdk to talk to the horizon instance hosted by Stellar.org
# To use the live network, set the hostname to 'horizon.stellar.org'
def get_server():
  return Server(horizon_url="https://horizon-testnet.stellar.org")

# Transactions require a valid sequence number that is specific to this account.
# We can fetch the current sequence number for the source account from Horizon.
def verified_account(source_public_key):
  return (get_server()).load_account(source_public_key)

def signin_transaction(transaction, keypair_source):
  return transaction.sign(keypair_source)
def submit_transaction(transaction):
  return (get_server()).submit_transaction(transaction)