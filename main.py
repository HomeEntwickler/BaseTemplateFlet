
from flet import *
#from Sidebar import*
#from Details import*

class ContentContainer(Container):
    def __init__(self) -> None:
        super().__init__()
        self.expand = 4
        self.border_radius = 8
        self.bgcolor = Colors.GREEN_900
#------------------------------------------------------------------------------------------------------------
class ContentViewContainer(Container):
    def __init__(self, homePage) -> None:
        super().__init__()
        self.homePage = homePage
        self.expand = 4

        self.contentContainer = ContentContainer()

        self.toolBar = Container(
            bgcolor = "#17181d",
            margin = margin.only(left = 0, top = -8, right = -8),
            content = Row(
                controls = [
                    IconButton(
                        icon = Icons.VIEW_SIDEBAR_OUTLINED, 
                        icon_color = Colors.GREY_500,
                        tooltip = "Anzeige der Seitenleiste auswählen",
#                        on_click = self.sidebarAnimate,
                    ),
                    Container(expand = True),
                    PopupMenuButton(
                        icon = Icons.MORE_VERT,
                        tooltip = "Mail Account konfigurieren",
                        items = [
                            PopupMenuItem(icon = Icons.MAIL_LOCK_OUTLINED, text = "Mail Account konfigurieren"), #on_click = lambda e: self.configureAccount(e)),
                        ],
                        opacity = 0.5,
                    ), 
                ]
            )
        )


        self.content = Row(
            expand = True,
            controls = [
#                self.sidebarContainer,
                Column(
                    expand = True,
                    controls = [
                        self.toolBar,
                        self.contentContainer,
                    ]
                ),
            ]
        )
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
def main(page: Page):
    page.window.min_width = 1024
    page.window.min_height = 600
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.theme_mode = 'dark'

    contentViewContainer = ContentViewContainer(page)

    page.add(contentViewContainer)
#------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
        app(target = main)
#    app(target = main, assets_dir = "assets")
#    app(target = main(), view = WEB_BROWSER)
#------------------------------------------------------------------------------------------------------------
