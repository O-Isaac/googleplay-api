import argparse
from gpapi.googleplay import GooglePlayAPI

def main():
   parser = argparse.ArgumentParser(description='Fate Grand Order Downloader APK')
   parser.add_argument('-r', '--region', help='Game server region')
   parser.add_argument('-t', '--type', help='64 or 32 Bits')
   parser.add_argument('-e', '--email', help='email pass')
   parser.add_argument('-p', '--password', help='app password')

   args = parser.parse_args()
   region = args.region
   type = args.type
   password = args.password
   email = args.email
   
   if type == "64":
      codename = "cloudbook"
      arch="arm64-v8a"
   else:
      codename = "cwv88s"
      arch="armeabi-v7a"
       

   if region == "JP":
      packageName = "com.aniplex.fategrandorder"
   else:
      packageName = "com.aniplex.fategrandorder.en"

   print("[+] Setting up configs")
   server = GooglePlayAPI(locale="en_US", timezone="UTC", device_codename=codename)

   print("[+] Logging in...")
   server.login(email=email, password=password)

   print(f"[+] Downloading {packageName} - {arch}")
   fl = server.download(packageName)

   with open(f"{packageName}.{arch}" + ".apk", "wb") as apk_file:
      for chunk in fl.get("file").get("data"):
         apk_file.write(chunk)
   
   print("[+] Download successful!")


if __name__ == '__main__':
    main()