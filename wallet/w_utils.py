from django.test import TransactionTestCase
"""The transaction test case is used because of  the
 database transaction facility it speed up the process of 
 resetting the database to a known state at the beginning of each test."""
from django.contrib.auth import get_user_model
import logging


User = get_user_model()
logger = logging.getLogger(__name__)


class WalletTestCase(TransactionTestCase):

    def _create_initial_balance(self, value):
        self.wallet.transaction_set.create(
            value=value,
            running_balance=value
        )
        self.wallet.current_balance = value
        self.wallet.save()
        """ Creating the initial value which will be 0 and save it before adding the money"""

    def setUp(self):
        logger.info('Creating wallet...')
        self.user = User()
        self.user.save()
        self.wallet = self.user.wallet_set.create()
        self.wallet.save()
        logger.info('Wallet created.')
        """ The wallet will be created after the user has 
        registered but this function is for initializing"""
