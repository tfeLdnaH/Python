'''tuna = int(input("What´s your favorite number?\n"))
print(tuna)'''
while True:
    try:
        number = int(input("Whats ur fav. number?\n"))
        print(18/number)
        break
    except ValueError:
        print("Make sure and enter a number")
    except ZeroDivisionError:
        print("Dont pick zero")
    except:
        break
    finally:
        print("loop complety")