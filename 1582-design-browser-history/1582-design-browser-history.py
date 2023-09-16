class HistoryNode:
    url: str
    prev = None
    next = None

    def __init__(self, url):
        self.url = url

class BrowserHistory:
    head = None
    cur = None

    def __init__(self, homepage: str):
        node = HistoryNode(homepage)
        self.head = node
        self.cur = node


    def visit(self, url: str) -> None:
        node = HistoryNode(url)
        node.prev = self.cur
        self.cur.next = node
        self.cur = node


    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.cur.prev != None:
                self.cur = self.cur.prev
        return self.cur.url


    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.cur.next != None:
                self.cur = self.cur.next
        return self.cur.url 
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)