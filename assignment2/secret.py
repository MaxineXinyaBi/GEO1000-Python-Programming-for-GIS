# GEO1000 - Assignment 2
# Authors: Xinya Bi, Xu Wang
# Studentnumbers:6195350, 6235379

def reverse_part(part):
    """Take as input a list
    Returns a new list with elements in input reversed
    Note: Pure function, so should not modify input!
    
    Example:
    
        >>> reverse_part(['t', 'h', 'i', 's'])
        ['s', 'i', 'h', 't']
    """
    modified_part = []
    for letter in part[::-1]:
        modified_part.append(letter)
    return modified_part


def part_to_str(part):
    """Take as input a list with letters.
    Returns a new string with letters in the input list

    Example:

        >>> part_to_str(['a', 'b', 'c'])
        "abc"

    """
    new_string = ''.join(part)
    return new_string


def split_in_parts(sentence):
    """Split the string into a list of lists (either containing letters, or just
    one character not part of the alphabet).

    Example:

        >>> split_in_parts("this is.")
        [['t', 'h', 'i', 's'], [' '], ['i', 's'], ['.']]

    """
    final_list = []
    temp_list = []

    for char in sentence:
        # check if the current char is alphabet, if it is, put it in a temp list
        if char.isalpha():
            temp_list.append(char)
        # if not
        else:
            # check if temp list exist
            if temp_list:
                final_list.append(temp_list)
                temp_list = []
            # append the non alphabet content as a list to the final list
            final_list.append([char])

    if temp_list:
        final_list.append(temp_list)

    return final_list


def reverse_relevant_parts(parts):
    """Reverse only those sublists consisting of letters
    
    Input: list of lists, e.g. [['t', 'h', 'i', 's'], [' '], ['i', 's'], ['.']]
    Returns: list with sublists reversed that consist of letters only.
    """
    result = []
    for sublist in parts:
        # if all char in the sublist are letters, reverse the list
        if all(char.isalpha() for char in sublist):
            result.append(reverse_part(sublist))
        # if not, append the sublist directly
        else:
            result.append(sublist)
    return result

def glue(parts):
    """Transforms the list of sublists back into a new string
    
    Returns: string
    """
    sentence = ''
    for part in parts:
        word = part_to_str(part)
        sentence += word
    return sentence



def encrypt(sentence):
    """Reverses all consecutive letter parts in a string.

    Input: a string
    Returns: a string
    """
    # step1: split the input string into parts
    parts = split_in_parts(sentence)
    # step2: reverse the parts
    reversed_parts = reverse_relevant_parts(parts)
    # step3: glue the reversed parts together
    result = glue(reversed_parts)
    return result


if __name__ == "__main__":

    paragraph = "toN ylno si ti ysae ot eil htiw spam, ti's laitnesse. oT yartrop lufgninaem spihsnoitaler rof a xelpmoc, eerht-lanoisnemid dlrow no a talf teehs fo repap ro a oediv neercs, a pam tsum trotsid ytilaer. sA a elacs ledom, eht pam tsum esu slobmys taht tsomla syawla era yllanoitroporp hcum reggib ro rekciht naht eht serutaef yeht tneserper. oT diova gnidih lacitirc noitamrofni ni a gof fo liated, eht pam tsum reffo a evitceles, etelpmocni weiv fo ytilaer. erehT's on epacse morf eht cihpargotrac xodarap: ot tneserp a lufesu dna lufhturht erutcip, na etarucca pam tsum llet etihw seil. --- woH ot eil htiw spam, kraM reinomnoM, 1996."
    print(encrypt(paragraph))
    assert encrypt(encrypt(paragraph)) == paragraph

