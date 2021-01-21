"""
4. Write a Python function to create the HTML
string with tags around the word(s).
Sample function and result are shown below:

    add_html_tags('h1', 'My First Page')

    <h1>My First Page</h1>

    add_html_tags('p', 'This is my first page.')

    <p>This is my first page.</p>

    add_html_tags('h2', 'A secondary header.')

    <h2>A secondary header.</h2>

    add_html_tags('p', 'Some more text.')

    <p>Some more text.</p>
"""

# input from Console to have didffernt entrance for tags and contents
input1 = input("Enter The Tag please: ")
input2 = input("Enter the contents please: ").title()

def add_html_tags(tag, content):
    print('<'+ tag + '>'+ content +'</' +tag +'>')
    
# insted of repeated method call, I used input and call the function once
add_html_tags(input1, input2)
