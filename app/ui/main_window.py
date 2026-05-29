from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QScrollArea,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)

from app.importers.excel_importer import ExcelImporter


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Zebra Label System V2")
        self.resize(1400, 900)

        self.df = None

        self.setup_ui()

    def setup_ui(self):

        # =========================
        # CENTRAL WIDGET
        # =========================

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        central_widget.setLayout(self.main_layout)

        # =========================
        # TOOLBAR
        # =========================

        toolbar = QFrame()
        toolbar.setFixedHeight(70)

        toolbar.setStyleSheet("""
            background-color: #2b2b2b;
            border-bottom: 1px solid #444;
        """)

        toolbar_layout = QHBoxLayout()
        toolbar_layout.setContentsMargins(20, 10, 20, 10)

        toolbar.setLayout(toolbar_layout)

        title = QLabel("Zebra Label System V2")

        title.setStyleSheet("""
            color: white;
            font-size: 22px;
            font-weight: bold;
        """)

        self.import_button = QPushButton("Importar Excel")

        self.import_button.setFixedHeight(40)
        self.import_button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.import_button.clicked.connect(
            self.import_excel
        )

        toolbar_layout.addWidget(title)
        toolbar_layout.addStretch()
        toolbar_layout.addWidget(self.import_button)

        # =========================
        # BODY
        # =========================

        body_layout = QHBoxLayout()
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)

        # =========================
        # SIDEBAR
        # =========================

        sidebar = QFrame()
        sidebar.setFixedWidth(280)

        sidebar.setStyleSheet("""
            background-color: #f3f3f3;
            border-right: 1px solid #ccc;
        """)

        sidebar_layout = QVBoxLayout()
        sidebar_layout.setContentsMargins(15, 15, 15, 15)

        sidebar.setLayout(sidebar_layout)

        sidebar_title = QLabel("Painel")

        sidebar_title.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            padding-bottom: 10px;
        """)

        self.file_name_label = QLabel("Arquivo: Nenhum")

        self.file_name_label.setWordWrap(True)

        self.file_name_label.setStyleSheet("""
            font-size: 13px;
            padding: 8px;
            background-color: white;
            border: 1px solid #ccc;
            border-radius: 6px;
        """)

        self.total_rows_label = QLabel("Registros: 0")

        self.total_rows_label.setStyleSheet("""
            font-size: 13px;
            padding: 8px;
            background-color: white;
            border: 1px solid #ccc;
            border-radius: 6px;
        """)

        sidebar_layout.addWidget(sidebar_title)
        sidebar_layout.addWidget(self.file_name_label)
        sidebar_layout.addWidget(self.total_rows_label)
        sidebar_layout.addStretch()

        # =========================
        # PREVIEW AREA
        # =========================

        preview_container = QFrame()

        preview_container.setStyleSheet("""
            background-color: #ebebeb;
        """)

        preview_layout = QVBoxLayout()
        preview_layout.setContentsMargins(15, 15, 15, 15)

        preview_container.setLayout(preview_layout)

        preview_title = QLabel("Previews")

        preview_title.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
            padding-bottom: 10px;
        """)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)

        self.scroll_content = QWidget()

        self.scroll_layout = QVBoxLayout()
        self.scroll_layout.setSpacing(15)

        self.scroll_content.setLayout(self.scroll_layout)

        self.scroll_area.setWidget(self.scroll_content)

        preview_layout.addWidget(preview_title)
        preview_layout.addWidget(self.scroll_area)

        # =========================
        # ADD BODY
        # =========================

        body_layout.addWidget(sidebar)
        body_layout.addWidget(preview_container)

        # =========================
        # ADD MAIN LAYOUT
        # =========================

        self.main_layout.addWidget(toolbar)
        self.main_layout.addLayout(body_layout)

        # =========================
        # STATUS BAR
        # =========================

        status_bar = QStatusBar()
        status_bar.showMessage("Sistema iniciado")

        self.setStatusBar(status_bar)

        # =========================
        # INITIAL MOCK
        # =========================

        self.create_mock_previews()

    def create_mock_previews(self):

        self.clear_previews()

        for i in range(5):

            preview_card = self.create_preview_card(
                title=f"Etiqueta Preview {i + 1}",
                material="XXXXX",
                quantity="5"
            )

            self.scroll_layout.addWidget(preview_card)

        self.scroll_layout.addStretch()

    def create_preview_card(
        self,
        title,
        material,
        quantity
    ):

        preview_card = QFrame()

        preview_card.setFixedHeight(180)

        preview_card.setStyleSheet("""
            background-color: white;
            border: 1px solid #ccc;
            border-radius: 8px;
        """)

        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(15, 15, 15, 15)

        preview_card.setLayout(card_layout)

        card_title = QLabel(title)

        card_title.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
        """)

        card_info = QLabel(
            f"Material: {material}\n"
            f"Quantidade: {quantity}"
        )

        card_info.setStyleSheet("""
            font-size: 14px;
        """)

        card_layout.addWidget(card_title)
        card_layout.addSpacing(10)
        card_layout.addWidget(card_info)
        card_layout.addStretch()

        return preview_card

    def clear_previews(self):

        while self.scroll_layout.count():

            item = self.scroll_layout.takeAt(0)

            widget = item.widget()

            if widget is not None:
                widget.deleteLater()

    def import_excel(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Selecionar Excel",
            "",
            "Excel Files (*.xlsx)"
        )

        if not file_path:
            return

        try:

            self.df = ExcelImporter.read_excel(
                file_path
            )

            total_rows = len(self.df)

            self.file_name_label.setText(
                f"Arquivo:\n{file_path}"
            )

            self.total_rows_label.setText(
                f"Registros: {total_rows}"
            )

            self.statusBar().showMessage(
                f"Excel carregado com sucesso | "
                f"{total_rows} registros"
            )

            self.generate_previews()

            QMessageBox.information(
                self,
                "Importação",
                f"Excel carregado com sucesso!\n\n"
                f"Total de registros: {total_rows}"
            )

        except Exception as error:

            QMessageBox.critical(
                self,
                "Erro ao importar Excel",
                str(error)
            )

    def generate_previews(self):

        self.clear_previews()

        if self.df is None:
            return

        for index, row in self.df.head(20).iterrows():

            material = str(
                row.iloc[0]
            ) if len(row) > 0 else "N/A"

            quantity = str(
                row.iloc[1]
            ) if len(row) > 1 else "N/A"

            preview_card = self.create_preview_card(
                title=f"Etiqueta {index + 1}",
                material=material,
                quantity=quantity
            )

            self.scroll_layout.addWidget(
                preview_card
            )

        self.scroll_layout.addStretch()