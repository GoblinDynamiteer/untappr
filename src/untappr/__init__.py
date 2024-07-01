from untappr.settings import Settings
from untappr.checkins import CheckIns


def main():
    _settings = Settings.create_from_args()
    check_ins = CheckIns.from_file(_settings.file_path)
    print(check_ins)
    for utah_checkin in check_ins.filter("Utah DIPA"):
        print(utah_checkin)


if __name__ == "__main__":
    main()
