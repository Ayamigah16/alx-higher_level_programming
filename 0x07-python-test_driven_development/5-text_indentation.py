#!/usr/bin/python3

def text_indentation(text):
    """
    Prints the text with 2 new lines after each '.', '?' and ':'.

    Parameters:
    text (str): The input text.

    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    result = ""
    new_line = True

    for char in text:
        if new_line and char == ' ':
            continue

        result += char

        if char in punctuations:
            result += '\n' + '\n'
            new_line = True
        else:
            new_line = False

    print(result, end='')

# Uncomment the following lines to run the provided test cases
# text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
# Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
# Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
# Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
# Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
# rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
# stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
# cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
# beatiorem! Iam ruinas videres""")

# text_indentation("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quonam modo?")
