from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Zebra Label System V2")
        self.resize(1400, 900)

        self.setup_ui()

    def setup_ui(self):

        # =========================
        # CENTRAL WIDGET
        # =========================

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

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
        toolbar.setLayout(toolbar_layout)

        title = QLabel("Zebra Label System V2")
        title.setStyleSheet("""
            color: white;
            font-size: 22px;
            font-weight: bold;
        """)

        import_button = QPushButton("Importar Excel")
        import_button.setFixedHeight(40)

        toolbar_layout.addWidget(title)
        toolbar_layout.addStretch()
        toolbar_layout.addWidget(import_button)

        # =========================
        # BODY
        # =========================

        body_layout = QHBoxLayout()

        # =========================
        # SIDEBAR
        # =========================

        sidebar = QFrame()
        sidebar.setFixedWidth(250)
        sidebar.setStyleSheet("""
            background-color: #f3f3f3;
            border-right: 1px solid #ccc;
        """)

        sidebar_layout = QVBoxLayout()
        sidebar.setLayout(sidebar_layout)

        sidebar_title = QLabel("Painel")
        sidebar_title.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            padding: 10px;
        """)

        sidebar_layout.addWidget(sidebar_title)
        sidebar_layout.addStretch()

        # =========================
        # PREVIEW AREA
        # =========================

        preview_container = QFrame()

        preview_layout = QVBoxLayout()
        preview_container.setLayout(preview_layout)

        preview_title = QLabel("Previews")
        preview_title.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
            padding: 10px;
        """)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_content = QWidget()

        scroll_layout = QVBoxLayout()
        scroll_content.setLayout(scroll_layout)

        # Mock previews
        for i in range(5):

            preview_card = QFrame()
            preview_card.setFixedHeight(180)

            preview_card.setStyleSheet("""
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 8px;
            """)

            card_layout = QVBoxLayout()
            preview_card.setLayout(card_layout)

            card_title = QLabel(f"Etiqueta Preview {i + 1}")
            card_title.setStyleSheet("""
                font-size: 16px;
                font-weight: bold;
            """)

            card_info = QLabel("Material: XXXXX\nQuantidade: 5")

            card_layout.addWidget(card_title)
            card_layout.addWidget(card_info)

            scroll_layout.addWidget(preview_card)

        scroll_layout.addStretch()

        scroll_area.setWidget(scroll_content)

        preview_layout.addWidget(preview_title)
        preview_layout.addWidget(scroll_area)

        # =========================
        # ADD BODY
        # =========================

        body_layout.addWidget(sidebar)
        body_layout.addWidget(preview_container)

        # =========================
        # ADD MAIN LAYOUT
        # =========================

        main_layout.addWidget(toolbar)
        main_layout.addLayout(body_layout)

        # =========================
        # STATUS BAR
        # =========================

        status_bar = QStatusBar()
        status_bar.showMessage("Sistema iniciado")

        self.setStatusBar(status_bar)