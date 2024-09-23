from Gen.chaloosOotaghListener import chaloosOotaghListener
from Gen.chaloosOotaghParser import chaloosOotaghParser


class MyListener(chaloosOotaghListener):
    def __init__(self):
        self.depth = 0
        self.max_depth = 0

    # Exit a parse tree produced by mygrammarParser#prog.
    def exitProg(self, ctx: chaloosOotaghParser.ProgContext):
        ctx.depth = ctx.declaration()
        print(self.max_depth)

    # Enter a parse tree produced by mygrammarParser#ifst.
    def enterIfst(self, ctx: chaloosOotaghParser.IfstContext):
        self.depth += 1
        if self.depth > self.max_depth:
            self.max_depth = self.depth

    # Exit a parse tree produced by mygrammarParser#ifst.
    def exitIfst(self, ctx: chaloosOotaghParser.IfstContext):
        self.depth -= 1

    # Enter a parse tree produced by mygrammarParser#whilest.
    def enterWhilest(self, ctx: chaloosOotaghParser.WhilestContext):
        self.depth += 1
        if self.depth > self.max_depth:
            self.max_depth = self.depth

    # Exit a parse tree produced by mygrammarParser#whilest.
    def exitWhilest(self, ctx: chaloosOotaghParser.WhilestContext):
        self.depth -= 1
