class BrowserHistory:
    history = []
    curi = 0
    lasti = 0

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curi = 0
        self.lasti = 0
        

    def visit(self, url: str) -> None:
        if self.curi == len(self.history)-1:
            self.history.append(url)
        else:
            self.history[self.curi+1] = url
        self.curi += 1
        self.lasti = self.curi


    def back(self, steps: int) -> str:
        self.curi = max(0, self.curi-steps)
        return self.history[self.curi]


    def forward(self, steps: int) -> str:
        self.curi = min(self.lasti, self.curi+steps)
        return self.history[self.curi]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)