import httpx
import argparse
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import JsonLexer

parser = argparse.ArgumentParser(
    prog="Test client for Fastapi app",
    description="This simple https client is used to test this Fastapi app",
)

parser.add_argument("--request-method", type=str)
parser.add_argument("action", type=str)
parser.add_argument("--parameter", type=str)

args = parser.parse_args()

url: str = "http://localhost:8000/"
url += args.action

if args.parameter is not None:
    url += f"/{args.parameter}"

if args.request_method == "get" or args.request_method is None:
    response: httpx.Response = httpx.get(url)
elif args.request_method == "post":
    response: httpx.Response = httpx.post(url)

print(highlight(response.text, JsonLexer(), TerminalFormatter()))
