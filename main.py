from flet import*

def main(page: Page):
    page.window.min_width = 1024
    page.window.min_height = 600
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.theme_mode = 'dark'

    page.add(
      Container(
        bgcolor = Colors.BLUE_900,
        padding = 16,
        content = Text("Das ist GitHub App"),
      )
    )
#------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app(target = main, assets_dir = "assets")
  
