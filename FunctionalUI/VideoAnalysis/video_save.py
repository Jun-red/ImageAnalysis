import sys

import PyQt5.QtWidgets as qw
import PyQt5.QtCore as qc

from DesignerUI.PyUI import Ui_video_save


class MySave(qw.QDialog, Ui_video_save.Ui_Form):
    save_data = qc.pyqtSignal(str, str, int, str)
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        
        self.save_out_type = "" # 保存类型
        self.save_out_path = "" # 保存地址
        self.save_method = 0    # 保存方法
        self.save_method_data = "" # 保存数据

        self.save_yes.clicked.connect(self.on_save_yes_cb)

        self.save_address.clicked.connect(self.on_choose_path_cb)

    def on_choose_path_cb(self):
        m = qw.QFileDialog.getExistingDirectory(None,"选取文件夹",".")  # 起始路径
        self.save_input_path.setText(m)

    def on_save_yes_cb(self):

        # 保存地址区域
        self.save_out_type = self.save_input_type.currentText()
        self.save_out_path = self.save_input_path.text()
        # if self.save_out_path == "":
        #     #无输入即为空

        # 保存方法区域
        if self.radioButton.isChecked():
            # "快捷键保存"
            self.save_method = 1
            self.save_method_data = self.save_keyboard.text()

        elif self.radioButton_2.isChecked():
            # "帧数保存"
            self.save_method = 2
            self.save_method_data = self.save_num.text()
        elif self.radioButton_3.isChecked():
            # ""时间保存(ms)""
            self.save_method = 3
            self.save_method_data = self.save_time.text()

        elif self.radioButton_4.isChecked():
            # ""不保存""
            self.save_method = 0
            self.save_method_data = ""
        # print('------------------------------------------')
        # print(self.save_out_type)
        # print(self.save_out_path)
        # print(self.save_method)
        # print(self.save_method_data)
        # print('------------------------------------------')
        # 关闭UI
        self.save_data.emit(self.save_out_path, self.save_out_type, self.save_method, self.save_method_data)
    