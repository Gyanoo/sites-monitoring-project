import ui.gui
import sys
# import ui.stylesheet

def main():
    app = ui.gui.QApplication(sys.argv)
    win = ui.gui.MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
