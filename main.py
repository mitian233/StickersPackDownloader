import requests

ua = {'User-Agent': 'Mozilla/5.0'}
id = input("Input LINE stickers pack ID:")  # Get stickers pack id
url = ("http://dl.stickershop.line.naver.jp/products/0/0/1/" + id + "/iphone/stickers@2x.zip")  # Generate download url

ans = input("Download stickers pack on " + url + " Sure? (Y/N):")  # Confirm the download url
if ans[-1] in ['Y', 'y']:
    r = requests.get(url, headers=ua)
    print(r.request.headers)
    print(r.status_code)  # Confirm status code
    with open('stickers.zip', 'wb') as f:
        f.write(r.content)
    exit()
elif ans[-1] in ['N', 'n']:
    print("Process canceled. ")
    exit()
else:
    print("Invalid input. ")
    exit()
#End of file