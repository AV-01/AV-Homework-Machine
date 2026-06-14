import requests

url = "http://192.168.12.242/upload-file?folder=testjune"

gcode_content = open("test.txt", "r").read()


# gcode_content = "hello world testing\n"*5000

files = {
    'file' : ("longtest2.gcode" , gcode_content , 'text/plain')
}

print(f"Uploading file to {url}...")

try:
    response = requests.post(url, files = files)
    print("status code: ", response.status_code)
    print("server response:", response.text)
except Exception as e:
    print("failed to connect or upload:", e)