# Project 1: Case Converter

**CS 101 | Winter 26 | Professor Duran**

## **Goals**

* Understanding Data Types and Type Checking
* Writing Functions with Parameters and Return Values
* Boolean Logic and Control Flow
* Unit Testing
* ASCII Arithmetic

---

## **Assignment Description**

Your task is to write a function called `convert_case` that accepts two arguments: a single character and a command string indicating the desired case.

Your goal is to convert the letter to the desired case based on the command.

* If the character is already in the desired case, return it unchanged.
* If the character is a non-letter (like punctuation or numbers), return it unchanged.

### **Constraints (Important!)**

* **NO Built-in String Methods:** You are **not** allowed to use methods like `.upper()`, `.lower()`, `.swapcase()`, or `.islower()`.
* **Hard Coded Logic:** You must manually check the ASCII values to determine casing.
* **ASCII Arithmetic:** You must use the `ord()` and `chr()` functions to perform the conversion mathematically.

---

## **The ASCII Table**

You will need to use the integer values of characters to determine if a letter is uppercase or lowercase.

| Character Type | Range (Letter) | Range (Decimal) |
| --- | --- | --- |
| **Uppercase** | 'A' to 'Z' | 65 to 90 |
| **Lowercase** | 'a' to 'z' | 97 to 122 |

**The Magic Number:** The difference between an uppercase letter and its lowercase equivalent is **32**.

* `'A'` (65) + 32 = `'a'` (97)
* `'a'` (97) - 32 = `'A'` (65)



### **Parameters**

1. **`character`**: A string containing a single letter: `"A"`, `"b"`, `"C"`.
2. **`target_case`**: A string representing the command. You must support the following exact command variations:
* For Lowercase: `"lower"`, `"LOWER"`, `"Lower"`
* For Uppercase: `"upper"`, `"UPPER"`, `"Upper"`



### **Error Handling**

If either `character` or `target_case` is **not a string**, your function must raise a `ValueError`.

---

## **Implementation Guide**

1. **Validate Input:** Check if the inputs are strings. If not, raise the error.
2. **Identify Target:** Check if `target_case` is asking for "upper" or "lower" (remember to check all 3 variations for each using `or`).
3. **Check ASCII:** Use `ord(character)` to get the number.
4. **Transform:**
* If the target is **Upper** and the number is between **97 and 122**, subtract 32 and convert back with `chr()`.
* If the target is **Lower** and the number is between **65 and 90**, add 32 and convert back with `chr()`.
* Otherwise, return the character as is.



---

## **Testing Requirements**

You must write a separate test file using `unittest`. You are required to implement **5 specific tests**:

1. **Upper to Lower:** Pass an uppercase letter and a "lower" command. Expect a lowercase letter.
2. **Lower to Upper:** Pass a lowercase letter and an "upper" command. Expect an uppercase letter.
3. **Upper to Upper:** Pass an uppercase letter and an "upper" command. Expect no change.
4. **Lower to Lower:** Pass a lowercase letter and a "lower" command. Expect no change.
5. **Non-Letter:** Pass a symbol (e.g., `!`, `?`, `1`) and any command. Expect no change.

**Check:** Ensure your function raises a `ValueError` if you pass an integer (e.g., `100`) instead of a string.

---

## **Submission**

Submit your Python file containing the function and your `unittest` file to github by the due date.