from stellar_sdk import Keypair, Network, Server, TransactionBuilder
import requests


def create_account():
    """To make this script work, create an account on the testnet."""

    keypair = Keypair.random()
    url = "https://friendbot.stellar.org"
    _response = requests.get(url, params={"addr": keypair.public_key})
    # Check _response.json() in case something goes wrong
    return keypair

# Derive Keypair object and public key (that starts with a G) from the secret
def get_keypair_and_public(secret_key):
  source_keypair = Keypair.from_secret(secret_key)
  source_public_key = source_keypair.public_key
  return source_keypair, source_public_key