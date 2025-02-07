##############
#Constants
###############
DIGITS ='123456789'

############################
#Errors
############################
class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        result  = f'{self.error_name}: {self.details}\n'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)

#######################################
# POSITION
#######################################

class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)

        
################################
 #Token
###############################
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
    def __init__(self, type_, value = None):
        self.type = type_
        self.type = value
    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'
    
######################################
#LEXER
#####################################

#Text handling and position
class Lexer:
    def __init__(self, fn ,text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, self.fn, text)
        self.current_char = None
        self.advance()

    #First character increment
    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
    
    #Next Character Peek
    def peek(self):
        peek_pos = self.pos +1
        return self.text[peek_pos] if peek_pos <len(self.text) else None

##################################
#Operations
##################################

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in '\t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
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
            else:
                char = self.current_char
                self.advance()
                return[], IllegalCharError("'"+char+"'")
        return tokens, None

def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))

######################################
##############RUN#####################
######################################
def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()

    return tokens, error