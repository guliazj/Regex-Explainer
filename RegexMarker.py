import re

class RegexMarker:
    def __init__(self, pattern):
        self.pattern = pattern

    def mark_text(self, text):
        try:
            compiled_pattern = re.compile(self.pattern)
        except re.error as e:
            return f"Invalid regex pattern: {e}"

        matches = list(compiled_pattern.finditer(text))
        if not matches:
            return text  # Return the original text if no matches found

        # More precise handling of zero-length matches
        parts = []
        last_index = 0
        for match in matches:
            start, end = match.span()
            parts.append(text[last_index:start])
            if start == end:  # Handling zero-length matches
                parts.append('|')  # Visual marker for zero-length match
            else:
                parts.append(f"[{text[start:end]}]")
            last_index = end
        parts.append(text[last_index:])

        return ''.join(parts)