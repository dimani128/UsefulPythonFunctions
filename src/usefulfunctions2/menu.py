
try:
    from multipledispatch import dispatch
    @dispatch(list)
    def menu(options:list):
        return menu('', tuple(options))

    @dispatch(tuple)
    def menu(options:tuple):
        return menu('', options)

    @dispatch(str, list)
    def menu(title: str, options:list):
        return menu(title, tuple(options))

    @dispatch(str, tuple)
    def menu(title: str, options:tuple):
        try:
            from kiwi_menu import Menu
        except ModuleNotFoundError:
            raise Exception("kiwi_menu not installed. please install kiwi_menu")
        
        menu = Menu(
            title,
            options
        )

        return menu.show_menu()
except ModuleNotFoundError:
    print("multipledispatch not installed. please install multipledispatch to enable more features")
    
    def menu(title: str, options:tuple):
        try:
            from kiwi_menu import Menu
        except ModuleNotFoundError:
            raise Exception("kiwi_menu not installed. please install kiwi_menu")
        
        menu = Menu(
            title,
            options
        )

        return menu.show_menu()