"""
 * Author: Artsiom Khatitonau
 * Date: 11/3/2015
 * Time: 4:43 PM
"""


from PyQt4 import QtGui, QtCore, uic
import sys

if __name__ =="__main__":

    app = QtGui.QApplication(sys.argv)
    app.setStyle("cleanLooks")

    data = QtCore.QStringList()
    data << "One" <<"Two" << "Three" << QtCore.QString(u"dsd")

    listwidget = QtGui.QListWidget()
    listwidget.addItems(data)
    listwidget.show()

    for i in xrange(listwidget.count()):
        item = listwidget.item(i)
        print item.setFlags( item.flags() | QtCore.Qt.ItemIsEditable)

    combobox = QtGui.QComboBox()
    combobox.show()
    combobox.addItems(data)


    sys.exit(app.exec_())