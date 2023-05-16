from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from lista import *

class ScoreboardWindow(QMainWindow):
    def setup(self, score_list):
        super().__init__()

        self.setWindowTitle("Scoreboard")
        self.setGeometry(100, 100, 400, 300)

        self.score_table = QTableWidget(self)
        self.score_table.setColumnCount(2)
        self.score_table.setHorizontalHeaderLabels(["Name", "Score"])

        self.populate_table(score_list)

        self.setCentralWidget(self.score_table)

    def populate_table(self, score_list):
        current = score_list.head
        row = 0
        while current:
            self.score_table.insertRow(row)  

            name_item = QTableWidgetItem(current.name)
            score_item = QTableWidgetItem(str(current.score))

            self.score_table.setItem(row, 0, name_item)
            self.score_table.setItem(row, 1, score_item)

            current = current.next
            row += 1

if __name__ == "__main__":
    app = QApplication([])
    score_list = LinkedList.load_scores("puntajes.txt")

    window = ScoreboardWindow(score_list)
    window.show()

    app.exec_()