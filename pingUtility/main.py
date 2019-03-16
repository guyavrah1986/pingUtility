import pingUtility.pinger


def main():
    print("main - start")
    ipAddress = "10.100.102.8"
    runPing(ipAddress)

    print("main - end")


if __name__ == "__main__":
    main()