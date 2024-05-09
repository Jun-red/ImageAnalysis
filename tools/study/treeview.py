from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel

app = QApplication([])

window = QMainWindow()
window.setWindowTitle('Tree View Example')

tree_view = QTreeView()
model = QFileSystemModel()
model.setRootPath('')
tree_view.setModel(model)

window.setCentralWidget(tree_view)
window.show()

app.exec_()
