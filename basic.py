##############
 #Token
#############
TT_INT      = 'TT_INT'
TT_FLOAT    = 'FLOAT'
TT_PLUS     = 'PLUS'
TT_MINUS    = 'MINUS'
TT_MUL      = 'MUL'
TT_DIV      = 'DIV'
TT_LPAREN   = 'LPAREN'
TT_RPAREN   = 'RPAREN'
TT_POW     = 'POW'        # Power/Exponentiation **
TT_MOD     = 'MOD'        # Modulo %
TT_FLOOR   = 'FLOOR'      # Floor division //
TT_EQ      = 'EQ'         # Equal ==
TT_GT      = 'GT'         # Greater than >
TT_LT      = 'LT'         # Less than 
TT_GTE     = 'GTE'        # Greater than or equal >=
TT_LTE     = 'LTE'        # Less than or equal <=


#Define tokens
class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.type = value
    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'
    
##################
#LEXER
#################

#Text handling and position
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()


    def advance(self):
        self.pos += 1
        self.current_char = self.text[pos] if self.pos < len(self.text) else None
    
    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in '\t':
                self.advance()
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == '()':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()