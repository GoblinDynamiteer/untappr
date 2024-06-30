from untappr.settings import Settings


def main():
    _settings = Settings.create_from_args()
    print(_settings.file_path)


if __name__ == "__main__":
    main()
