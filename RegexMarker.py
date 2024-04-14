import re

class RegexMarker:
    def __init__(self, pattern):
        self.pattern = pattern
        self.color_start = "\033[91m"  # Red color start
        self.color_end = "\033[0m"    # Reset to default color

    def mark_text(self, text):
        try:
            compiled_pattern = re.compile(self.pattern)
        except re.error as e:
            return f"Invalid regex pattern: {e}"

        # Start and end ANSI codes for red text
        start_color = '\033[91m'  # Red
        end_color = '\033[0m'     # Reset to default

        matches = list(compiled_pattern.finditer(text))
        if not matches:
            return text  # Return the original text if no matches found

        # More precise handling of zero-length matches
        parts = []
        last_index = 0
        for match in matches:
            start, end = match.span()
            parts.append(text[last_index:start])
            parts.append(f"{start_color}{text[start:end]}{end_color}")
            last_index = end
        parts.append(text[last_index:])

        return ''.join(parts)
    

    