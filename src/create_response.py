import sys


def root_dir():
    return "HTTP/1.1 200 OK\r\n\r\n"


def echo(path):
    data = path.split("/")[-1]
    return f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(data)}\r\n\r\n{data}"


def user_agent(request):
    for line in request.get_headers():
        if line.startswith("User-Agent:"):
            data = line.split(": ")[1]
    return f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(data)}\r\n\r\n{data}"


def get_files(data):
    try:
        with open(data, "r") as file:
            file_contents = file.read()
        return f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(file_contents)}\r\n\r\n{file_contents}"
    except Exception as e:
        print(f"Error: {e}")
        return "HTTP/1.1 404 Not Found\r\n\r\n"


def post_files(request, data):
    try:
        with open(data, "w") as file:
            file.write(request.body)
        return f"HTTP/1.1 201 Created\r\n\r\n"
    except Exception as e:
        print(f"Error: {e}")


def create_response(request):
    # Get the path of the request
    path = request.get_status().split()[1]

    # Match the path with its case and return the appropriate response
    match path:
        case "/":
            response = root_dir()
        case path if path.startswith("/echo/"):
            response = echo(path)
        case "/user-agent":
            response = user_agent(request)
        case path if path.startswith("/files"):
            directory = sys.argv[-1]
            filename = path.split("/")[-1]
            data = f"{directory}{filename}"

            if request.get_status().startswith("GET"):
                response = get_files(data)
            elif request.get_status().startswith("POST"):
                response = post_files(request, data)
        case _:
            response = "HTTP/1.1 404 Not Found\r\n\r\n"
    return response
