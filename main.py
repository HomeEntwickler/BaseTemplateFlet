from flet import *
from Sidebar import*
from Details import*

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
        self.sidebarContainer = SidebarContainer(self)
#        self.detailsContainer = DetailsContainer(self)

        self.toolBar = Container(
            bgcolor = "#17181d",
            margin = margin.only(left = 0, top = -8, right = -8), #-8,
            content = Row(
                controls = [
                    IconButton(
                        icon = Icons.VIEW_SIDEBAR_OUTLINED, 
                        icon_color = Colors.GREY_500,
                        tooltip = "Anzeige der Seitenleiste auswählen",
                        on_click = self.sidebarAnimate,
                    ),
                    Container(expand = True),
                    PopupMenuButton(
                        icon = Icons.MORE_VERT,
                        tooltip = "Mail Account konfigurieren",
                        items = [
                            PopupMenuItem(icon = Icons.MAIL_LOCK_OUTLINED, text = "Mail Account konfigurieren", on_click = lambda e: self.configureAccount(e)),
                        ],
                        opacity = 0.5,
                    ), 
                ]
            )
        )

        self.contentContainer.content = Row(
            controls = [
                self.detailsContainer,
                # self.rezeptContainer,
                # self.tabbarContainer,
            ]
        )

        self.content = Row(
            expand = True,
            controls = [
                self.sidebarContainer,
                Column(
                    expand = 4,
                    controls = [
                        self.toolBar,
                        self.contentContainer,
                    ]
                ),
            ]
        )

    def sidebarAnimate(self, e):
        self.sidebarContainer.width = 0 if self.sidebarContainer.width == 280 else 280  
        self.sidebarContainer.update()

    def configureAccount(self, e):
        print("configureAccount")
        # configureEmailAccount = ConfigureEmailAccount(self)
        # configureEmailAccount.showDialog(e)

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
