class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = {}
        def uniqueFinder(email):
            # add the unique email to the dict
            local, domain = email.split("@")
            local = local.split('+')[0]
            local = local.replace(".", "")
                        
            newEmail = local + "@" + domain
            unique[newEmail] = unique.get(newEmail, 0) + 1
            
        # call uniqueFinder on every email in emails
        for email in emails:
            uniqueFinder(email)
        print(unique)
        return len(unique.keys())