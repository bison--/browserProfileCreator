import shutil


class Helper:

    @staticmethod
    def prompt_user(options, prompt_message):
        """
        Prompt the user to select from a list of options.
        """

        for index, key in enumerate(options, start=1):
            print(f"{index}. {key}")

        while True:
            choice = input(prompt_message)
            try:
                index = int(choice)
                if 1 <= index <= len(options):
                    return options[index - 1]

            except ValueError:
                pass

            print("Invalid selection, please choose a number from the list.")

    @staticmethod
    def detect_browsers():
        """
        Detect installed Chrome- or Firefox-based browsers.

        Returns:
            dict: Mapping of browser type to executable path.
        """
        candidates = {
            "chrome": ["google-chrome", "chromium", "chromium-browser"],
            "firefox": ["firefox"]
        }

        found = {}
        for browser_type, executables in candidates.items():
            for exe in executables:
                path = shutil.which(exe)
                if path:
                    found[browser_type] = path
                    break

        return found
