from PyQt5.QtWidgets import QApplication, QMainWindow, QListView
from PyQt5.QtCore import QStringListModel
app = QApplication([])

window = QMainWindow()
window.setWindowTitle('List View Example')

list_view = QListView()
model = QStringListModel()
model.setStringList(['Item 1', 'Item 2', 'Item 3'])
list_view.setModel(model)

window.setCentralWidget(list_view)
window.show()

app.exec_()
