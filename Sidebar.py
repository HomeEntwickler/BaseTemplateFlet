from flet import *

#----------------------------------------------------------------------------------------------
class SidebarContainer(Container):
    def __init__(self, homePage) -> None:
        super().__init__()
        self.homePage = homePage
        self.width = 280
        self.alignment = alignment.top_left
        self.margin = margin.only(top = -8)
        self.bgcolor = "#17181d"
        self.animate = animation.Animation(800, AnimationCurve.LINEAR)
        self.sectionView = SectionView(self.homePage)
        self.content = self.sectionView
#----------------------------------------------------------------------------------------------
class SectionView(Container):
    def __init__(self, homePage) -> None:
        super().__init__()
        self.homePage = homePage
        self.expand = True
        self.cardBgColor = None
        self.column: Column = Column(scroll = True)

    def createToolbar(self):
        self.column.controls.append(Column(
            scroll = True,
            controls = [
                Row(
                    alignment = MainAxisAlignment.SPACE_AROUND,
                    controls = [
                        PopupMenuButton(
                            icon = Icons.MORE_VERT,
                            tooltip = "Menü anzeigen",
                            items = [
                                PopupMenuItem(icon = Icons.IMPORT_CONTACTS_OUTLINED, text = "Rezeptbuch öffnen"), #on_click = lambda _: 
                                    # self.toolbarFilePicker.pick_files(dialog_title = "Rezeptbuch", file_type = FilePickerFileType.CUSTOM, allowed_extensions = ["sqlite"], allow_multiple = False)),
                                PopupMenuItem(icon = Icons.NEWSPAPER, text = "Neues Rezeptbuch"), #on_click = lambda e: self.newRecipeCollection(e)),
                            ],
                        opacity = 0.5,
                        ),
                        Text("Kategorien", theme_style = TextThemeStyle.TITLE_LARGE, color = Colors.GREY_500),
                        IconButton(
                            icon = Icons.ADD, 
                            icon_color = Colors.GREY_500,
                            tooltip = "Neue Kategorie", 
#                            on_click = self.AddKategorien
                        ),
                    ],
                ),
            ],
            alignment = MainAxisAlignment.START,
            )
        )

    def build(self):
        self.column.controls.clear()
        self.createToolbar()
        # self.createSectionView()
        self.content = self.column
        # self.page.overlay.append(self.toolbarFilePicker)
