import fire


class BrokenCalculator(object):

    def __init__(self, offset=1):
        self._offset = offset

    def add(self, x, y) -> int:
        """

        Args:
            x (): 
            y (): 

        Returns:

        """
        return x + y + self._offset

    def multiply(self, x: int, y: int) -> int:
        """

        Args:
            x (): 
            y (): 

        Returns:
            int: 

        """
        return x * y + self._offset


if __name__ == '__main__':
    fire.Fire(BrokenCalculator)
