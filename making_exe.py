import sys
from PyQt5.QtWidgets import *
from Main_program import *
from constants import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.acci = QLineEdit()
        self.acci.setPlaceholderText('사고자를 입력하세요')
        self.out = QLineEdit()
        self.out.setPlaceholderText('외출자를 입력하세요')
        self.out.returnPressed.connect(self.make_work)
        self.lbl = QLabel('근무결과')
        self.result = QTextEdit()

        grid = QGridLayout()
        grid.addWidget(self.acci, 0, 0)
        grid.addWidget(self.out, 1, 0)
        grid.addWidget(self.lbl, 2, 0)
        grid.addWidget(self.result, 3, 0)

        self.setLayout(grid)

        self.setWindowTitle('718근무 프로그램')
        self.setGeometry(100, 100, 1500, 800)
        self.show()

    def make_work(self):


        Time_Scheduler.acci = self.acci.text()
        Time_Scheduler.out = self.out.text()
        self.temp_work, self.real_worker, self.outing, self.today_time, self.today_group, self.p2, self.accident, self.no_return_work, self.hes_1, self.hes_2, self.hes_3, self.long_nighter = Time_Scheduler.scheduler(Timetable, which_group, work_group, is_weekend,
                                                                       p2)

        self.result.append("오늘 근무:" + self.today_group)
        self.result.append("총원 : " + str(len(self.p2)))

        self.result.append("사고자 수 : %d" % (len(self.accident)) + "\n외출자 수 %d" % (len(self.outing)) + "\n\n사고 내용\n사고자 : " + str([x.name for x in self.accident]) + "\n외출자 : " + str([x.name for x in self.outing]))
        self.result.append("\n복귀타 없는 외출자 수 : %d" % (len(self.no_return_work)) + "\n내용 : " + str([x.name for x in self.no_return_work]))

        self.result.append("\n현원 : %d" % len(self.real_worker))
        self.result.append("1타자 수 : %d" % len(self.hes_1) + str([x.name for x in self.hes_1]))
        self.result.append("2타자 수 : %d" % len(self.hes_2) + str([x.name for x in self.hes_2]))
        self.result.append("3타자 수 : %d" % len(self.hes_3) + str([x.name for x in self.hes_3]))

        if self.today_group == 'B':
            self.result.append("긴밤자 수 : %d" % len(self.long_nighter) + "긴밤자 : " + str([x.name for x in self.long_nighter]))
        for i in range(4):
            self.result.append(str(self.today_time[i]) + "\t" + str([x.name for x in self.temp_work[i]]))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

