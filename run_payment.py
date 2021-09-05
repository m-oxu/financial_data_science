# The source account is the account we will be signing and sending from.
from request_account import create_account, get_keypair_and_public
from easy_transaction import get_server, verified_account, signin_transaction, submit_transaction
from stellar_sdk import Keypair, Network, Server, TransactionBuilder
import requests

# These commands creates randomly a test account, with a public and a secret key.
example_keypair = create_account()
destination = example_keypair.public_key

source_secret_key = example_keypair.secret
keypair_source, public_key_account = get_keypair_and_public(source_secret_key)

source_account = verified_account(public_key_account)

# we are going to submit the transaction to the test network,
# so network_passphrase is `Network.TESTNET_NETWORK_PASSPHRASE`,
# if you want to submit to the public network, please use `Network.PUBLIC_NETWORK_PASSPHRASE`.

# Here, you can choose which asset and the amount of money do you want to transfer.
asset = str(input('Which asset do you wanna use?'))
amount = str(input("What is the amount of the transaction?"))
leave_message = str(input('Do you wanna leave a message for the destinatary? Y/n:'))

message = str(input('Write your message!')) if leave_message == 'Y' else ''

# This is the most importat and critical part of the code. This transaction builder
# create an structure which can enable to the money from one account pass from another
# in some asset.

transaction = (
      TransactionBuilder(
          source_account=source_account,
          network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
          base_fee=100,
      )
      .add_text_memo(message)  # Add a memo
      # Add a payment operation to the transaction
    # Here, the destination is also from a test account created previously.
      .append_payment_op(destination, amount, asset)
      .set_timeout(30)  # Make this transaction valid for the next 30 seconds only
      .build()
  )

# Sign this transaction with the secret key
# NOTE: signing is transaction is network specific. Test network transactions
# won't work in the public network. To switch networks, use the Network object
# as explained above (look for stellar_sdk.network.Network).
#transaction.sign(keypair_source)
signin_transaction(transaction, keypair_source)

# Submit the transaction to the Horizon server.
# The Horizon server will then submit the transaction into the network for us.
#response = (get_server()).submit_transaction(transaction)
response = submit_transaction(transaction)
print(response)