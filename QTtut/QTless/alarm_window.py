"""
 * Author: Artsiom Khatitonau
 * Date: 11/2/2015
 * Time: 5:00 PM
"""

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication, QLabel, QSplashScreen
from PyQt4.QtCore import Qt, QTimer

from optparse import OptionParser
import datetime
import time
import sys

def main():
    parser = OptionParser()

    default_time = datetime.datetime.now()
    default_format = "%Y-%m-%d %H:%M:%S"
    default_msg = "DEFAULT MESSAGE: %s alarm" %default_time.strftime(default_format)

    parser.add_option("-t", "", dest="time", default=default_time.strftime(default_format))
    parser.add_option("-f", "", dest="format", default=default_format)
    parser.add_option("-m", "", dest="message", default=default_msg)

    (options, args) = parser.parse_args()

    cur_time = options.time
    cur_format = options.format

    try:
        frmt_time = cur_time
        cur_time = datetime.datetime.strptime(cur_time, cur_format)
        cur_message = "[%s] %s"%(frmt_time, options.message)
    except Exception as e:
        cur_message = default_msg
        cur_time = default_time

    print cur_time, cur_message
    app = QApplication(sys.argv)

    while datetime.datetime.now() <= cur_time:
        time.sleep(5)

    print "DONE"
    label = QLabel("<font color=red size=72> <b>%s</b></font>"%cur_message)
    # label.setWindowFlags(Qt.WindowStaysOnTopHint)
    label.setWindowFlags(Qt.SplashScreen)

    label.show()

    QTimer.singleShot(20000, app.quit)
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()
