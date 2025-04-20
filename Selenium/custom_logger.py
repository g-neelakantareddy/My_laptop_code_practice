import logging

class CustomColoredFormatter(logging.Formatter):
    # Define your own colors for each log level
    COLORS = {
        'DEBUG': '\033[94m',    # Blue
        'INFO': '\033[92m',     # Green
        'WARNING': '\033[93m',  # Yellow
        'ERROR': '\033[91m',    # Red
        'CRITICAL': '\033[41m'  # Red background
    }
    RESET = '\033[0m'  # Reset color

    def format(self, record):
        # Get the color for the current log level
        color = self.COLORS.get(record.levelname, self.RESET)
        # Format the message using the default formatter
        message = super().format(record)
        # Return the colored message
        return f"{color}{message}{self.RESET}"

def setup_logger():
    # Basic configuration
    logging.basicConfig(
        level=logging.INFO,  # Set to DEBUG to capture all levels
        format='%(asctime)s - %(levelname)s - %(message)s',
    )

    # Create a custom handler
    handler = logging.StreamHandler()
    handler.setFormatter(CustomColoredFormatter('%(asctime)s - %(levelname)s - %(message)s'))

    # Get the root logger and add the custom handler
    logger = logging.getLogger()
    logger.addHandler(handler)

    return logger
