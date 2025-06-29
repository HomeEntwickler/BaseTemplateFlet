
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
        self.bgcolor = Colors.GREEN_900

        self.content = Text("Text von ContentViewContainer")
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
