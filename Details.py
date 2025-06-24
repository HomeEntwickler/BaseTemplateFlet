from flet import*

class DetailsContainer(Container):
    def __init__(self, homePage) -> None:
        super().__init__()
        self.homePage = homePage
        self.expand = 1
        self.bgcolor = Colors.GREEN_900 #"#17181d"
        self.alignment = alignment.top_left
#------------------------------------------------------------------------------------------------------------
