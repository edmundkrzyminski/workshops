---
layout: default
title: Common Questions
workshop: JavaScript Basics
section: Instructor Notes
---

# JavaScript Basics Common Questions

Keep answers simple first. Add detail only if a student asks for more. \
Encourage curiosity and normalize not knowing everything.

## **"What's the difference between JavaScript and Java?"**

They're completely different languages! JavaScript was named to sound similar for marketing reasons, but they're not related. JavaScript runs in browsers and with Node.js. Java is a different language used for different things.

*If they want more*: Java is compiled and runs in a "Java Virtual Machine." JavaScript is interpreted and runs in browsers or Node.js. They have different syntax and purposes.

## **"Why do we use Node.js instead of a browser?"**

Great question! JavaScript was made for browsers, but Node.js lets us run it anywhere - in the terminal, on servers, in robots. We're using Node because it's simpler to start with terminal output before we add HTML next workshop.

*If they want more*: Node.js uses the same JavaScript engine as Chrome (V8) but without the browser parts. It's great for learning basics without distraction.

## **"When do I use let vs const?"**

`const` is for values that never change (like a character's name in a story). `let` is for values that might change (like a score that goes up). When in doubt, start with `const` - if you need to change it later, JavaScript will tell you to use `let` instead!

*If they want more*: `const` stands for "constant" - unchanging. This helps prevent bugs. There's also `var` (older way) but we use `let` and `const` now.

## **"Why are my quotes different colors in VS Code?"**

That's syntax highlighting - the editor is helping you see different parts of your code! Strings are usually one color, variables another. It helps spot mistakes.

*If they want more*: VS Code recognizes JavaScript syntax and colors it to help you read code. If colors look wrong, it might mean there's a missing quote or bracket.

## **"What does 'undefined' mean?"**

Your variable exists but doesn't have a value yet. Like a labeled box with nothing inside. Make sure you assign a value: `let name = "Sam";` not just `let name;`.

*If they want more*: In JavaScript, undefined is a special value meaning "no value assigned yet." It's different from null (intentionally empty) or an empty string `""`.

## **"Why does console.log sometimes show [object Object]?"**

You're trying to concatenate something that isn't a string or number. For now, make sure you're using strings, numbers, or booleans. We'll learn about objects in future workshops!

*If they want more*: Objects are collections of related data. When you try to concatenate an object, JavaScript can't convert it to a readable string automatically.

## **"Do I need semicolons?"**

JavaScript is flexible - semicolons are optional but recommended. They mark the end of a statement. Using them is good practice and prevents rare bugs.

*If they want more*: JavaScript has "automatic semicolon insertion" which adds them for you. But it's best to be explicit.

## **"Can I use single quotes or double quotes?"**

Either works! `"Hello"` and `'Hello'` are the same. Pick one style and be consistent. Most JavaScript developers use double quotes for strings.

*If they want more*: Use single quotes if your string contains double quotes: `'She said "hello"'`. Or use template literals (backticks) for complex strings.

## **"What's the difference between '5' and 5?"**

`"5"` (with quotes) is a string - text that happens to be a number character. `5` (no quotes) is a number you can do math with. `"5" + "5"` makes `"55"`, but `5 + 5` makes `10`.

*If they want more*: This is called "type coercion." JavaScript tries to be helpful but it can cause bugs. Always use the right type for what you need!

## **"How do I fix 'node: command not found'?"**

Node.js isn't installed or isn't in your PATH. Run the setup guide or verify installation with an instructor. This needs to be fixed before you can continue.

*If they want more*: PATH is an environment variable that tells your computer where to find programs. Node.js needs to be added to PATH during installation.

## **"Why do I get 'SyntaxError: Unexpected string'?"**

Usually a missing quote or plus sign. Check that:
- All strings have matching quotes at both ends
- Concatenations have `+` between parts
- Each statement is complete

Read the error carefully - it tells you the line number!

*If they want more*: Syntax errors mean JavaScript can't understand your code. The error message usually points to where it got confused.

## **"Can I make programs that ask questions?"**

Yes! But input handling in the terminal requires different techniques which we're saving for later. For now, we're focusing on output and variables. Next workshop, you'll handle user input in the browser!

*If they want more*: Node.js can use `readline` or `prompt` libraries for input. Browsers can use `prompt()` or form inputs. We'll learn those soon!

## **"Why doesn't my code work after I changed it?"**

Did you save the file? Did you run it again with `node story.js`? Common troubleshooting:
1. Save the file (Ctrl+S / Cmd+S)
2. Make sure terminal is in the right folder
3. Re-run the command
4. Read any error messages!

*If they want more*: Node.js runs the saved version of your file, not what's on screen. Always save before running!

## **"What if I want spaces in my variable name?"**

You can't have spaces in variable names! Use camelCase instead: `myVariableName`. Or underscores: `my_variable_name`. But camelCase is the JavaScript convention.

*If they want more*: JavaScript sees spaces as separators between different parts of code. camelCase keeps readability without spaces.

## **"Can I name a variable anything?"**

Almost! Can't use reserved words (like `let`, `const`, `if`, `function`). Must start with a letter, $, or underscore. No spaces or most special characters. Be descriptive!

*If they want more*: JavaScript has about 60 reserved keywords. VS Code will highlight them differently to warn you.

## **"Why do I see ` and ${} in some code?"**

Those are template literals (backticks). They're an alternative to concatenation:
```javascript
let name = "Alex";
// Old way:
console.log("Hello " + name);
// New way:
console.log(`Hello ${name}`);
```

Both work! We're teaching + first because it's simpler to start.

*If they want more*: Template literals can span multiple lines and make complex strings easier to read.

## Teaching Notes for Instructors

**Keep the tone curious and encouraging**. When a student asks "Can I...?" the answer is almost always "Yes! Let's figure out how" even if it's beyond today's scope.

**Read error messages together**. Don't just fix it - show them how to interpret what JavaScript is telling them.

**"I don't know, let's try it!"** is a great response. Experimentation builds confidence.

**Normalize not knowing everything**. "That's a great question - I had to look that up myself recently!"
