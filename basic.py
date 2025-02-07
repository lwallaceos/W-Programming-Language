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
TT_POW      = 'POW'     # **
TT_MOD      = 'MOD'     # %
TT_FLOOR    = 'FLOOR'   # //
TT_GT       = 'GT'      # >
TT_LT       = 'LT'      # <
TT_EQ       = 'EQ'      # ==

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

    #First character increment
    def advance(self):
        self.pos += 1
        self.current_char = self.text[pos] if self.pos < len(self.text) else None
    
    #Next Character Peek
    def peek(self):
        peek_pos = self.pos +1
        return self.text[peek_pos] if peek_pos <len(self.text) else None

#################
#Operations
################

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
                if self.peek() == '*':          
                    tokens.append(Token(TT_POW))
                    self.advance()
                self.advance()
            elif self.current_char == '/':
                if self.peek() == '/':
                    tokens.append(Token(TT_FLOOR))
                    self.advance()
                    self.advance()
                else:
                    tokens.append(Token(TT_DIV))
                    self.advance()
                tokens.append(Token(TT_DIV))
                self.advance()
            
            elif self.current_char == '()':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()