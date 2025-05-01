# Final Challenge: Deduplicate and compare email lists
def clean_email_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    all_unique = set1.union(set2)
    common = set1.intersection(set2)
    unique_to_each = set1.symmetric_difference(set2)

    print("All unique emails:", all_unique)
    print("Emails in both lists:", common)
    print("Emails unique to each list:", unique_to_each)

email_list1 = ['a@example.com', 'b@example.com', 'a@example.com']
email_list2 = ['b@example.com', 'c@example.com', 'd@example.com']

clean_email_lists(email_list1, email_list2)
