import loguru
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from src.utils.call_windows_default_console_cmd import call_windows_default_console_cmd
from src.utils.cmd_text_edit import CMDTextEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window - PySide6 Debug Console Example")
        self.resize(500, 250)

        self.debug_console_window = CMDTextEdit()
        self.debug_console_window.setWindowTitle("Debug Console - Press ESC to hide")
        self.debug_console_window.resize(800, 800)
        self.debug_console_window.move(100, 100)
        self.debug_console_window.hide()

        self.initUI()

    def initUI(self):
        self.generate_debug_log()
        self.show_debug_console_checkbox = QCheckBox("Show Debug Console", self)
        self.show_debug_console_checkbox.setChecked(False)

        self.show_debug_console_checkbox.stateChanged.connect(
            self.show_or_hide_debug_console_function
        )
        self.debug_console_window.window_hidden_signal.connect(
            lambda: self.show_debug_console_checkbox.setChecked(False)
        )  # Press ESC to hide

        self.show_default_console_button = QPushButton("Show Default Console", self)
        self.show_default_console_button.clicked.connect(
            self.show_default_console_button_function
        )

        self.default_console_return_code_label = QLabel("Default Console Return Code: ")

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.show_debug_console_checkbox)
        self.layout.addWidget(self.show_default_console_button)
        self.layout.addWidget(self.default_console_return_code_label)
        self.setLayout(self.layout)

    def show_or_hide_debug_console_function(self):
        if self.show_debug_console_checkbox.isChecked():
            self.debug_console_window.show()
        else:
            self.debug_console_window.hide()

    def show_default_console_button_function(self):
        # QSS to initialize the label with default text and color
        self.default_console_return_code_label.setText("Default Console Return Code: ")
        self.default_console_return_code_label.setStyleSheet("QLabel { color: black; }")

        return_code = call_windows_default_console_cmd()

        if return_code == 0:
            self.default_console_return_code_label.setText(
                "Default Console Return Code: 0"
            )
            # QSS to highlight the label in green
            self.default_console_return_code_label.setStyleSheet(
                "QLabel { color: green; }"
            )
        else:
            self.default_console_return_code_label.setText(
                f"Default Console Return Code: {return_code}"
            )
            # QSS to highlight the label in red
            self.default_console_return_code_label.setStyleSheet(
                "QLabel { color: red; }"
            )

    def generate_debug_log(self):
        self.debug_console_window.run_cmd(
            "ping 127.0.0.1",
        )
        loguru.logger.info("Hello World!")
        loguru.logger.error("This is an error message")
        loguru.logger.warning("This is a warning message")
        loguru.logger.debug("This is a debug message")
        loguru.logger.critical("我是一段中文日志信息")


def main():
    app = QApplication()
    main_window = MainWindow()
    main_window.show()
    app.exec()
