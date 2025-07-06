import sys
import traceback


class CustomException(Exception):
    def __init__(self, error_message, error_detail=sys):
        super().__init__(error_message)
        # Call the method to get detailed message including filename and line number
        self.error_message = self.get_detailed_error_message(error_message, error_detail)

    @staticmethod
    def get_detailed_error_message(error_message, error_detail=sys):
        # Use exc_info() to get the current exception info: (type, value, traceback)
        _,_, exc_tb = traceback.sys.exc_info()
        if exc_tb is not None:
            # Get the last traceback frame (most recent call)
            last_traceback = traceback.extract_tb(exc_tb)[-1]
            file_name = last_traceback.filename
            line_number = last_traceback.lineno
        else:
            # If no traceback is found, provide fallback info
            file_name = "Unknown file"
            line_number = "Unknown line"

        return f"Error Occurred in {file_name}, line {line_number}: {error_message}"

    def __str__(self):
        return self.error_message
