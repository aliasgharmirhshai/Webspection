import sys

# Get Target Url
def get_target(command_range, url_range):
    try:
        if sys.argv[command_range] == '--host':
            host = sys.argv[url_range]
        else:
            print('Command Not Found\n')
    except IndexError:
        print('Pleases Enter url')

    return host