import os

# Used for adding color to console
os.system('color')

# Elements to be replaced with their symbol => 'code':'symbol'
tokens = {'<0.5>': '½',
          '<mu>': 'μ',
          '<int>': '∫',
          '<inf>': '∞',
          '<x>': '×',
          '</>': '÷',
          '<Cdel>': 'Δ',
          '<sdel>': 'δ',
          '<pi>': 'π',
          '<theta>': 'θ',
          '<2root>': '√'}

# Raised when empty arguments are provided, no inbuilt error raised to avoid stopping the program
errors = {'^': 'Error[1]:Empty argument for superscript',
          '^^': 'Error[2]:Empty argument for subscript'}


# Convert input to superscript
def get_super(x) -> None:
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)


# Convert input to subscript
def get_sub(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)


# All tokens are replaced with their symbols
def convert(string):
    for i in tokens:
        string = string.replace(i, tokens[i])
    return string


# Exchanging superscript and subscript with their symbols
def lexer(string: str) -> str:
    output = ''
    string = convert(string)
    i = 0
    while string[i] != 'Ӂ':
        # Subscript and super script
        if string[i] == '^':
            if string[i + 1] == '^':
                output += get_sub(string[i + 2])
                i += 3
            else:
                output += get_super(string[i + 1])
                i += 2
        else:
            output += string[i]
            i += 1
    return output


def main():
    # Taking input with 'Ӂ' to signify end of line (testing solutions)
    string = input('\x1b[7;30;44m' + "INPUT >" + '\x1b[0m' + ' ') + 'Ӂ'
    while string != ':qӁ':
        try:
            # Show help table if help called
            if string == 'helpӁ':
                for i in tokens:
                    print(f"{i} -> {tokens[i]}")
            # Show possible errors, helpful for debugging
            elif string == 'errorsӁ':
                for i in errors:
                    print('\x1b[1;31;40m' + f"{i} -> {errors[i]}" + '\x1b[0m')
            # Output the converted string
            else:
                print('\x1b[7;30;42m' + "OUTPUT>" + '\x1b[0m' + " " + lexer(string))
        except IndexError:
            # Dealing with erroneous input
            if string == '^Ӂ':
                print('\x1b[1;31;40m' + f"{errors['^']}" + '\x1b[0m')
            elif string == '^^Ӂ':
                print('\x1b[1;31;40m' + f"{errors['^^']}" + '\x1b[0m')
            else:
                print('\x1b[1;31;40m' + 'ERROR> Incorrect input value' + '\x1b[0m')
        
        # Taking input for next iteration
        string = input('\x1b[7;30;44m' + "INPUT >" + '\x1b[0m' + ' ') + 'Ӂ'


if __name__ == "__main__":
    main()
