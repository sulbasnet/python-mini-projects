import pyshorteners

def shorten_url(long_url):
    try:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(long_url)
        return short_url
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Python URL Shortener")
    print("-" * 30)

    long_url = input("Enter the URL to shorten: ").strip()

    if not long_url.startswith("http"):
        print("Please enter a valid URL (starting with http or https)")
        return

    short_url = shorten_url(long_url)
    print(f"\nShortened URL:\n{short_url}")

if __name__ == "__main__":
    main()
