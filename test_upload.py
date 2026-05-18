import requests

url = "http://192.168.12.242/" + "upload-file"

payload = {
    "file" : "TEST-FILE-3.gcode",
    "folder" : "",
    "content": "Testing, hello world\nmultiline test\nline 3\nCREATED MAY 17 8:01 PM"
}

response = requests.post(url, data=payload)
print(response.status_code)
print(response.text)