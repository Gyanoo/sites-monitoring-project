import sys
# import ui.stylesheet
import monitoring_main
import multiprocessing
import ui.gui


def main():
    app = ui.gui.QApplication(sys.argv)
    win = ui.gui.MainWindow()
    win.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()
    p1 = multiprocessing.Process(target=main)
    p2 = multiprocessing.Process(target=monitoring_main.start_monitor)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
