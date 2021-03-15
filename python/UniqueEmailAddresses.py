## Notes
# - dots before "@"

## Edge-cases:
# - Are there any other characters that I should consider? 
# - Should I be considering empty strings? (current will fail)
# - Should I consider missing "@" symbols? (current will fail)
# - Multiple "+"? In this case I would append only the first element

## Approach:
# - 1) Split the email address into local and domain names (TUPLE)
# - 2) Clean each domain name and add back to full string in a set (SET)
# - 3) Update the full string to the set

## Time Complexity and Memory
# O(n): Only run through the for loop once
# Memory: Potentially O(n) since every email could be a unique one

## My solution beats 87%

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        # Create empty set to store unique emails
        unique_emails = set()
        
        # Iterate through emails
        for email in emails:
            
            local, domain = email.split('@') # assumption is that there will be an @ symbol
            
            # clean local
            local = local.split("+")[0].replace('.','')

            # join full string and update set
            unique_emails.update([local+'@'+domain])
            
        return len(unique_emails)
