import tkstyle
from cyberpunk_theme import constant


def get_style():
    style = tkstyle.Text()
    style.font = constant.FONT_FAV_NORMAL
    style.foreground = "#9B9B9B"
    style.background = "#1C2024"
    style.selectBackground = "#105B74"
    style.selectForeground = "#D5D5FF"
    style.readonlyBackground = "#181C20"
    style.inactiveSelectBackground = "#105B74"
    style.disabledBackground = "#15191D"
    style.insertBackground = "#9B9B9B"
    style.highlightThickness = 0
    style.relief = "flat"
    return style
