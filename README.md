# Learn-Python-the-Hard-way-Notes

1.  String formatting
    *  %d will format a number for display
    *  %s will insert the presentation string representation of the object (i.e. str(o))
    *  %r will insert the canonical string representation of the object (i.e. repr(o))
2. Use \ to escape double quotes (or any other confusing things for python)
    *  ex. print ("double\"quotes ")
       *  output=> double"quotes
3. Use pydoc for documentation about built-in function/commands/operations for python
4. WITH in python =>
with handle the lifecycle of the object automatically, destroys it in the end. Calssic example is used with open file

   ```python
   with open('output.txt', 'w') as f:

    f.write('Hi there!')
   ```
eg. [ex16](ex16.py)
5. Iterator, Generator and Yield

 [Python Wiki for Generators ](https://wiki.python.org/moin/Generators)
 
 [Stackoverflow discussion about ](http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python)

6.  Usage of read() = > [ex16]()
  ```python
  """main function."""
  with open("test") as inputfile:
      indata = inputfile.read()
  with open("outputtest", 'w') as outputfile:
      outputfile.write(indata)
  ```
