import instaloader
profile=input("Enter profile name")
print("Download media")
instaloader.Instaloader().download_profile(profile,profile_pic_only=False)
print("download completed")