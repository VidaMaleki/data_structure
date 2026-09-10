import requests
from html.parser import HTMLParser

class GoogleDocParser(HTMLParser):
  def __init__(self):
    super().__init__()
    self.rows = []
    self._current_row = []
    self._current_cell = []
    self._in_cell = False

  def handle_starttag(self, tag, attrs):
    if tag == "tr":
      self._current_row = []
    elif tag == "td":
      self._in_cell = True
      self._current_cell = []

  def handle_endtag(self, tag):
    if tag == "td":
      self._current_row.append("".join(self._current_cell).strip())
      self._in_cell = False
    elif tag == "tr":
      if self._current_row:
        self.rows.append(self._current_row)

  def handle_data(self, data):
    if self._in_cell:
      self._current_cell.append(data)


def print_secret_message(doc_url):
  response = requests.get(doc_url)  # fixed: requests not request
  response.raise_for_status()

  parser = GoogleDocParser()
  parser.feed(response.text)

  rows = parser.rows
  if rows and rows[0][:3] == ["x-coordinate", "Character", "y-coordinate"]:
    rows = rows[1:]

  grid = {}
  max_x = 0
  max_y = 0

  for row in rows:
    if len(row) < 3:
      continue
    x = int(row[0])
    char = row[1]
    y = int(row[2])
    grid[(x, y)] = char
    max_x = max(max_x, x)
    max_y = max(max_y, y)

  for y in range(max_y, -1, -1):
    line = "".join(grid.get((x, y), " ") for x in range(max_x + 1))
    print(line)

print_secret_message("https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub")