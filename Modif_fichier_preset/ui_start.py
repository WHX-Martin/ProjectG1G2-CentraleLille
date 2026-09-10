from PySide6.QtWidgets import QApplication, QMainWindow
from ui_Interface import Ui_MainWindow  # 导入生成的UI模块
import sys
from qt_material import apply_stylesheet
import sys
import logging
import os
from datetime import datetime


class LoggerWriter:
    def __init__(self, logger, level):
        self.logger = logger
        self.level = level

    def write(self, message):
        if message.strip():
            self.logger.log(self.level, message.strip())

    def flush(self):
        pass


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Presets Correction")


if __name__ == "__main__":
    # log
    log_folder = "log"
    os.makedirs(log_folder, exist_ok=True)

    log_file = os.path.join(log_folder, f"{datetime.now().strftime('%Y-%m-%d')}.log")

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )

    sys.stdout = LoggerWriter(logging.getLogger(), logging.INFO)
    sys.stderr = LoggerWriter(logging.getLogger(), logging.ERROR)

    # window
    app = QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(app, theme="dark_blue.xml")
    window.show()
    sys.exit(app.exec())
