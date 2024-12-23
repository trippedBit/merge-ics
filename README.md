# merge-ics
merge-ics simply merges two ics files into one by comparing the events in both files. Events available in source but missing in target will be merged into target.<br>
There is only one check which might block the merge: timezones.<br>
Tested and seems to work properly when merging new events (events in the future) into an existing calendar.<br>
Not tested with past events or the same event with different settings in both calendars but expectation is that the events differ due to different settings and therefore both will appear in the merged calendar.
## Command line arguments
Argument|Example|Description
|--|--|--|
--source|--source "C:\new_calendar.ics"|Calendar to merge into an existing one.
--target|--target "C:\existing_calendar.ics"|Calendar to merge source into.
## License
Please see [LICENSE](LICENSE).