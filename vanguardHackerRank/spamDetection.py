# Implement a prototype of an email spam detection algorithm.

# For simulation, subjects of n emails and k spam words are given in two arrays of strings, subjects, and spam words.
# An email is considered spam if it contains at leat two spam words in the subject. If a spam word is repeated, it counts as two so the email is considered spam. The spam words are not case-sensitive.

# Given subjects and spam_words, return an array of n strings, "spam" or "not_spam", one for each subject.


def detect_spam(subjects, spam_words):
    # Convert spam words to lowercase to make comparison case-insensitive
    spam_words = [word.lower() for word in spam_words]

    # Initialize an empty list to store results
    spam_detection_results = []

    # Iterate over each subject
    for subject in subjects:
        # Convert subject to lowercase and split it into words
        subject_words = subject.lower().split()

        # Initialize counter for spam words
        spam_counter = 0

        # Iterate over each word in the subject
        for word in subject_words:
            # If the word is in the list of spam words, increment the counter
            if word in spam_words:
                spam_counter += 1

            # If there are at least two spam words, mark the email as spam and break the loop
            if spam_counter >= 2:
                spam_detection_results.append("spam")
                break

        # If the loop completed without finding two spam words, mark the email as not spam
        else:
            spam_detection_results.append("not_spam")

    # Return the list of spam detection results
    return spam_detection_results