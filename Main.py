import re

class RegexExplainer:
    def __init__(self, pattern):
        self.pattern = pattern
        self.components = []
        self.explanations = []

    def parse_pattern(self):
        # Updated patterns for identifying components, including correct handling of \b as an anchor
        component_patterns = [
            (r'\\b', 'word_boundary'),             # Word boundary
            (r'\\[dws]', 'predefined_characters'), # \d, \w, \s, etc.
            (r'\[.*?\]', 'character_class'),       # Character classes
            (r'\\.', 'escaped_character'),         # Escaped characters
            (r'\(\?[:=!]', 'non_capturing_group'), # Non-capturing groups
            (r'\(.*?\)', 'capturing_group'),       # Capturing groups
            (r'\{.*?\}', 'quantifier'),            # Quantifiers like {n,m}
            (r'[+*?^$]', 'quantifier_or_anchor'),  # Quantifiers * + ? and anchors ^ $
            (r'[^\\*+?()\[\]{}|^$]', 'literal')    # Literal characters
        ]

        index = 0
        while index < len(self.pattern):
            match = None
            for pattern, type in component_patterns:
                regex = re.compile(pattern)
                match = regex.match(self.pattern, index)
                if match:
                    self.components.append((match.group(), type))
                    index += len(match.group())
                    break
            if not match:
                index += 1  # In case of no match, skip to the next character

    def explain_components(self):
        # Explanation for each component type
        explanations = {
            'word_boundary': 'Matches a position at the start or end of a word',
            'literal': 'Matches the literal “{}” character',
            'character_class': 'Matches characters in the set {}',
            'predefined_characters': {
                '\\d': 'Matches any Unicode digit.',
                '\\w': 'Matches any Unicode letter, ideogram, digit, or underscore.',
                '\\s': 'Matches any Unicode whitespace character.',
                '\\D': 'Matches any character that is not a Unicode digit.',
                '\\W': 'Matches any character that is not a Unicode word character.',
                '\\S': 'Matches any character that is not a Unicode whitespace character.'
            },
            'escaped_character': 'Matches the literal character {}',
            'non_capturing_group': 'Groups without capturing {}',
            'capturing_group': 'Captures the group {}',
            'quantifier': 'Specifies repetition {}',
            'quantifier_or_anchor': 'Represents quantifier or anchor point {}'
        }
        
        # Generate explanations based on identified components
        for component, component_type in self.components:
            explanation = explanations[component_type].format(component)
            self.explanations.append((component, explanation))

    def display_explanations(self):
        # Print each component and its explanation
        for component, explanation in self.explanations:
            print(f"{component} - {explanation}")

def run_regex_explainer():
    # Obtain regex input from the user
    regex_input = input("Please enter a regex pattern: ")
    explainer = RegexExplainer(regex_input)
    explainer.parse_pattern()
    explainer.explain_components()
    explainer.display_explanations()

if __name__ == "__main__":
    run_regex_explainer()