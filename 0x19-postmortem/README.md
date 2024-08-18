## Postmortem: Apache(server incident)

## Date: Aug 14, 2024

## Author: Katleho Lekale

## Status: Issue resolved

## Issue Summary
Duration: The outage lasted 15 minutes, starting at 07:00 am and ending at 7:15 am GMT.
Impact: The Apache server returned a 500 Error, rendering the WordPress site inaccessible. Not all users could access the website, leading to significant disruptions in service.
Root Cause: A misspelled .phpp file should have been spelled .php caused the Apache server to fail to process the needed configuration file, resulting in the error.
## Timeline
* 07:00 AM: The issue was detected through a monitoring alert indicating a spike in 500 Internal Server Errors on the website.
* 07:01 AM: I verified the issue by attempting to access the website and received a 500 Internal Server Error.
* 07:03 AM: Initial investigation began with checking Apache logs, revealing generic error messages without specific causes.
* 07:05 AM: Strace was attached to the Apache process to trace system calls and signals, revealing the missing locale WP.phpp file.
* 07:07 AM: Misleading debugging paths included checking the settings files and file permissions, which were found to be correct.
* 07:09 AM: The misspelled php file was identified as the root cause.
* 07:11 AM: The spelling of the file was corrected, and Apache was restarted.
* 07:13 AM: The website was confirmed to be fully operational, and monitoring alerts were cleared.
* 07:15 AM: The incident was resolved, and a post-incident review meeting was scheduled.
## Root Cause and Resolution
* Root Cause: The cause of the outage was a spelling error in the `wp-settings.php` file, where the symbolic link filename was incorrectly referenced as `locale-wp.phpp`. The correct file, `locale-wp.php`, existed in the `/var/www/html/locale/` directory, however, since there was a spelling error/typo, Apache could not load the necessary configuration, resulting in a 500 Internal Server Error.
* Resolution: The typo was corrected in the `wp-settings.php` file, changing the reference from `locale-wp.phpp` to `locale-wp.php`. A Puppet manifest was created and deployed across all servers to ensure the fix was applied consistently. Apache was restarted, and the website was brought back online.
* Corrective and Preventative Measures
* Improvements:
1. Code Review Process: Implement a stricter code review process to catch typographical errors before deployment.
2. Automated Syntax Checks: Introduce and implement syntax and link checks for configuration files to prevent similar issues.
3. Documentation: Update deployment documentation to include verification steps for symbolic links and configuration files.
