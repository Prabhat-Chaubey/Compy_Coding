cleaned_string = ""

        for c in s:
            # Check if the character is alphanumeric
            if c.isalnum():
                # Convert to lowercase and add to cleaned string
                cleaned_string += c.lower()


# the isalnum() checks if the character i have is alphanumeric or not , if not then it wont add and if it is then it would add
# the one liner for this is
clearedstring=''.join(c.lower() for c in s if c.isalnum())
