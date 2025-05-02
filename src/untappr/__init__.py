from untappr.settings import Settings
from untappr.checkins import CheckIns


def run_gui(check_ins: CheckIns):
    from untappr.gui import Gui

    Gui().run()

def main():
    _settings = Settings.create_from_args()
    check_ins = CheckIns.from_file(_settings.file_path)

    if _settings.use_gui:
        run_gui(check_ins)
        return


    if not _settings.search_filter:
        for check_in in check_ins:
            print(check_in)
    else:
        for check_in in check_ins.filter(_settings.search_filter):
            print(check_in)


if __name__ == "__main__":
    main()
