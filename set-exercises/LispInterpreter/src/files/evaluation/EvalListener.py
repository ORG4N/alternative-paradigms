
from ..LispListener import LispListener

class EvalListener(LispListener):

    def enterEveryRule(self, ctx):
        print("Enter:", type(ctx).__name__ , ctx.getText())

    def exitEveryRule(self, ctx):
        print("Exit:", type(ctx).__name__ , ctx.getText())