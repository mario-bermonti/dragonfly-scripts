# The MIT License (MIT)
#
# Copyright (c) 2013 Chris Cowan

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text,
                       Integer, CompoundRule, Choice, RuleRef, Alternative,
                       Repetition)

context = AppContext(title="python")
grammar = Grammar("python", context=context)

rules = MappingRule(
    name = "python",
    mapping = {
        # general commands for buffers, windows, etc.
        "open file": Key("c-o"),
        "run file": Key("f5"),
        "close file": Key("a-f4"),
        "yes": Text("yes"),
        "no": Text("no"),

        # programming constructs
        "new class": Text("class ():") + Key("left, left, left"),
        "new function": Text("def ():") + Key("left, left, left"),
        "new conditional": Text("if :") + Key("left"),
        "new while loop": Text("while :") + Key("left"),
        "new for loop": Text("for  in :") + Key("left, left, left, left, left"),
        "print statement": Text("print()") + Key("left"),
        "pass":  Text("pass"),
        "self": Text("self."),
        "for loop": Text("for"),
        "new dictionary": Text("dict()"),
        "find coordinates": Text("coords()"),

        # movements
        "to last": Key("end"),
        "to start": Key("home"),
        "to top": Key("c-home"),
        "to bottom": Key("c-end"),
        # SPELLING AND SYMBOL
        # lowercase letters
        "alpha": Text("a"),
        "bravo": Text("b"),
        "charlie": Text("c"),
        "delta": Text("d"),
        "echo": Text("e"),
        "fox": Text("f"),
        "golf": Text("g"),
        "hotel": Text("h"),
        "indie": Text("i"),
        "juliet": Text("j"),
        "kick": Text("k"),
        "lame": Text("l"),
        "mike": Text("m"),
        "november": Text("n"),
        "oscar": Text("o"),
        "pancake": Text("p"),
        "quebec": Text("q"),
        "romeo": Text("r"),
        "sierra": Text("s"),
        "tango": Text("t"),
        "uniform": Text("u"),
        "victor": Text("v"),
        "whiskey": Text("w"),
        "x-ray": Text("x"),
        "yep": Text("y"),
        "zappy": Text("z"),
        # uppercase letters
        "bic alpha": Text("A"),
        "bic bravo": Text("B"),
        "bic charlie": Text("C"),
        "bic delta": Text("D"),
        "bic echo": Text("E"),
        "bic fox": Text("F"),
        "bic golf": Text("G"),
        "bic hotel": Text("H"),
        "bic indie": Text("I"),
        "bic juliet": Text("J"),
        "bic kick": Text("K"),
        "bic lame": Text("L"),
        "bic mike": Text("M"),
        "bic november": Text("N"),
        "bic oscar": Text("O"),
        "bic pancake": Text("P"),
        "bic quebec": Text("Q"),
        "bic romeo": Text("R"),
        "bic sierra": Text("S"),
        "bic tango": Text("T"),
        "bic uniform": Text("U"),
        "bic victor": Text("V"),
        "bic whiskey": Text("W"),
        "bic x-ray": Text("X"),
        "bic yep": Text("Y"),
        "bic zappy": Text("Z"),

        # numbers
        "zero":  Text("0"),
        "one": Text("1"),
        "two": Text("2"),
        "three": Text("3"),
        "four": Text("4"),
        "five": Text("5"),
        "six": Text("6"),
        "seven": Text("7"),
        "eight": Text("8"),
        "nine": Text("9"),

        # symbols
        "semi": Text(";"),
        "commie": Key("comma"),
        "corn": Key("colon"),
        "left single": Key("squote"),
        "left double": Key("dquote"),
        "left paren": Key("lparen"),
        "right paren": Key("rparen"),
        "left brace": Key("lbrace"),
        "right brace": Key("rbrace"),
        "left bracket": Key("lbracket"),
        "right bracket": Key("rbracket"),
        "spa": Key("space"),
        "plus": Key("space, plus, space"),
        "minus": Key("space, minus, space"),
        "equals": Key("space, equal, space"),
        "is equals to": Key("equal"),
        "Ash": Key("hyphen"),
        "times [<text>]": Text("* ") + Text("%(text)s"),
        "braces": Key("lbrace, rbrace") + Key("left"),
        "brackets": Key("lbracket, rbracket") + Key("left"),
        "parens": Key("lparen, rparen") + Key("left"),
        "angles": Key("langle, rangle") + Key("left"),
        "doubles": Key("dquote, dquote") + Key("left"),
        "singles": Key("squote, squote") + Key("left"),
        "exclamation": Key("exclamation"),
        "greater than": Text(" => "),
        "double equals": Text(" == "),
        "not equals": Text(" != "),
        "pound": Text("#"),
        "dot": Text("."),

        # editing
        "indent": Key("tab"),
        "indent out": Key("s-tab"),
        "copy": Key("c-c"),
        "cut": Key("c-x"),
        "paste": Key("c-v"),
        "undo": Key("c-z"),
        "again": Key("c-y"),
   },

    extras = [
        Dictation("text", format=False),
        Dictation("mark", format=False),
        Integer("n", 1, 20000),
        Integer("scroll_by", 1, 20000),
      ],
    defaults = {
      "text" : "",
      "mark": "a",
      "n" : 1,
      "scroll_by" : 1
      }
    )


class Identifiers(CompoundRule):
    """The class identifiers was taken from Cesar Crusius' repository
    (https://github.com/ccrusius/dragonfly-modules).
    The specs determine the properties of the words.

    The options are the following:
    If the first spec is true then all the letters are uppercase.

    If the second spec is true then the first words will be cap.

    If the third spec is true then the first letter of each word will be cap,
    except for the first word.

    If the fourth spec is true then the separator specified will be
    used to join the words.
    """

    spec = "<naming> <text>"
    extras = [
        Choice("naming", {
            "constant": [True, False, False, "_"],
            "variable": [False, False, True, ""],
            "snake": [False, False, False, "_"],
            "class": [False, True, True, ""],
            "fragment": [False, False, False, " "],
            "sentence": [False, True, False, " "],
            "file path": [False, False, False, "\\"],
            "dot notation": [False, False, False, "."]
        }),
        Dictation("text")
    ]

    def _process_recognition(self, node, extras):
        spec = extras["naming"]
        text = extras["text"].format()
        text = text.upper() if spec[0] else text.lower()
        words = text.split(" ")
        if len(words) == 0:
            return
        if spec[1]:
            words[0] = words[0].capitalize()
        if spec[2]:
            words = [words[0]] + [w.capitalize() for w in words[1:]]
        Text(spec[3].join(words)).execute()


keystroke = RuleRef(rule=(rules))
sequence = Repetition(
                      Alternative([keystroke, ]),
                      min=1,
                      max=16,
                      name="sequence"
           )

grammar.add_rule(Identifiers())
grammar.add_rule(rules)
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
