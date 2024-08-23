
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton,QWidget, QDialog
from PySide6.QtGui import QIcon, QPixmap, QPainter, QColor
from PySide6.QtCore import Qt, QSize, QPoint
from PySide6.QtSvg import QSvgRenderer
from ui_form import Ui_MainWindow
from ui_dialog import Ui_Dialog

import sys

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.old_position = None

        self.home_page_index = 0
        self.new_page_index = 1
        self.rupture_page_index = 2
        self.expiration_page_index = 3
        self.available_page_index = 4
        self.admin_page_index = 5

        self.general_page_index = 0
        self.add_page_index = 5
        self.report_page_index = 2
        self.analyse_page_index = 3
        self.unite_page_index = 4
        self.user_page_index = 1

        self.closed_menu= False
        self.previous_button = False
        self.previous_sub_button = False

        self.last_click_time = None
        self.double_click_interval = 300

        self.showMaximized()
        self.setWindow()
        self.listenerEvent()

    def open_dialog(self):
        dialog = CustomDialog(self)
        dialog.exec()

    def change_icon_color(self):
        # Charger et manipuler l'icône SVG
        svg_renderer = QSvgRenderer(":/icons/icons/chevron-left.svg")
        pixmap = QPixmap(100, 100)
        pixmap.fill(Qt.GlobalColor.transparent)  # Make the background transparent

        painter = QPainter(pixmap)
        svg_renderer.render(painter)
        painter.end()

        # Recolorier le pixmap
        colored_pixmap = QPixmap(pixmap.size())
        colored_pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(colored_pixmap)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Source)
        painter.drawPixmap(0, 0, pixmap)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
        painter.fillRect(colored_pixmap.rect(), QColor("red"))  # Change color here
        painter.end()

        icon = QIcon(colored_pixmap)
        self.ui.toggleMenuPushButton.setIcon(icon)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_position = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.old_position:
            delta = QPoint(event.globalPos() - self.old_position)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_position = event.globalPos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_position = None

    def on_mouse_press(self, event):
        if event.button() == Qt.LeftButton:
            if self.last_click_time and (event.timestamp() - self.last_click_time) < self.double_click_interval:
                # Double clic détecté
                self.setWindowSize()
                self.last_click_time = None
            else:
                # Premier clic
                self.last_click_time = event.timestamp()


    def closeEvent(self, event):
        # Créer une boîte de dialogue personnalisée
        reply = QMessageBox(self)
        reply.setWindowTitle("Confirmation")
        reply.setText("  Etes-vous sûr de vouloir fermer la fenêtre?   ")

        # Personnaliser les boutons
        yes_button = QPushButton("Oui")
        no_button = QPushButton("Non")

        reply.addButton(yes_button, QMessageBox.ButtonRole.AcceptRole)
        reply.addButton(no_button, QMessageBox.ButtonRole.RejectRole)


        # Appliquer un style aux boutons (facultatif)
        # yes_button.setStyleSheet("background-color: green; color: white;")
        # no_button.setStyleSheet("background-color: #e55222; color: white;")

        # Afficher la boîte de dialogue et capturer la réponse
        reply.exec()

        if reply.clickedButton() == yes_button:
            event.accept()
        else:
            event.ignore()

    def setWindow(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.menuHideIcon = QIcon()
        self.menuHideIcon.addFile(u":/icons/icons/chevron-left.svg", QSize(), QIcon.Normal, QIcon.Off)

        self.menuShowIcon = QIcon()
        self.menuShowIcon.addFile(u":/icons/icons/list.svg", QSize(), QIcon.Normal, QIcon.Off)



    def listenerEvent(self):
        self.ui.accueilPushButton.clicked.connect(lambda: self.changePage(self.ui.accueilPushButton, self.home_page_index))
        self.ui.newPushButton.clicked.connect(lambda: self.changePage(self.ui.newPushButton, self.new_page_index))
        self.ui.rupturePushButton.clicked.connect(lambda: self.changePage(self.ui.rupturePushButton, self.rupture_page_index))
        self.ui.expirationPushButton.clicked.connect(lambda: self.changePage(self.ui.expirationPushButton, self.expiration_page_index))
        self.ui.availablePushButton.clicked.connect(lambda: self.changePage(self.ui.availablePushButton, self.available_page_index))
        self.ui.adminPushButton.clicked.connect(lambda: self.changePage(self.ui.adminPushButton, self.add_page_index))

        self.ui.generalPushButton.clicked.connect(lambda: self.changeSubPage(self.ui.generalPushButton, self.general_page_index))
        self.ui.addPushButton.clicked.connect(lambda: self.changeSubPage(self.ui.addPushButton, self.add_page_index))
        self.ui.reportPushButton.clicked.connect(lambda: self.changeSubPage(self.ui.reportPushButton, self.report_page_index))
        self.ui.analysePushButton.clicked.connect(lambda: self.changeSubPage(self.ui.analysePushButton, self.analyse_page_index))
        self.ui.userPushButton.clicked.connect(lambda: self.changeSubPage(self.ui.userPushButton, self.user_page_index))
        self.ui.unitePushButton.clicked.connect(lambda: self.changeSubPage(self.ui.unitePushButton, self.user_page_index))

        self.ui.topBarWidget.mousePressEvent = self.on_mouse_press


        self.ui.toggleMenuPushButton.clicked.connect(self.toggleMenu)

        getattr(self.ui, "reducePushButton").clicked.connect(lambda: self.showMinimized())
        getattr(self.ui, "closePushButton").clicked.connect(lambda: self.close())
        getattr(self.ui, "enlargePushButton").clicked.connect(lambda: self.setWindowSize())
        # getattr(self.ui, "topBarWidget").mouseDoubleClickEvent = self.toggleWindowSize



    def changePage(self,button, index):
        print(self.previous_button)
        if button is not None:
            button_id = button.objectName()
            self.ui.stackedWidget.setCurrentIndex(index)
            if self.previous_button:
                self.previous_button.setStyleSheet("")
            button.setStyleSheet("background-color: #2c313c;")
            self.previous_button = button

    def changeSubPage(self, button, index):

        if button is not None:
            button_id = button.objectName()
            self.ui.adminStackedWidget.setCurrentIndex(index)
            if self.previous_sub_button:
                self.previous_sub_button.setStyleSheet("")
            button.setStyleSheet("background-color: #838ea2;")
            self.previous_sub_button = button





    def toggleMenu(self):
        if self.closed_menu:
            self.ui.leftWidget.setMinimumWidth(300)
            self.ui.leftWidget.setMaximumWidth(300)
            self.closed_menu=False
            self.ui.toggleMenuPushButton.setIcon(self.menuHideIcon)

        else:
            self.ui.leftWidget.setMinimumWidth(0)
            self.ui.leftWidget.setMaximumWidth(0)
            self.closed_menu=True
            self.ui.toggleMenuPushButton.setIcon(self.menuShowIcon)

    def setWindowSize(self):
        if(self.isMaximized()):
            self.showNormal()
            self.center()
        else:
            self.showMaximized()

    def center(self):
        # Obtenir la géométrie de l'écran principal
        screen_geometry = QApplication.primaryScreen().availableGeometry()

        # Calculer la position centrale de la fenêtre
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())

        # Déplacer la fenêtre à la position calculée
        self.move(window_geometry.topLeft())

    def open_new_page(self):
        # Implémenter l'ouverture d'une nouvelle page
        new_window = QWidget()
        new_window.setWindowTitle("New Page")
        new_window.setGeometry(150, 150, 300, 200)
        new_window.show()
        # Garder une référence pour éviter que la fenêtre soit fermée immédiatement
        self.new_window = new_window


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

