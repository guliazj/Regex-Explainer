explanations = {
    '^': "Matches the start of the string",
    '$': "Matches the end of the string",
    '.': "Matches any single character except newline \\n",
    '\d': "Matches any digit character (0-9)",
    '\D': "Matches any non-digit character",
    '\w': "Matches any word character (alphanumeric characters plus underscore)",
    '\W': "Matches any non-word character",
    '\s': "Matches any whitespace character (space, tab, newline)",
    '\S': "Matches any non-whitespace character",
    '[ ]': "Matches any single character within the brackets",
    '[^ ]': "Matches any single character not within the brackets",
    '*': "Matches zero or more occurrences of the preceding element",
    '+': "Matches one or more occurrences of the preceding element",
    '?': "Matches zero or one occurrence of the preceding element",
    '{n}': "Matches exactly {0} occurrences of the preceding element",
    '{n,}': "Matches at least {0} occurrences of the preceding element",
    '{n,m}': "Matches between {0} and {1} occurrences of the preceding element",  # Updated explanation with placeholders
    '()': "Groups multiple tokens together",
    '|': "Acts like an OR operator",
    '\\': "Escapes special characters, allowing you to match them literally",
    '@': "Matches the literal '@' character",
    '{': "Denotes the start of a repetition quantifier",
    '}': "Denotes the end of a repetition quantifier."
}

pattern = input("Enter your regex pattern: ")

i = 0
while i < len(pattern):
    if pattern[i:i+2] in explanations:
        print(f"{pattern[i:i+2]} - {explanations[pattern[i:i+2]]}")
        i += 2
    elif pattern[i] in explanations:
        if pattern[i] == '{':
            j = i + 1
            while pattern[j] != '}':
                j += 1
            range_pattern = pattern[i:j+1]
            if ',' in range_pattern:
                min_occurrences, max_occurrences = map(lambda x: int(x) if x else None, range_pattern[1:-1].split(','))
                if max_occurrences is None:
                    explanation = explanations['{n,}'].format(min_occurrences)
                else:
                    explanation = explanations['{n,m}'].format(min_occurrences, max_occurrences)
            else:
                min_occurrences = int(range_pattern[1:-1])
                explanation = explanations['{n}'].format(min_occurrences)
            print(f"{range_pattern} - {explanation}")
            i = j + 1
        else:
            print(f"{pattern[i]} - {explanations[pattern[i]]}")
            i += 1
    else:
        i += 1
