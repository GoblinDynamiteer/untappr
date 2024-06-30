from untappr.settings import Settings
from untappr.checkins import CheckIns


def main():
    _settings = Settings.create_from_args()
    check_ins = CheckIns.from_file(_settings.file_path)
    print(check_ins)


if __name__ == "__main__":
    main()
