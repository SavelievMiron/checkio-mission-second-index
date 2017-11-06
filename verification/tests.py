"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["sims", "s"],
            "answer": 3
        },
        {
            "input": ["find the river", "e"],
            "answer": 12
        },
        {
            "input": ["hi", " "],
            "answer": None,
            "explanation": "No space in the given line."
        },
        {
            "input": ["hi mayor", " "],
            "answer": None,
            "explanation": "Only one space in a give line, we looking for the second one"
        },
        {
            "input": ["hi mr Mayor", " "],
            "answer": 5
        }
    ],
    "Extra": [
        {
            "input": ["hi", "i"],
            "answer": None,
        },
        {
            "input": ["abc", "d"],
            "answer": None
        },
        {
            "input": ["see you", "e"],
            "answer": 2
        }
    ]
}
