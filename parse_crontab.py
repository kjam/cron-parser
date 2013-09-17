from subprocess import call, check_output
from sys import argv


def usage():
    print """
        1. your crontab must be formatted with sections of the cron delineated
           for different projects. For an example of how to organize your
           crontab, see crontab_example.txt.
        2. create a file that has the list of crons you'd like to replace for
           a project and put it in a file. For an example of this file,
           see crontab_new_example.txt.
        3. run python parse_crontab.py /full/path/new-cron-file.txt proj_name
           and viola! your crontab is updated.
    """


def get_crontab():
    cron = check_output(['crontab', '-l'])
    f = open('/tmp/cron.txt', 'wb')
    f.write(cron)
    f.close()
    return get_file('/tmp/cron.txt')


def get_file(file_name):
    f = open(file_name, 'rb')
    return f.readlines()


def write_crontab(lines):
    f = open('/tmp/cron.txt', 'wb')
    for l in lines:
        f.write(l)
    f.close()
    call(['crontab', '/tmp/cron.txt'])


def rewrite_cron(lines, section_name, new_cron_lines):
    start, end, inserted = False, False, False
    new_list = []
    for l in lines:
        if not start and section_name in l:
            start = True
            new_list.append(l)
        elif start and section_name in l:
            end = True
        if start and not end:
            if not inserted:
                new_list.extend(new_cron_lines)
                inserted = True
            continue
        new_list.append(l)
    return new_list


def main(file_name, section):
    new_lines = get_file(file_name)
    old_cron = get_crontab()
    cron_list = rewrite_cron(old_cron, section, new_lines)
    write_crontab(cron_list)

if __name__ == '__main__':
    if not argv or '--help' in argv or len(argv) < 3:
        usage()
    else:
        main(argv[1], argv[2])
