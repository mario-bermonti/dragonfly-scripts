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
                       Repetition, Playback)

context = AppContext(title="emacs")
grammar = Grammar("emacs", context=context)

rules = MappingRule(
    name = "emacs",
    mapping = {
        # general commands for buffers, windows, etc.
        "open file": Key("escape, c-x, c-f"),
        "save file": Key("escape, c-x, c-s"),
        "save as": Key("escape, c-x, c-w"),
        "close file": Key("escape, g, k, enter"),
        "close all": Key("escape, colon, q, a, l, l, enter"),
        "hard close": Key("escape, colon, q, exclamation, enter"),
        "close buffer": Key("c-x, 0"),
        "command [<text>]": Key("escape, colon") + Text("%(text)s"),
        "split view": Key("escape, colon") + Text("split") + Key("enter"),
        "vertical split": Key("escape, colon") + Text("vsplit") + Key("enter"),
        "new split": Key("escape, colon") + Text("new") + Key("enter"),
        "new vertical": Key("escape, colon") + Text("vnew") + Key("enter"),
        "next buffer": Key("escape, c-x, o"),
        "search [<text>]": Key("c-s") + Text("%(text)s"),
        "search before": Key("c-r"),
        "next found": Key("c-s"),
        "find [<text>]": Key("f") + Text("%(text)s"),
        "find back [<text>]": Key("F") + Text("%(text)s"),
        "until [<text>]": Key("d, t") + Text("%(text)s"),
        "oops": Key("c-g"),
        "only buffer": Key("c-x, 1"),
        "exit emacs": Key("c-x, c-c"),
        "go to buffer": Key("c-x, b"),
        "run file": Key("c-c, c-c") + Key("enter") + Text("y") + Key("c-c, c-z"),
        "go to python": Key("c-c, c-z"),

        # programming constructs
        "new class": Key("c-c, c-t, c"),
        "new function": Key("c-c, c-t, d"),
        "new conditional": Key("c-c, c-t, i"),
        "new elif": Key("escape") + Key("i") + Text("elif :") + Key("left"),
        "new else": Key("i") + Text("else:") + Key("escape, o"),
        "new while loop": Key("c-c, c-t, w"),
        "new for loop": Key("c-c, c-t, f"),
        "new try block": Key("c-c, c-t, t"),
        "print statement": Text("print()") + Key("escape, i"),
        "pass":  Text("pass"),
        "self": Text("self."),
        "for loop": Text("for"),
        "new dictionary": Text("dict()") + Key("escape"),
        "find coordinates": Text("coords()") + Key("escape, i"),
        "define in it": Text("__init__"),
        "append": Text(".append()") + Key("escape, i"),
        "jason": Text("json"),

        # movements
        "go to last": Key("escape, dollar"),
        "go to start": Key("escape, caret"),
        "go to top": Key("escape, 1, G"),
        "go to bottom": Key("escape, G"),
        "visualline": Key("home"),
        "go up [<n>] ": Key("escape") + Text("%(n)d") + Key("k"),
        "go down [<n>]": Key("escape") + Text("%(n)d") + Key("j"),
        "scroll [<scroll_by>] down": Text("%(scroll_by)d") + Key("c-f"),
        "scroll [<scroll_by>] up": Text("%(scroll_by)d") + Key("c-b"),
        "jump [<n>]": Key("escape, w:%(n)d"),
        "jump back [<n>]": Key("escape, b:%(n)d"),
        "bow [<n>]": Key("escape, e:%(n)d"),
        "paragraph down [<n>]": Text("%(n)d") + Key("a-lbrace"),
        "paragraph up [<n>]": Text("%(n)d") + Key("a-rbrace"),
        "prior bracket [<n>]": Text("%(n)d") + Key("escape:down, c-b, escape:up"),
        "next bracket [<n>]": Text("%(n)d") + Key("escape:down, c-f, escape:up"),
        "go to line [<n>]": Key("escape") + Text("%(n)d") + Key("G"),
        "set mark": Key("c-space, c-space"),
        "go back": Key("c-u, c-space"),
        "scroll up other buffer": Key("a-pgup"),
        "scroll down other buffer": Key("a-pgdown"),

        # SPELLING AND SYMBOL
        # words
        "pie":  Text("py"),
        "yes": Text("yes"),
        "no": Text("no"),

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
        "semi": Key("escape, a") + Text(";"),
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
        "equals to": Key("equal"),
        "Ash": Key("hyphen"),
        "times [<text>]": Text("* ") + Text("%(text)s"),
        "divided by": Text("/"),
        "braces": Key("lbrace, rbrace, escape, i"),
        "brackets": Key("lbracket, rbracket, escape, i"),
        "parens": Key("lparen, rparen, escape, i"),
        "angles": Key("langle, rangle, escape, i"),
        "doubles": Key("dquote, dquote, escape, i"),
        "singles": Key("squote, squote, escape, i"),
        "exclamation": Key("exclamation"),
        "greater than": Text(" > "),
        "smaller than": Text(" < "),
        "greater or equal to": Text(" >= "),
        "smaller or equal to": Text(" <= "),
        "double equals": Text(" == "),
        "not equals": Text(" != "),
        "pound": Text("#"),
        "dot": Text("."),
        "insert doc string": Key("escape, i, dquote, dquote, escape, i") +
            Key("dquote, dquote, escape, i") +
            Key("dquote, dquote, escape, i"),

        # editing
        "insert": Key("escape, i"),
        "small insert": Key("escape, a"),
        "bic insert": Key("escape, A"),
        "insert at beginning": Key("escape, s-i"),
        "indent [<n>]": Key("escape") + Text("%(n)d") + Key("rangle, rangle"),
        "indent out [<n>]": Key("escape") + Text("%(n)d") + Key("langle, langle"),
        "change case": Key("tilde"),
        "kill line before [<n>]": Key("escape") + Text("%(n)d") + Key("k, d, d"),
        "kill line after [<n>]": Key("escape") + Text("%(n)d") + Key("j, d, d, k"),
        "kill [<n>]": Text("%(n)d") + Key("d") + Key("space"),
        "kill back [<n>]": Key("escape") + Text("%(n)d") + Key("d") + Key("h"),
        "kill [<n>] line": Key("escape") + Text("%(n)d") + Key("d, d"),
        "kill [<n>] word": Key("escape") + Text("%(n)d") + Key("d, w"),
        "kill last word [<n>]": Key("escape") + Text("%(n)d") + Key("d, b"),
        "delete line [<n>]": Key("escape") + Text("%(n)d") + Key("d, d"),
        "replace text": Key("s"),
        "open line": Key("escape, o"),
        "open line before": Key("escape, O"),
        "yank": Key("escape") + Key("y"),
        "big yank": Key("escape") + Key("Y"),
        "put previous": Key("escape") + Key("c-p"),
        "put": Key("escape") + Key("p"),
        "big put": Key("escape") + Key("P"),
        "cut": Key("c-x"),
        "duplicate line": Key("escape") + Key("Y, P"),
        "that's all": Key("escape, g, g, V, G"),
        "undo [<n>]": Text("%(n)d") + Key("c-underscore"),
        "scratch": Key("escape, u"),
        "do it again": Key("escape, c-r"),
        "again": Key("dot"),
        "autocomplete": Key("tab"),
        "remove blank": Key("escape, F, space, x"),
        "add blank": Key("escape, b, i, space, escape"),
        "add blank after": Key("escape, e, a, space, escape"),
        "remove blank after": Key("escape, f, space, x"),
        "comment out": Key("s-i") + Text("#") + Key("escape"),
        "join lines": Key("J"),
        "grab [<n>] word": Key("escape, b, v") +  Text("%(n)d") + Key("e"),
        "grab word from beginning": Key("escape, v") + Key("e"),
        "grab [<n>] lines": Key("escape, home, v") +  Text("%(n)d") + Key("j, k, end"),
        "search and replace": Key("a-percent"),

        # modes
        "escape": Key("escape"),
        "visual": Key("escape, v"),
        "bic visual": Key("escape, V"),
        "call visual": Key("escape, c-v"),

        # projectile mode
        "open in all projects": Key("escape, c, c, p, F"),
        "open in project": Key("escape, c, c, p, f"),
        "open project directory": Key("escape, c, c, p, D"),
        "catch file": Key("escape, c, c, p, z"),
        "close all project files": Key("escape, c, c, p, k"),
        "save all project files": Key(" escape,c-c, p, S"),


        # Jedi mode
        "look for definition": Key("escape, c, c, dot"),
        "look for documentation": Key("escape, c, c, question"),
        "look for function details": Key("escape, c, c, slash"),
        "jedi go back": Key("escape, c, c, comma"),
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


grammar.add_rule(Identifiers())
grammar.add_rule(rules)
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
