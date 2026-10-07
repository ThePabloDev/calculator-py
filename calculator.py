import tkinter as tk
from tkinter import ttk, messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculadora Python')
        self.geometry('340x455')
        self.minsize(300, 400)
        self.configure(bg='#141820')
        self.expressao = ''
        self.display = tk.StringVar(value='0')
        visor = tk.Entry(self, textvariable=self.display, font=('Segoe UI', 26),
                         justify='right', bd=0, bg='#202633', fg='white',
                         insertbackground='white', state='readonly', readonlybackground='#202633')
        visor.pack(fill='x', padx=14, pady=(20, 15), ipady=16)
        grade = tk.Frame(self, bg='#141820')
        grade.pack(expand=True, fill='both', padx=12, pady=(0, 14))
        botoes = [
            ['C', '⌫', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '−'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '='],
        ]
        for i in range(5):
            grade.rowconfigure(i, weight=1)
        for j in range(4):
            grade.columnconfigure(j, weight=1)
        for i, linha in enumerate(botoes):
            for j, botao in enumerate(linha):
                destaque = botao == '='
                operador = botao in ('÷', '×', '−', '+', '%')
                bg = '#438cf5' if destaque else ('#2d3950' if operador else '#252c39')
                tk.Button(grade, text=botao, font=('Segoe UI', 17, 'bold'),
                          bg=bg, fg='white', activebackground='#526b90',
                          activeforeground='white', relief='flat', bd=0,
                          command=lambda x=botao: self.clicar(x)).grid(
                              row=i, column=j, sticky='nsew', padx=3, pady=3)
        self.bind('<Key>', self.tecla)
isso é um teste, beleza
    def atualizar(self):
        self.display.set(self.expressao or '0')

    def clicar(self, botao):
        if botao == 'C':
            self.expressao = ''
        elif botao == '⌫':
            self.expressao = self.expressao[:-1]

                       ast.UAdd: operator.pos}
                def resolver(node):
             ance(valor, float) and valor.is_integer() else str(round(valor, 10))
            except (ValueError, SyntaxError, ZeroDivisionError, OverflowError):
                self.display.set('Erro')
                self.expressao = ''
                return
        else:
            self.expressao += botao
        self.atualizar()

    def tecla(self, event):
        tecla = event.char
        if tecla in '0123456789.+%': self.clicar(tecla)
        elif tecla == '-': self.clicar('−')
        elif tecla == '*': self.clicar('×')
        elif tecla == '/': self.clicar('÷')
        elif event.keysym in ('Return', 'KP_Enter'): self.clicar('=')
        elif event.keysym == 'BackSpace': self.clicar('⌫')
        elif event.keysym == 'Escape': self.clicar('C')

if __name__ == '__main__':
    Calculadora().mainloop()
