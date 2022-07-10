class MenuDesign:

    @staticmethod
    def made_terminal_component(component_name: str, width: int = 120, fill_char: str = "-") -> None:
        print(f" {component_name.upper()} ".center(width, fill_char))