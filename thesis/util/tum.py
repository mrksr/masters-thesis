# -*- coding: utf-8 -*-
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace, Literal


class TumStyle(Style):
    background_color = "#ffffff"
    default_style = ""

    styles = {
        Comment:                   "italic #58585A",
        Comment.Preproc:           "noitalic #65170B",

        Keyword:                   "bold #005293",
        Keyword.Pseudo:            "nobold",
        Keyword.Type:              "bold #90210F",

        Literal.Scalar:             "bold #90210F",

        Name.Variable:             "bold #C9651E",
        Name.Label:                "#005293",

        String:                    "#0073CF",
        String.Doc:                "italic",
        Number:                    "bold #C9651E",
    }
