
from funcs import menu

match menu("Choose a menu", ['Hi', 'hello', 'tuples']):
    case 0:
        print(menu("Hello", ['Hi', 'Hello', 'Bye', 'GO AWAY I DON\'T WANT TO TALK TO YOU']))
    case 1:
        print(menu(['This has no title', 'Pretty cool right?']))
    case 2:
        print(menu('This has tuples', ('stuff', 'reasons', 'i dont have any ideas for cool other options')))