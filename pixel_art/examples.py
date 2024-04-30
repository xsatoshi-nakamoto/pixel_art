
import pixels

# test your code here
def colors():
  print(f"{pixels.BLACK}{pixels.Back.RESET} - 'black'")
  print(f"{pixels.RED}{pixels.Back.RESET} - 'red'")
  print(f"{pixels.GREEN}{pixels.Back.RESET} - 'green'")
  print(f"{pixels.YELLOW}{pixels.Back.RESET} - 'yellow'")
  print(f"{pixels.BLUE}{pixels.Back.RESET} - 'blue'")
  print(f"{pixels.MAGENTA}{pixels.Back.RESET} - 'magenta'")
  print(f"{pixels.CYAN}{pixels.Back.RESET} - 'cyan'")
  print(f"{pixels.WHITE}{pixels.Back.RESET} - 'white'")

if __name__ == '__main__':
  colors()