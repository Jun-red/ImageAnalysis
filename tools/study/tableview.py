from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QStandardItem
from PyQt5.QtCore import QStandardItemModel
app = QApplication([])

window = QMainWindow()
window.setWindowTitle('Table View Example')

table_view = QTableView()
model = QStandardItemModel(4, 3)
for row in range(4):
    for column in range(3):
        item = QStandardItem(f'Row {row}, Column {column}')
        model.setItem(row, column, item)
table_view.setModel(model)

window.setCentralWidget(table_view)
window.show()

app.exec_()
