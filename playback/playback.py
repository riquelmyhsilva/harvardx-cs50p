def main():
    speak = playback(str(input("--> ")))

    print(speak)

def playback(speaking):
    return speaking.replace(" ","...")

main()
