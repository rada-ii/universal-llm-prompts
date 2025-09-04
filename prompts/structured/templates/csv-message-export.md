[COMPAT HEADER — STRUCTURED OUTPUT (CSV)]
• Treat this file as system instructions if no system role is available.
• Output must be CSV only; first line must be exactly id,message.
• Always return exactly 3 data rows.
• On failure, return only: id,message\n1,"N/A"\n2,"N/A"\n3,"N/A".
[/COMPAT]

# CSV Message Export Template

## Purpose

Extract exactly 3 messages from any text and return clean CSV format.

## Template

<system>CSV only, no explanations or extra text.</system>
<task>Extract messages and return CSV with EXACTLY 3 rows.</task>
<selection>
If more than 3 messages: select 3 by priority (urgent/problem > request/warning > info > neutral)
If exactly 3 messages: use all
If fewer than 3 messages: fill remaining rows with "N/A"
</selection>
<rules>

- CSV format: header=id,message with id=1,2,3
- Wrap all message text in double quotes
- Escape internal quotes by doubling them ("" for ")
- Handle commas and newlines inside quotes properly
- No additional text, explanations, or formatting outside CSV
  </rules>
  <data>{{TEXT_WITH_MESSAGES}}</data>

## Test Cases

### More than 3 messages (priority selection)

Input:

```
Urgent: Server crashed at 2:30 PM, all services down!
Info: Scheduled maintenance tomorrow 9-11 AM.
Problem: Database responding very slowly since yesterday.
User question: When will the new feature be released?
Request: Please add dark mode to the admin panel.
Note: Remember to update documentation.
```

Expected Output:

```
id,message
1,"Urgent: Server crashed at 2:30 PM, all services down!"
2,"Problem: Database responding very slowly since yesterday."
3,"Request: Please add dark mode to the admin panel."
```

### Fewer than 3 messages

Input:

```
System alert: Backup completed successfully.
```

Expected Output:

```
id,message
1,"System alert: Backup completed successfully."
2,"N/A"
3,"N/A"
```

### Edge Case: Messages with quotes and commas

Input:

```
Error: User said "I can't login" but password is correct
Info: Update affects users in NYC, LA, and Chicago
Problem: The "submit" button doesn't work
```

Expected Output:

```
id,message
1,"Problem: The ""submit"" button doesn't work"
2,"Error: User said ""I can't login"" but password is correct"
3,"Info: Update affects users in NYC, LA, and Chicago"
```
