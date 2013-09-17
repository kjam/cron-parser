Cron parser 
=======================

Easy python script that allows you to change pieces of a crontab for different projects based on having a crontab that delineates different sections on a project-by-project basis.


Using cron_parser
-------------------

1. your crontab must be formatted with sections of the cron delineated to different projects. For an example of how to organize your crontab, see crontab_example.txt.
2. create a file that has the list of crons you'd like to replace for a project and put it in a file. For an example of this file, see crontab_new_example.txt.
3. run python parse_crontab.py new-file-with-crons.txt project_name and viola! your crontab is updated.


Questions?
----------

@kjam on freenode / @katharine on hipchat

