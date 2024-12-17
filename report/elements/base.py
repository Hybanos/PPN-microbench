from elements.bench import *

from abc import ABC, abstractmethod
import json

class AbstractElement(ABC):

    obj = None

    @abstractmethod
    def to_html(self):
        raise NotImplementedError("Abstract method call")

    @abstractmethod
    def get_index(self):
        raise NotImplementedError("Abstract method call")

class Report(AbstractElement):
    def __init__(self, json_path):
        self.json_path = json_path

        self.mapping = {
            "OPS" : Ops,
        }

        self.generate()

    def generate(self):
        with open(self.json_path, "r") as f:
            AbstractElement.obj = json.load(f)

        self.pages = [Cover(), Index(), SysInfo()]

        for bench in AbstractElement.obj["data"]:
            self.pages.append(Ops(AbstractElement.obj))

        self.pages[1].set_pages(self.pages)

    def to_html(self):
        tmp = ""
        for p in self.pages:
            tmp += f"<div>{p.to_html()}</div>"

        html = f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>PPN-microbench</title>
    </head>
    <body>
        {tmp}
    </body>
</html>
"""
        return html

    def get_index(self):
        pass

class Cover(AbstractElement):
    """cover page"""
    def to_html(self):
        html = f"""
        <h1>Haha<h1>
"""
        return html

    def get_index(self):
        return f"<li><a href='#Cover'>Cover</a></li>"

class Index(AbstractElement):
    """report index"""

    def set_pages(self, pages):
        self.pages = pages

    def to_html(self):
        tmp = ""
        for p in self.pages:
            tmp += p.get_index()
        html = f"""
<h1 id='Index'>Index</h1>
<ul>
    {tmp}
</ul>
"""
        return html

    def get_index(self):
        return f"<li><a href='#Index'>Index</a></li>"

class SysInfo(AbstractElement):
    """cpu, ram and gpu information"""
    def to_html(self):
        obj = AbstractElement.obj
        cpu_info = ""
        for key, info in obj["meta"]["cpu_info"].items():
            cpu_info += f"<tr><td>{str(key)}</td><td>{str(info)}</td></tr>"
        cpu_info = f"<table>{cpu_info}</table>"

        mem_info = ""
        for key, info in obj["meta"]["mem_info"].items():
            mem_info += f"<tr><td>{str(key)}</td><td>{str(info)}</td></tr>"
        mem_info = f"<table>{mem_info}</table>"


        return f"<h1 id='SysInfo'>System information</h1>" + cpu_info + "<br/>" + mem_info
    
    def get_index(self):
        return f"<li><a href='#SysInfo'>System information</a></li>"