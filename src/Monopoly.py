from src.ui.console import InterfaceConsole


def main():
    """
    choix de l'ui (console par défaut)\n
    lancement du jeu
    """
    console = InterfaceConsole()
    console.lance_partie()


main()