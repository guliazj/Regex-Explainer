import re

class RegexMarker:
    def __init__(self, pattern):
        self.pattern = pattern

    def mark_text(self, text):
        # Attempt to compile the regex pattern to ensure it's valid
        try:
            compiled_pattern = re.compile(self.pattern)
        except re.error as e:
            return f"Invalid regex pattern: {e}"

        # Finding all matches using finditer
        matches = list(compiled_pattern.finditer(text))
        if not matches:
            return text  # Return the original text if no matches found

        # Highlight matches by inserting markers
        highlighted_text = ""
        last_index = 0
        for match in matches:
            start, end = match.span()
            highlighted_text += text[last_index:start] + "[" + text[start:end] + "]"
            last_index = end
        highlighted_text += text[last_index:]

        return highlighted_text