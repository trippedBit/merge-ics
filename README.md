# merge-ics
merge-ics simply merges to ics files into one by comparing the events in both files. Events available in source but missing in target will be merged into target.<br>
There is only one check which might block the merge: timezones.
## Command line arguments
Argument|Example|Description
|--|--|--|
--source|--source "C:\new_calendar.ics"|Calendar to merge into an existing one.
--target|--target "C:\existing_calendar.ics"|Calendar to merge source into.
## License
Please see [LICENSE](LICENSE).