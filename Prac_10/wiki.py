import wikipedia

def main():
    title = input("Enter page title: ")
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(wikipedia.summary(title, sentences=2))
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("Disambiguation error. Try one of these options:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f"Page titled '{title}' does not exist. Try another one.")
        title = input("\nEnter page title: ")

    print("Thank you.")

main()
