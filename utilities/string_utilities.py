class StringUtilities:
    """
    utility class to create static methods for various simple operations on input type
    """

    @staticmethod
    def convert_comma_separated_string_to_list(command_separated_string: str):
        return command_separated_string.split(',')
