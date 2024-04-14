import sys
from RegexExplainer import RegexExplainer
from RegexMarker import RegexMarker
def main():
    while True:
        i = int(input("(1)Regex Explainer\t(2)Regex Marker\n"))
        if i == 1:
            run_regex_explainer()
            break
        elif i == 2:
            run_regex_marker()
            break
        else: print("Invalid input\n")

def run_regex_explainer():
    # Obtain regex input from the user
    regex_input = input("Please enter a regex pattern: ")
    explainer = RegexExplainer(regex_input)
    explainer.parse_pattern()
    explainer.explain_components()
    explainer.display_explanations()

def run_regex_marker():
    regexInput = input("Please enter a regex pattern: ")
    textInput = input("Please enter text: ")
    marker = RegexMarker(regexInput)
    highlightedText = marker.mark_text(textInput)
    print("Highlighted Text:")
    print(highlightedText)

if __name__ == "__main__":
    main()