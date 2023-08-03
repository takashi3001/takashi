import sys
from PyQt5.QtWidgets import *
class E(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text = QTextEdit(self)
        self.setCentralWidget(self.text)
        self.setWindowTitle('pO - Editor de Texto')
        self.setGeometry(100, 100, 800, 600)
        self.f = ''
        self.a = [
            ('Novo', self.new),
            ('Abrir', self.o),
            ('Salvar', self.s),
            ('Desfazer', self.text.undo),
            ('Refazer', self.text.redo),
        ]
        self.c([{'Arquivo': ['Novo', 'Abrir', 'Salvar']}, {'Editar': ['Desfazer', 'Refazer']}])
        self.setStyleSheet("background-color: #1e1e1e; color: #f0f0f0;")
    def c(self, m):
        for i in m:
            for j in i:
                m = self.menuBar().addMenu(j)
                for t in i[j]:
                    a = QAction(t, self)
                    setattr(self, f'{t.lower()}_action', a)
                    m.addAction(getattr(self, f'{t.lower()}_action'))
    def new(self):
        self.text.clear()
        self.f = ''
    def o(self):
        n, _ = QFileDialog.getOpenFileName(self, 'Abrir arquivo', '', 'Arquivos de texto (*.txt);;Todos os arquivos (*)')
        if n:
            with open(n, 'r') as a:
                self.text.setPlainText(a.read())
            self.f = n
    def s(self):
        if self.f:
            with open(self.f, 'w') as a:
                a.write(self.text.toPlainText())
        else:
            n, _ = QFileDialog.getSaveFileName(self, 'Salvar arquivo', '', 'Arquivos de texto (*.txt);;Todos os arquivos (*)')
            if n:
                with open(n, 'w') as a:
                    a.write(self.text.toPlainText())
                self.f = n
if __name__ == '__main__':
    a = QApplication(sys.argv)
    e = E()
    e.show()
    sys.exit(a.exec_())

