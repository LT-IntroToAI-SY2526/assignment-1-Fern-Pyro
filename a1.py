# Assignment 1: AI-Generated Python Problems
# Name: [Your Name Here]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
"I am a high school student with a background in java programming, but have no prior experience with python. Create a problem set of 5-7 questions that cover the basics of python a beginner needs to know. Assume knowledge of programming concepts, but not how concepts are applied to python."

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: Conditionals
 Write a Python function grade_level(age) that returns:
    "Elementary" if age < 11,
    "Middle" if 11 <= age < 14,
    "High School" if 14 <= age < 18,
    "College" otherwise.
"""
def grade_level(age: int): #-> str :
    if age < 11:
        return("Elementary")
    elif 11<= age < 14:
        return("Middle") 
    elif 14<= age < 18:
        return("High School")
    else:
        return ("College")

"""
🧪 Test Cases:
 grade_level(10) → "Elementary"
 grade_level(13) → "Middle"
 grade_level(17) → "High School"
 grade_level(19) → "College"
"""











# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
assert grade_level(10) == "Elementary", "grade_level of 10 failed"
assert grade_level(13) == "Middle", "grade_level of 13 failed"
assert grade_level(17) == "High School", "grade_level of 17 failed"
assert grade_level(19) == "College", "grade_level of 19 failed"

print("\nTesting Problem 2:")
# Add your tests here

print("\nTesting Problem 3:")
# Add your tests here

print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here


