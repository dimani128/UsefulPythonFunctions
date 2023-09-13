
def cls():
    """Clears the screen. From https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console"""
    import os
    os.system('cls' if os.name=='nt' else 'clear')