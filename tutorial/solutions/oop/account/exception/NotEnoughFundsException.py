class NotEnoughFundsException(Exception):
    """
    General exception that should be thrown whenever withdrawing funds cannot be done due to not enough funds in the Acc
    """
    def __init__(self, current_funds):
        super().__init__('Not enough minerals. Current state is {}'.format(current_funds))