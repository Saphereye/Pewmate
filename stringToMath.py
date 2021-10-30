import os
os.system('color')
# Words to math converter
tokens = {'<0.5>' :'½',
          '<mu>'  :'μ',
          '<int>' :'∫',
          '<inf>' :'∞',
          '<x>'   :'×',
          '</>'   :'÷',
          '<Cdel>':'Δ',
          '<sdel>':'δ'}

# function to convert to superscript
def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)

# function to convert to subscript
def get_sub(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)

#string = 'a^2 + b^2 + 2ab = (a + b)^2'

"""
elements = string.split(' ')
for i in elements:
    if (i in tokens):
        print(tokens[i],end=' ')
    else:
        print(i,end=' ')
"""

#major change with reference to token dictionary
def convert(string):
    for i in tokens:
        string = string.replace(i,tokens[i])
    return(string)

#subtle changes like super scripte and subscript
def lexer(string):
    output = ''
    string = convert(string)
    i=0
    while(string[i]!='Ӂ'):
        #Subscript and super script
        if (string[i]=='^'):
            if (string[i+1] == '^'):
                output+=get_sub(string[i+2])
                i+=3
            else:
                output+=get_super(string[i+1])
                i+=2
        else:
            output+=string[i]
            i+=1
    return output

def main():
    string = input('\x1b[7;30;44m'+"INPUT >"+'\x1b[0m'+' ')+'Ӂ'
    while(string!=':qӁ'):
        try:
            if string=='helpӁ':
                for i in tokens:
                    print(f"{i} -> {tokens[i]}")
            else:
                print('\x1b[7;30;42m'+"OUTPUT>"+'\x1b[0m'+" "+lexer(string))
        except:
            print('\x1b[1;31;40m'+'ERROR> Incorrect input value'+'\x1b[0m')
        string = input('\x1b[7;30;44m'+"INPUT >"+'\x1b[0m'+' ')+'Ӂ'


if __name__ == "__main__":
    main()
